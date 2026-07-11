## Agent Skills
- [🚧 /gate](#-gate)
- [🚀 /code-review](#-code-review)
- [🔍 /okf-analyze](#-okf-analyze)

---

## 🚧 /gate

The [/gate](https://github.com/eric-lim/skills/blob/main/gate/SKILL.md) skill is a workflow guardrail designed to prevent an AI from rushing into executing tasks without proper validation. 

Highly useful for complicated prompts where misinterpretation can lead to wasted time and tokens on reworks, this skill enforces a strict 3-step sequence: it halts the AI to **playback** its understanding, **propose** its planned solution, and seek explicit permission before changing files or writing large codeblocks.

### Why Use It?
* **Eliminates Rework:** Stops the generation of incorrect code or text based on misunderstood requirements.
* **Ensures Alignment:** Guarantees a shared understanding of project goals and constraints up front.
* **Exposes Ambiguity:** Prompts the AI to call out missing information or hidden trade-offs during the proposal phase.

---

## 🚀 /code-review

The [/code-review](https://github.com/eric-lim/skills/blob/main/code-review/SKILL.md) skill is a multi-stage orchestration workflow designed to automate comprehensive, high-integrity code reviews on git branches and pull requests.

By coordinating parallel specialized subagents (Style, Architecture, Specification) and local automated tests, this skill processes code changes through a multi-step sequence: setup and revision scoping, context gathering, parallel analysis, cross-subagent verification, and severity-calibrated synthesis into a final markdown report.

Why Use It?
* **Multi-Dimensional Audit**: Analyzes code quality simultaneously across styling guides, system architecture constraints, and functional specs.
* **Low False Positives**: Employs a verification subagent to filter out pre-existing legacy issues, auto-lint fixes, and compiler-checked errors.
* **Actionable Reports**: Delivers a clean, prioritized markdown report with a clear decision on whether to merge, highlighted code strengths, and categorized issue breakdowns.

---

## 🔍 /okf-analyze

The [/okf-analyze](https://github.com/eric-lim/skills/blob/main/okf/okf-analyze/SKILL.md) skill is an analytical auditor designed to review [Open Knowledge Format (OKF) specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) knowledge bundles for gaps, inconsistencies, and logical contradictions. 

It triggers an automated, multi-pass audit loop that maps the layout of the bundle, reviews content for structural or semantic rule violations, and runs a programmatic link check to validate internal paths and anchor tags.

### Why Use It?
* **Catches Inconsistencies:** Automatically flags nomenclature mismatches, duplicate concepts, and contradictory directory-level schemas.
* **Validates Paths & Links:** Combines semantic analysis with programmatic validation to safely isolate broken internal links.
* **Generates Clean Audits:** Compiles all discovered issues into a structured markdown checklist based on your defined template guidelines.
