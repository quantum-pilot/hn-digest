# GCC steering committee announces AI policy

- Score: 231 | [HN](https://news.ycombinator.com/item?id=49108685) | Link: https://lwn.net/Articles/1086041/

### TL;DR
GCC’s steering committee has adopted an AI policy that, per discussion, effectively forbids significant LLM-generated contributions, driven by two concerns: a growing flood of low-quality, fully automated “agent” PRs that dump maintenance burdens on humans, and legal uncertainty around mixing LLM output with GPL-licensed code. Some maintainers welcome clear rules and even use “no-AI” prompts in repos to shut down agents; others argue blanket bans unfairly block careful, disclosed AI-assisted work from experienced contributors.

*Content unavailable; summarizing from title/comments.*

### Comment pulse
- Flood of autonomous LLM PRs is unreviewable → maintainers want policies to quickly reject agent spam and discourage non-human, unowned contributions.  
- Policy seems to forbid even disclosed AI-assisted patches → long-time contributors feel excluded — counterpoint: others argue human authorship guarantees are essential for GPL compliance.  
- Unclear copyright status of LLM output worries free-software projects → they fear accepting AI code could undermine GPL licensing or import undisclosed proprietary snippets.  

### LLM perspective
- View: Repository-level AI policies will become standard hygiene, like contribution guidelines, to filter automation without banning all tool-assisted work.  
- Impact: Tool vendors may adapt agents to read these policies and automatically avoid repos or modes disallowed by maintainers.  
- Watch next: Expect test cases: contributors challenging blanket bans with demonstrably beneficial AI-assisted patches; how GCC handles those will set norms.
