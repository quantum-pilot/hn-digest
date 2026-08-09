# We found an undocumented bug in the Apollo 11 guidance computer code

- Score: 376 | [HN](https://news.ycombinator.com/item?id=47673005) | Link: https://www.juxt.pro/blog/a-bug-on-the-dark-side-of-the-moon/

### TL;DR

JUXT says Claude and its Allium behavioral specification language distilled 130,000 lines of Apollo Guidance Computer assembly into 12,500 lines of specifications, exposing an error path that failed to release the LGYRO gyro lock. A cage event during torque could therefore block later gyro work until some recovery. However, AGC restoration leader Mike Stewart confirmed the defect while overturning the article’s novelty and danger claims: surviving reports logged it during SATANCHE testing, documented recovery for Apollo 14, and fixed it before Apollo 15; starting another program already cleared the lock.

### Comment pulse

- Stewart said the proposed two-instruction fix was incomplete; the actual repair also woke waiting jobs and restructured the relevant code.
- He corrected other historical claims about rope verification, personnel, scheduler behavior, and the electrical cause behind Apollo 11’s 1202 alarms.
- Readers valued formalized resource lifecycles — counterpoint: several criticized a dramatic Collins scenario that normal program changes make impossible.

### LLM perspective

- **View:** The specification surfaced a genuine lock leak, but expert archival knowledge was essential to interpret its operational significance.
- **Impact:** AI-assisted formalization can expose neglected paths; unchecked narrative framing can turn valid findings into misleading historical claims.
- **Watch next:** Authors should reconcile the anomaly report, published fix, recovery notes, and expert corrections with their reproducible specification.
