## Agent Skills
- [🚧 /gate](#-gate)
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

## 🔍 /okf-analyze

The [/okf-analyze](https://github.com/eric-lim/skills/blob/main/okf/okf-analyze/SKILL.md) skill is an analytical auditor designed to review [Open Knowledge Format (OKF) specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) knowledge bundles for gaps, inconsistencies, and logical contradictions. 

It triggers an automated, multi-pass audit loop that maps the layout of the bundle, reviews content for structural or semantic rule violations, and runs a programmatic link check to validate internal paths and anchor tags.

### Why Use It?
* **Catches Inconsistencies:** Automatically flags nomenclature mismatches, duplicate concepts, and contradictory directory-level schemas.
* **Validates Paths & Links:** Combines semantic analysis with programmatic validation to safely isolate broken internal links.
* **Generates Clean Audits:** Compiles all discovered issues into a structured markdown checklist based on your defined template guidelines.
