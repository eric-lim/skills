# Code Review Report: [Scope / Revision Target]
**Date**: [Date and Time]

## 1. Executive Summary
* **Review Verdict**: [Merge | Merge with fixes | Hold]
* **Reasoning**: [1-2 sentence technical assessment summarizing why this decision was reached.]

---

## 2. Review Summary

### Automated Test Run
* **Status**: [Passed | Failed | Skipped]
* **Notes**: [Brief summary of failing tests, coverage details, or if bypassed]

### Findings Breakdown
| Subagent | Critical (Must Fix) | Important (Should Fix) | Minor (Nice to Have) | Total |
| :--- | :---: | :---: | :---: | :---: |
| **Style** | [Count] | [Count] | [Count] | [Total] |
| **Architecture (Arch)** | [Count] | [Count] | [Count] | [Total] |
| **Specification (Spec)** | [Count] | [Count] | [Count] | [Total] |
| **Total** | [Total] | [Total] | [Total] | [Grand Total] |

---

## 3. Strengths
[Highlight what was implemented well. Be specific, referencing files or patterns. Accurate praise builds trust and collaboration.]
* **[Strength Topic]**: [Detailed description of the strength and its impact.]

---

## 4. Issues & Findings

### Critical (Must Fix)
[Bugs, safety issues, database lock risks, security vulnerabilities, or major spec deviations that will cause production failure.]
1. **[Issue Name]**
   - **File**: `[file path]` (Lines L[start]-L[end])
   - **Subagent Source**: [Style | Arch | Spec (select the single primary source)]
   - **Description**: [What's wrong and why it matters.]
   - **Suggested Fix**: [Brief explanation of the proposed change.]
     ```diff
     -old_code_line (start line with '-' character, then code indentation)
     +new_code_line (start line with '+' character, then code indentation)
     ```

### Important (Should Fix)
[Design defects, poor separation of concerns, test coverage gaps, performance issues, or architectural violations.]
1. **[Issue Name]**
   - **File**: `[file path]` (Lines L[start]-L[end])
   - **Subagent Source**: [Style | Arch | Spec (select the single primary source)]
   - **Description**: [What's wrong and why it matters.]
   - **Suggested Fix**: [Brief explanation of the proposed change.]
     ```diff
     -old_code_line (start line with '-' character, then code indentation)
     +new_code_line (start line with '+' character, then code indentation)
     ```

### Minor (Nice to Have)
[Non-blocking style nits, simple optimization opportunities, or documentation polish.]
1. **[Issue Name]**
   - **File**: `[file path]` (Lines L[start]-L[end])
   - **Subagent Source**: [Style | Arch | Spec (select the single primary source)]
   - **Description**: [Detailed suggestion for style or doc improvement.]
