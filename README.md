## 📌 List of Agent Skills
* [🚧 /gate](#-gate)
* [🔍 okf-analyze](#-okf-analyze)

## 🚧 /gate

The [/gate](https://github.com/eric-lim/skills/blob/main/gate/SKILL.md) skill is a workflow guardrail designed to prevent an AI from rushing into executing tasks without proper validation. 

This is highly useful for complicated prompts where misinterpretation by AI can lead to wasted time and tokens on reworks. This skill forces the AI to stop, playback its understanding, propose its solution, and seek explicit permission before changing files or writing large codeblocks.

### Why Use It?
* **Prevents Waste:** Stops the generation of incorrect code or text based on misunderstood requirements.
* **Ensures Alignment:** Guarantees a shared understanding of project goals and constraints up front.
* **Exposes Ambiguity:** Prompts the AI to call out missing information or hidden trade-offs before starting.

### How it Works
The `/gate` command forces a strict 3-step sequence:

1. **Playback:** The AI summarizes your goal to confirm alignment.
2. **Propose:** The AI outlines its planned solution, questions, and trade-offs.
3. **Gate:** The AI halts completely and waits for your explicit approval to proceed.

---

## 🔍 /okf-analyze

The [/okf-analyze](https://github.com/eric-lim/skills/blob/main/okf/okf-analyze/SKILL.md) skill is an analytical auditor designed to review Open Knowledge Format (OKF) knowledge bundles for gaps, inconsistencies, and logical contradictions.

### Why Use It?
* **Catches Inconsistencies:** Automatically flags nomenclature mismatches, duplicate concepts, and contradictory directory-level schemas.
* **Validates Paths & Links:** Combines semantic analysis with a Python validation script to isolate broken links and anchor tags.
* **Generates Clean Audits:** Outputs a structured, tracking-ready markdown issue checklist based on your defined template.

### How it Works
The `/okf-analyze` command forces a strict 3-step audit loop:

1. **Discovery:** Maps out the layout and reads primary indexing and localized configuration files.
2. **Multi-Pass Audit:** Evaluates content for text discrepancies, placeholder gaps, and rule violations.
3. **Automated Check:** Executes an internal script to check relative paths, compiling all findings into an untracked issue report.