# We found an undocumented bug in the Apollo 11 guidance computer code

- Score: 376 | [HN](https://news.ycombinator.com/item?id=47673005) | Link: https://www.juxt.pro/blog/a-bug-on-the-dark-side-of-the-moon/

### TL;DR
An AI-assisted behavioural specification of Apollo 11’s guidance computer revealed a genuine lock-leak bug in the gyro control code: an error path (`BADEND`) fails to release the `LGYRO` resource, potentially blocking future gyro torques. The authors used Allium, a spec language, plus Claude to model resource lifecycles across all paths and expose the missing unlock. Hacker News experts confirm the bug is real but note it was found during Apollo testing, later fixed, and could not have caused the dramatic failure scenario described.

---

### Comment pulse
- Bug validity → AGC historian: yes, real and logged as anomaly L-1D-02; fixed between Apollo 14–15; real failure mode yields alarms, not a silent hang.  
- Historical/context corrections → LGYRO cleared on program changes, reducing risk; roles (rope mother), scheduling behavior, and 1202 root cause subtly misdescribed.  
- Storytelling and AI framing → Some dislike the dramatized “elbow flip” scenario and marketing tone; others defend narrative as needed to explain subtle failures.

---

### LLM perspective
- View → AI-guided behavioural specs are well-suited to uncover lifecycle bugs in complex, poorly documented legacy systems.  
- Impact → Safety-critical and infrastructure software can gain new assurance layers without rewriting into modern languages or runtimes.  
- Watch next → Open benchmarks comparing AI-assisted specs vs traditional testing, and integration into CI for large, long-lived codebases.
