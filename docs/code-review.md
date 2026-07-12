# 🚀 /code-review

The `/code-review` skill is a multi-stage orchestration workflow designed to automate comprehensive, high-integrity code reviews on git branches and pull requests.

---

## Why Use This Skill?

It runs specialized subagents (Style, Architecture, Specification) and automated tests in parallel to analyze your changes, filter out false positives, and compile the findings into a single structured markdown report.

Why Use It?
* **Multi-Dimensional Audit**: Analyzes code quality simultaneously across styling guides, system architecture constraints, and functional specs.
* **Minimize False Positives**: Employs a verification agent to actively filter out false positives and speculative warnings, leaving only real, actionable issues.
* **Actionable Reports**: Delivers a clean, prioritized markdown report with a clear decision on whether to merge, highlighted code strengths, and categorized issue breakdowns.

---

## Architecture & How It Works

The orchestrator executes a structured, 5-stage workflow to transition from an unreviewed Git diff to a comprehensive, calibrated markdown report:

```text
[Stage 1: Target Scoping] ──> [Stage 2: Context Resolution]
                                        │ (Approval Gate)
                                        ▼
                            [Stage 3: Parallel Review]
                            ├── Style Subagent (Fast Model)
                            ├── Arch Subagent  (Reasoning Model)
                            ├── Spec Subagent  (Reasoning Model)
                            └── Automated Test Suite Execution
                                        │
                                        ▼
                            [Stage 4: Verification & Synthesis]
                                        │ (Deduplication & Test Matrix)
                                        ▼
                            [Stage 5: Calibration & Presentation]
                                        │
                                        ▼
                            📂 .code-review/report-*.md
```

### The 5-Stage Pipeline

1. **Stage 1: Setup & Target Scoping**
   Automatically resolves the target Git revision to compare against using an intelligent Git fallback chain:
   * Explicit Arguments ➔ Upstream Tracking ➔ Git Merge-Base Heuristics ➔ Local Fallbacks.
   * Runs `git diff` checks to ensure a valid Git diff range exists before consuming resources.

2. **Stage 2: Context Resolution & User Approval Gate**
   Scans the workspace to map out relevant specifications and project guidelines (`CLAUDE.md`, `agents.md`).
   * Halts and presents a unified registry to the user, ensuring the review layer has the exact context required.

3. **Stage 3: Parallel Review & Testing**
   Spins up isolated subagent instances concurrently alongside your native test suite (`npm test`, `pytest`, etc.) to prevent context contamination and drastically reduce total execution latency:
   * **Style Subagent:** Audits code formatting, type safety, defensive boundaries, and structural code smells against the **Style Checklist** and **Smells Guide**.
   * **Arch Subagent:** Scrutinizes high-level design, data structure choices, concurrency, and security vulnerabilities against the **Architecture Checklist**.
   * **Spec Subagent:** Evaluates implementation completeness against the original design requirements and checks for hidden scope creep against the **Specification Checklist**.

4. **Stage 4: Verification & Synthesis**
   A sequential **Verification Subagent** acts as the quality filter:
   * Merges duplicate findings from the subagents.
   * Checks if flagged lines are actually part of the diff (discarding legacy code alerts).
   * Correlates bug risks against the automated test log output.

5. **Stage 5: Calibration & Presentation**
   Compiles the finalized findings into a beautifully structured, scannable Markdown report:
   * Tallies findings by severity (**Critical, Important, Minor**).
   * Highlights code **Strengths**.
   * Issues an actionable **Review Verdict**: `Merge`, `Merge with fixes`, or `Hold`.

---

## Repository Structure

The core engine relies on a modular pair of checklists and subagent system instructions:

```text
code-review
├── SKILL.md                  # Main Orchestrator Workflow & Entrypoint
├── checklists/
│   ├── arch-checklist.md     # Design, Scalability, and Security constraints
│   ├── spec-checklist.md     # Feature completeness and test efficacy rules
│   ├── style-checklist.md    # Code quality and DRY guidelines
│   └── severity.md           # Definite thresholds for Critical/Important/Minor
└── subagents/
    ├── arch-subagent.md      # System prompt for the Architecture Auditor
    ├── spec-subagent.md      # System prompt for the Specification Auditor
    ├── style-subagent.md     # System prompt for the Lint/Style Auditor
    └── verification-subagent.md # System prompt for the Synthesis & Deduplication Filter
```

## Configuration & Flags

Fine-tune or skip execution layers dynamically using standard CLI flags:

* `--target <branch/commit>`: Explicitly set the base revision target to diff against.
* `--spec <path>`: Explicitly point the Spec Subagent to a specific requirement file.
* `--output <path>`: Override the default `.code-review/report-YYYYMMDD-HHMMSS.md` destination.
* `--no-style` | `--no-arch` | `--no-spec`: Bypass individual subagent evaluation tracks.
* `--no-tests`: Skip automated test suite execution logs integration.
* `--no-verify`: Skip Stage 4 synthesis and output raw aggregated data.

---

## Best Practices

* **Prioritize Repository Guidelines:** The *Style Subagent* treats project context files like `CLAUDE.md` or `agents.md` as strict laws. If a heuristic code smell (e.g., Primitive Obsession) contradicts a project style file, **the project guideline always wins**.
* **Run Pre-Commit or In CI:** Integrate this tool inside your local pre-push workflows or run it as a GitHub Action step to block failing pull requests automatically if the review verdict returns a `Hold`.