# Wikipedia was in read-only mode following mass admin account compromise

- Score: 857 | [HN](https://news.ycombinator.com/item?id=47263323) | Link: https://www.wikimediastatus.net

- TL;DR  
An internal Wikimedia test accidentally unleashed a self-propagating JavaScript worm, forcing Wikipedia and sister wikis into temporary read-only mode. A staff security engineer bulk-loaded random user scripts under a highly privileged account; one was a two‑year‑old malicious script from Russian Wikipedia that injected itself into global JS, hid UI, vandalized pages, and deleted articles under admin accounts. Commenters liken it to the Samy MySpace worm and criticize Wikimedia’s practice of allowing user-supplied JS and testing on production.

- Comment pulse  
  - Root cause: security engineer bulk-loaded random user scripts; one was old XSS worm, which leveraged global JS privileges and forced emergency read-only mode.  
  - Worm behavior: persists via Common.js, hides admin UI hints, vandalizes random pages, and mass-deletes articles when run under admin accounts, echoing early 2000s XSS worms.  
  - Design debate: allowing user-injected JavaScript is powerful but enables XSS worms and potential credential theft — counterpoint: strict scopes and auditing can keep risk acceptable.

- LLM perspective  
  - View: Core issue is governance: excessive privileges, live-data testing, and executable user content combined into a predictable failure mode.  
  - Impact: Expect Wikimedia to restrict JS capabilities, segregate test environments, and audit high-privilege accounts more aggressively after this incident.  
  - Watch next: Watch for per-wiki security policies, sandboxed scripting models, and analyses of whether AI-assisted tools helped create or detect worms.
