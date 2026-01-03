# Why users cannot create Issues directly

- Score: 711 | [HN](https://news.ycombinator.com/item?id=46460319) | Link: https://github.com/ghostty-org/ghostty/issues/3558

- TL;DR  
  Ghostty’s maintainer explains why ordinary users can’t open GitHub Issues: the project treats Issues as a curated backlog, not a support forum. Users must start in Discussions; maintainers convert only well-understood, reproducible problems or scoped feature work into Issues. This minimizes noise from misconfigurations, environment glitches, and vague requests that historically dominate reports. HN commenters debate whether this is pragmatic triage or needless friction, raising GitHub’s weak triage tools, fragmented bug reports, and expectations around open‑source maintainer responsibility.

- Comment pulse  
  - Issues-as-backlog, discussions-as-triage → cuts 80–90% noise from user errors, config problems, vague feature asks; GitHub Issues lacks strong triage tools—counterpoint: labels/statuses can emulate this.  
  - Dual trackers and off-GitHub reports fragment knowledge; e.g., Ghostty memory leak spread across discussions and social, never “issue-worthy”—counterpoint: maintainers say evidence still inconclusive.  
  - Some power users resent extra friction, reading it as arrogance; others rebut that unpaid maintainers may set any workflow, and users can fork.

- LLM perspective  
  - View: This pattern formalizes a two-stage funnel: community surfaces problems; maintainers curate a high-signal, implementation-ready backlog.  
  - Impact: Best suited to popular, under-resourced projects; for small tools, the overhead of Discussions may outweigh benefits.  
  - Watch next: GitHub could integrate issue/discussion states, default views, and triage roles, reducing the need for these ad-hoc workflows.
