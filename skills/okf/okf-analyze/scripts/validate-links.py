import os
import sys
import re
from typing import Set, Dict, List, Tuple, Optional

def slugify(text: str) -> str:
    """Mimic GitHub slugification by converting to lowercase, removing non-word/space/hyphen characters, and replacing spaces with hyphens."""
    # Mimic GitHub slugification
    text = text.lower()
    # Remove any characters that are not word characters, spaces, or hyphens
    text = re.sub(r'[^\w\s-]', '', text)
    # Replace spaces with hyphens
    text = re.sub(r'\s', '-', text)
    return text

def collect_anchors(file_path: str) -> Set[str]:
    """Scan a markdown file and collect slugified header texts to build a set of anchor names."""
    anchors: Set[str] = set()
    if not os.path.exists(file_path):
        return anchors
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("#"):
                match = re.match(r'^(#+)\s+(.*)$', line)
                if match:
                    header_text = match.group(2)
                    # Strip trailing '#' characters if any
                    header_text = re.sub(r'\s+#+$', '', header_text)
                    anchors.add(slugify(header_text))
    return anchors

def build_anchors_cache(okf_dir: str) -> Dict[str, Set[str]]:
    """Traverse okf_dir and pre-cache anchors for all markdown files to avoid redundant re-reading."""
    anchors_cache: Dict[str, Set[str]] = {}
    for root, _, files in os.walk(okf_dir):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                anchors_cache[full_path] = collect_anchors(full_path)
    return anchors_cache

def resolve_link_path(okf_dir: str, root: str, file_path: str, link_path: str) -> str:
    """Resolve the target path of a link relative to current file's directory or the OKF root directory."""
    if not link_path:
        return file_path
    if link_path.startswith("/"):
        # Absolute (bundle-relative) links start with '/'
        return os.path.normpath(os.path.join(okf_dir, link_path.lstrip("/")))
    return os.path.normpath(os.path.join(root, link_path))

def check_anchor(target_path: str, anchor: str, anchors_cache: Dict[str, Set[str]]) -> bool:
    """Verify if the slugified anchor exists in the target file, lazily updating the cache if needed."""
    target_anchors = anchors_cache.get(target_path)
    if target_anchors is None:
        # If cache missed (e.g. target is not in the walk list but exists), collect now
        target_anchors = collect_anchors(target_path)
        anchors_cache[target_path] = target_anchors
    return anchor in target_anchors

def check_single_link(
    okf_dir: str,
    root: str,
    file_path: str,
    text: str,
    link: str,
    anchors_cache: Dict[str, Set[str]]
) -> Tuple[Optional[str], bool]:
    """Validate a single markdown link. Returns a warning message (if broken) and a boolean indicating if it is an internal link."""
    # Skip external links
    if link.startswith(("http://", "https://", "mailto:")):
        return None, False

    parts = link.split("#")
    link_path = parts[0]
    anchor = parts[1] if len(parts) > 1 else None

    target_path = resolve_link_path(okf_dir, root, file_path, link_path)

    # Check if file exists
    if not os.path.exists(target_path):
        rel_file = os.path.relpath(file_path, okf_dir)
        rel_target = os.path.relpath(target_path, okf_dir)
        return (
            f"W_LINK: Broken link '{link}' ({text}) in '{rel_file}' "
            f"resolves to non-existent path '{rel_target}'"
        ), True

    # Check if anchor exists in target file
    if anchor and not check_anchor(target_path, anchor, anchors_cache):
        rel_file = os.path.relpath(file_path, okf_dir)
        rel_target = os.path.relpath(target_path, okf_dir)
        return (
            f"W_ANCHOR: Anchor '#{anchor}' in link '{link}' ({text}) in "
            f"'{rel_file}' does not exist in target file "
            f"'{rel_target}'"
        ), True

    return None, True

def process_file_links(
    okf_dir: str,
    root: str,
    file: str,
    anchors_cache: Dict[str, Set[str]]
) -> Tuple[int, List[str]]:
    """Scan and process all markdown links in a single markdown file, returning the count of checked internal links and any warnings."""
    file_path = os.path.join(root, file)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    warnings: List[str] = []
    checked_links = 0
    # Find all markdown links [text](path)
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    for text, link in links:
        warning, is_internal = check_single_link(okf_dir, root, file_path, text, link, anchors_cache)
        if is_internal:
            checked_links += 1
        if warning:
            warnings.append(warning)
    return checked_links, warnings

def print_warnings_report(warnings: List[str]) -> None:
    """Classify validation warning messages into link and anchor failures, printing reports for both."""
    w_links = [w for w in warnings if w.startswith("W_LINK")]
    w_anchors = [w for w in warnings if w.startswith("W_ANCHOR")]
    
    if w_links:
        print(f"\n⚠️ Found {len(w_links)} broken cross-link warnings (permitted by OKF spec but worth noting):")
        for w in w_links:
            print(f"  {w}")
    else:
        print("\n✅ All cross-links resolved successfully.")
        
    if w_anchors:
        print(f"\n⚠️ Found {len(w_anchors)} anchor mismatch warnings:")
        for w in w_anchors:
            print(f"  {w}")
    else:
        print("✅ All anchors matched successfully.")

def print_validation_results(checked_files: int, checked_links: int, warnings: List[str]) -> None:
    """Print overall summary execution statistics and warnings, then exit the program."""
    print(f"Validated {checked_files} files, checked {checked_links} links.")
    if warnings:
        print_warnings_report(warnings)
    else:
        print("\n✅ All links and anchors resolved successfully.")
    sys.exit(0)

def validate_links(okf_dir: str) -> None:
    """Walk through all files in okf_dir, caching headers, processing markdown links, and reporting results."""
    warnings: List[str] = []
    checked_files = 0
    checked_links = 0
    
    anchors_cache = build_anchors_cache(okf_dir)

    for root, _, files in os.walk(okf_dir):
        for file in files:
            if file.endswith(".md"):
                checked_files += 1
                links_count, file_warnings = process_file_links(okf_dir, root, file, anchors_cache)
                checked_links += links_count
                warnings.extend(file_warnings)

    print_validation_results(checked_files, checked_links, warnings)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
    else:
        # Default to current working directory
        target_dir = os.getcwd()
        
    if not os.path.isdir(target_dir):
        print(f"Error: {target_dir} is not a valid directory.")
        sys.exit(1)
        
    print(f"Auditing links in: {target_dir}")
    validate_links(target_dir)
