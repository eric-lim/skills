---
name: code-review
description: "Performs a multi-stage code review on git diffs and branch revisions."
---

This is a multi-stage workflow that coordinates several subagents and automated checks to perform a comprehensive code review.

## Mandatory Rules
> [!IMPORTANT]
> The following rules are strict, mandatory, and MUST be followed without exception by the main orchestrator agent and all child subagents:
> 
> 1. **Read-Only Inspection:** The main orchestrator agent and all child subagents MUST NOT modify any existing source code files or documents under review. The review process is strictly read-only; all findings, suggested diffs, and feedback must be written only to the final generated review report.
> 2. **Scope Constraint:** The main orchestrator agent and all child subagents MUST focus their review and findings strictly on modified or newly introduced code within the target git diff range. They must NOT report issues or formatting nits on unmodified legacy code or documents that are outside the scope of the diff.

### Model Definition Guidelines
* **Fast Model:** Optimized for speed and lower cost (e.g., Claude Haiku, Gemini Flash, GPT mini).
* **Reasoning Model:** Optimized for deep analytical tasks, logic verification, and complex audits (e.g., Claude Sonnet, Gemini Pro, GPT/GPT-o series).

## Stage 1: Setup & Target Scoping
1. **Log Stage Entry**: Print a line divider and the header: `"\n----------------------------------------\n🚀 [Stage 1: Setup & Target Scoping]\n"` to the standard output.
2. **Identify Revision Target:**
   - Resolve the comparison target branch (e.g. `main` or merge-base).
   - If not specified, ask the user: "What branch or commit should I compare against? (Default: main)".
3. **Verify Git Range:**
   - Run `git diff --stat <target>...HEAD` to verify changes exist.
   - If diff is empty, announce "No changes to review since <target>." and halt.

## Stage 2: Context Resolution
1. **Log Stage Entry**: Print a line divider and the header: `"\n----------------------------------------\n🔍 [Stage 2: Context Resolution]\n"` to the standard output.
2. **Locate Specifications (Spec Resolution Chain):**
   To handle varying project structures, resolve the originating specification using the following fallback chain:
   * **Explicit argument**: Check if a specific file path was passed as an argument (e.g. `--spec <path>`).
   * **Config Registry**: Look for workspace-level files (e.g. `agents.json`, `.agents/config.json`) defining `"specs_dir"` or custom paths.
   * **Commit Message Parser**: Extract commit hashes in the diff range (`git log <target>..HEAD --oneline`) and identify issue references (e.g. `#123`, `JIRA-881`). Fetch issue descriptions using the GitHub CLI (`gh issue view`) or appropriate MCP tools.
   * **Convention Scanning**: Scan common paths: root or subfolder `plan.md`, `implementation_plan.md`, `spec.md`, `prd.md`, or folders like `/docs`, `/specs`, `/design`.
   * **Branch Heuristic**: Search for files containing a substring match of the current branch name (e.g., branch `feature/auth-refresh` matching `docs/auth-refresh.md`).
   * **Interactive Fallback**: If no specs are resolved, prompt the user: "Where is the spec file for this branch? (Type 'none' to skip Spec subagent review)".
3. **Locate Standards & Style Guides:**
   * Gather any root or sub-folder guidelines (e.g., `agents.md`, `CLAUDE.md`, `CODING_STANDARDS.md`).
4. **User Context Audit & Approval Gate:**
   * **Print Summary**: You MUST print a summarized registry of all resolved context to the standard output titled "Guidelines & Specs Found" categorized by:
     * **Style**: Associated style guides, standards, and style check checklist items.
     * **Architecture**: Associated design references and architectural checklist items.
     * **Specification**: Resolved spec files/issues and spec checklist items.
   * **Prompt**: Once the summary is printed, prompt the user: *"I have gathered the following context for Stage 3. If there are any mistakes or missing files, please specify them now. Ready to proceed? (Y/n)"*
   * Halt execution until the user validates the context list or overrides file paths.

## Stage 3: Parallel Review & Testing
> [!IMPORTANT]
> The orchestrator MUST delegate the Style, Architecture, and Specification reviews to three separate isolated subagent instances. The main orchestrator is strictly forbidden from executing these reviews inline within its own conversation or execution context.

Launch three isolated subagents and run the automated test suite in parallel to minimize latency.

**Crucial Rule**: Instruct all subagents to focus their findings strictly on modified or newly introduced code within the git diff range, avoiding style/design complaints about unmodified legacy code. All subagents must output findings using the standardized block schema (specifying File, Line Range using `L<start>-L<end>`, Severity, and Recommendation with a unified diff if applicable).

1. **Log Stage Entry**: Print a line divider and the header: `"\n----------------------------------------\n⚡ [Stage 3: Parallel Review & Testing]\n"` to the standard output.
2. **Style Subagent (Fast Model):**
   - **Bypass Flag:** Skip execution via the `--no-style` flag.
   - Prompt: Load from `./resources/subagents/style-subagent.md`.
   - Input: Git diff, guidelines found (e.g., agents.md, CLAUDE.md), baseline Fowler smells.
   - Task: Identify syntax rule violations, style deviations, and classic code smells in modified code, assigning `Important` or `Minor` severity.
3. **Arch Subagent (Reasoning Model):**
   - **Bypass Flag:** Skip execution via the `--no-arch` flag.
   - Prompt: Load from `./resources/subagents/arch-subagent.md`.
   - Input: Git diff.
   - Task: Review high-level design decisions, performance bottlenecks, concurrency risks, security hazards, and system reliability in modified code, assigning `Critical`, `Important`, or `Minor` severity.
4. **Spec Subagent (Reasoning Model):**
   - **Bypass Flag:** Skip execution via the `--no-spec` flag.
   - Prompt: Load from `./resources/subagents/spec-subagent.md`.
   - Input: Git diff, spec/plan documents.
   - Task: Review functional correctness, missing plan requirements, testing efficacy, production readiness, and scope creep in modified code, assigning `Critical`, `Important`, or `Minor` severity.
5. **Automated Test Run:**
   - **Bypass Flag:** Skip execution via the `--no-tests` flag.
   - Task: Detect the test suite in the codebase (e.g., `npm test` for Node, `pytest` for Python) and execute it. Save all output logs for the verification phase in Stage 4.

## Stage 4: Verification & Synthesis
Run the Verification Subagent sequentially after Stage 3 parallel processes complete:

1. **Log Stage Entry**: Print a line divider and the header: `"\n----------------------------------------\n🛡️ [Stage 4: Verification & Synthesis]\n"` to the standard output.
2. **Verification Agent (Reasoning Model):**
   - **Bypass Flag:** Skip execution via the `--no-verify` flag.
   - Prompt: Load from `./resources/subagents/verification-subagent.md`.
   - Input: Git diff, active linter rules, aggregated Stage 3 subagent findings, and results/logs from the Stage 3 Automated Test Run.
   - Task: Review the findings against the diff and test results to filter out false positives, pre-existing/legacy code issues, compiler-checked items, and linters' auto-fixes. Apply deduplication merging with single-source attribution priority (Spec > Arch > Style), legacy checks, and the Test Corroboration Matrix.

## Stage 5: Calibration & Presentation
1. **Log Stage Entry**: Print a line divider and the header: `"\n----------------------------------------\n📊 [Stage 5: Calibration & Presentation]\n"` to the standard output.
2. **Calibrate Severity & Verdict:**
   - Ensure the report starts by highlighting **Strengths** (accurate praise).
   - Classify remaining issues into **Critical** (breaks correctness/security), **Important** (architecture/missing features), and **Minor** (style/nitpicks).
   - **Attribute Unique Source**: Verify each finding is attributed to exactly **one** primary subagent (`Style`, `Arch`, or `Spec`).
   - **Tally Verification**: Verify that the counts in the "Findings Breakdown" table are the strict mathematical sum of the rows and columns, and correspond exactly to the number of issues listed in the detailed sections.
   - Determine the **Review Verdict** recommendation based on findings:
     * **Merge**: Approved to merge (no Critical or Important issues, and all tests passed).
     * **Merge with fixes**: Approved to merge after minor/important issues are resolved (no Critical issues, but some Important/Minor issues present).
     * **Hold**: Do not merge yet (any Critical issues present, or the automated test suite failed).

3. **Output Format:**
   - Generate a single report markdown file using the structure in `./resources/templates/report-template.md`.
   - **Storage Destination:**
     * By default, save the report to `.code-review/report-YYYYMMDD-HHMMSS.md` (e.g., `.code-review/report-20260709-140921.md`), creating the `.code-review/` directory in the repository root if it does not exist.
     * Support overriding the output destination path via an explicit CLI argument (e.g., `--output <path>`) or workspace config setting.
     * Print the absolute path of the generated report to the terminal upon completion.
