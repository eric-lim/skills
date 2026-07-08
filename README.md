## 🚧 /gate

The [/gate](https://github.com/eric-lim/skills/blob/main/gate/SKILL.md) skill is a workflow guardrail designed to prevent an AI from rushing into executing tasks, writing large codeblocks, or changing files without proper validation. 

It forces the AI to stop, playback its understanding, and seek explicit user permission before proceeding.

### Why Use It?
* **Prevents Waste:** Stops the AI from generating pages of incorrect code or text based on a misunderstood prompt.
* **Encourages Alignment:** Guarantees a shared understanding of project requirements and constraints before work begins.
* **Promotes Honesty:** Forces the AI to call out ambiguity, missing information, or hidden trade-offs up front.

### How it Works
The `/gate` command forces a strict 3-step sequence:

1. **Playback:** The AI summarizes your goal to confirm alignment.
2. **Propose:** The AI outlines its solution, trade-offs, and questions.
3. **Gate:** The AI halts completely and waits for your approval before making changes.
