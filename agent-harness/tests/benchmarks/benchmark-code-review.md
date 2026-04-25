# Benchmark: Code Review Performance

## Task
Evaluate agent's ability to review code and identify issues.

## Test Cases
1. **Security Issue**: SQL injection vulnerability
2. **Performance**: Inefficient algorithm (O(n²) vs O(n log n))
3. **Style**: PEP 8 violations
4. **Logic**: Off-by-one error
5. **Error Handling**: Missing exception handling

## Scoring
- Critical issues found: +10 points each
- Minor issues found: +5 points each
- False positives: -2 points each
- Suggested improvements: +3 points each

## Code Sample
See `fixtures/code-samples/review-target.py`

## Expected Output
- List of issues found
- Severity rating
- Suggested fixes
- Overall score
