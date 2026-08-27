# You did this with an AI and you do not understand what you're doing here

- Score: 982 | [HN](https://news.ycombinator.com/item?id=45330378) | Link: https://hackerone.com/reports/3340109

### TL;DR

A HackerOne submission claimed a critical cURL cookie-parsing overflow, but its proof of concept merely called `strlen` on a deliberately unterminated local buffer and never exercised libcurl. cURL staff requested the exact faulty source line; the reporter then acknowledged the error, retracted the claim, and asked that it be closed as invalid. HN readers saw obvious AI-generated prose and focused on the external cost of unverified submissions, arguing that users must personally validate and own AI-assisted security reports before burdening maintainers.

### Comment pulse

- Human review was effectively absent → the elaborate severity claims collapsed because the reproducer never invoked the targeted code.
- Saved effort became transferred effort → maintainers had to investigate and rebut a report that established no cURL vulnerability.
- AI assistance is not the problem alone → commenters emphasize accountability when submitting generated work under one’s own name.

### LLM perspective

- View: Polished technical language can conceal a missing causal link between evidence and claim.
- Impact: Unfiltered automated reports increase triage costs and may crowd out legitimate vulnerability research.
- Watch next: Reproducer requirements, submission-rate controls, provenance signals, and sanctions for repeated unverifiable reports.
