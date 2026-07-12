# Verification Checklist

- **False Positives**:
  - Does the finding point to a bug or style violation that is actually correct/intended?
  - Is the finding based on a misunderstanding of local context?
- **Pre-existing Code**:
  - Is the finding flagging code that was NOT introduced or modified in the current diff range? (If so, discard it unless it directly causes a compiler/test failure in modified code).
- **Linter/Tooling Duplication**:
  - Is the finding already covered by standard compiler warnings or active linter rules? (If yes, discard it).
- **Test Corroboration**:
  - Do test failures and stack trace logs validate the suspected bug findings? (If a test fails on modified code, prioritize the related bug finding).
  - Does the test run pass successfully, suggesting that speculative concerns/warnings about logical correctness are likely false positives? (If so, consider downgrading or discarding speculative nits).
