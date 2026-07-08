---
name: okf-analyze
description: Audit and analyze an Open Knowledge Format (OKF) knowledge bundle to identify information gaps, ambiguities, contradictions, and structural or semantic inconsistencies.
compatibility: Requires Python 3
---

## Shortcuts
* `<folder>`: The directory containing the OKF knowledge bundle (defaults to `kb/`).
* `<issues>`: The output file for documenting issues, relative to the workspace root (defaults to `okf-issues.md`).
* `<issues-template>`: The template file used to structure the report (defaults to `.agents/skills/okf-analyze/assets/okf-issues-template.md`).

## Persona
Act as an independent reviewer auditing the [Open Knowledge Format (OKF) specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) compliance and logical consistency of the knowledge bundle in `<folder>`.

## Methodology

### 1. Map and Discovery
- List all directories and files under `<folder>` to understand the layout and index structure.
- Read primary index files (e.g., `<folder>/index.md`, and concept index files like `<folder>/technology/index.md` or `<folder>/business/index.md`).

### 2. Identify Discrepancies
Conduct a multi-pass analysis of the content:
- **Nomenclature Mismatches**: Look for terms that have been renamed in one file but remain in their legacy format in other files (e.g., concept categories, concept names, concept properties, or abbreviations).
- **Index & Log Gaps**: Cross-reference directory contents with their parent index files and the update log (`<folder>/log.md`) to verify that all created/refactored files are linked and documented accurately.
- **Requirement & Dependency Disconnects**: Look for rules, constraints, or mandates declared for a concept that lack the corresponding properties, permissions, or linked dependencies required to satisfy or enforce them (e.g., a schema concept requiring a validation algorithm that is not defined or linked anywhere in the bundle).
- **Conceptual Overlaps & Contradictions**: Identify duplicate concept definitions, redundant schemas, or conflicting specifications representing the same underlying entity or policy (e.g., two different subdirectories containing duplicate or conflicting schema definitions for the same user profile object).
- **Incomplete / Placeholder References**: Run the link validation script to programmatically detect broken relative or bundle-relative links and anchor mismatches (see below). Also manually look for draft placeholders (TBD) and links pointing to generic overview documents instead of specific roster or detail pages.
- **Exclude Tracked Issues**: Do not duplicate or flag issues in `<issues>` if they are already recorded as open questions, problems, or challenges in other tracking documents (e.g., a local `issues.md` or `status.md` file in a project subdirectory). Focus `<issues>` solely on untracked, conflicting, or global contradictions (e.g., if a local `payments/status.md` already tracks a broken API link, omit it from the main report).
- **Respect Directory-Level Rules**: During audits, locate any local `agents.md` or `claude.md` files. The rules defined in these files govern all concepts and child concepts recursively under the directory where the rules file resides. Check that concepts under these folders adhere to these local rules and flag violations. Note that `agents.md` and `claude.md` are configuration/rules files and do not require YAML frontmatter.

### 3. Run Automated Link Auditor
Run the link auditing script to programmatically scan for broken relative or bundle-relative file links and mismatched anchors:
```bash
python3 <path_to_skill_directory>/scripts/validate-links.py <folder>
```
*(Note: The agent should replace `<path_to_skill_directory>` with the actual absolute path to this skill directory on the filesystem).*
Document any discovered path mismatches or broken heading anchors under the **Structural & Reference Inconsistencies** section of `<issues>`.

### 4. Record Issues in `<issues>`
Generate a report at the root level (`/`) named `<issues>`.
- Read the template file `<issues-template>` and copy its structure.
- For each identified issue, format the header as an unchecked markdown task list item (e.g., `- [ ] **1.1 Item 1**`).
- Do NOT add OKF frontmatter to `<issues>` as it resides outside `<folder>`.

## Critical Rules
- **Relative Links**: All links within `<issues>` must be relative to the workspace root (e.g., `[<folder>/tech/technology-stack.md](./<folder>/tech/technology-stack.md)`). Never use absolute paths.



