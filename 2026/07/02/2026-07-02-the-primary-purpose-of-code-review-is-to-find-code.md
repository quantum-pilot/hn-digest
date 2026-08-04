# The primary purpose of code review is to find code that will be hard to maintain

- Score: 323 | [HN](https://news.ycombinator.com/item?id=48759870) | Link: https://mathstodon.xyz/@mjd/115096720350507897

### TL;DR

The essay argues that code review’s main job is not proving correctness or finding bugs, but detecting code reviewers cannot readily understand—and therefore future maintainers will struggle with—while its author still has context to improve it. HN broadly rejected that single-purpose framing. Commenters treated review as a layered gate for maintainability, defects, security, performance, design, consistency, malicious changes, and tests, plus knowledge transfer and shared ownership. They also noted that team-wide approval can preserve system awareness on small teams but becomes performative and slow as teams scale.

### Comment pulse

- Review transfers ownership → a pull request marks code’s passage from one author to the team, spreading context and exposing hidden dependencies.
- Static inspection does find defects → commenters cited leaked resources, missing awaits, swallowed errors, bad casts, security flaws, and performance mistakes.
- Universal approval does not scale → broad review builds awareness on teams near five engineers — counterpoint: larger groups drift into rubber-stamping.

### LLM perspective

- **View:** Review is a socio-technical control: its value comes from combining human comprehensibility, risk detection, accountability, and organizational learning.
- **Impact:** AI-generated volume raises reviewer workload, making scoped ownership, automation, and explicit review criteria more important than blanket approvals.
- **Watch next:** Measure escaped defects, review latency, reviewer coverage, knowledge concentration, and maintainability regressions by team size and change risk.
