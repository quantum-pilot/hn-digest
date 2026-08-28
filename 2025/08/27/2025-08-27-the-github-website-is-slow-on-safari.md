# The GitHub website is slow on Safari

- Score: 446 | [HN](https://news.ycombinator.com/item?id=45037365) | Link: https://github.com/orgs/community/discussions/170758

### TL;DR

A GitHub Community thread reports that GitHub feels extremely slow in Safari, but the supplied discussion contains no measurements or official GitHub diagnosis. Several commenters blame GitHub’s client-heavy interface and report sluggishness in other browsers, especially on pull requests containing more than a thousand files. Others point to recently merged WebKit rendering and CSS improvements as evidence that a Safari-specific bug contributed. The thread therefore supports a real user-visible problem, not a settled explanation of its root cause.

### Comment pulse

- Participants argued over React and SPA architecture, with others stressing implementation quality rather than any single framework.
- Reports of Chrome struggling on enormous pull requests suggest GitHub also has browser-independent scaling problems.

### LLM perspective

- View: The evidence suggests interacting GitHub and WebKit costs, not a clean choice between browser bug and site regression.
- Impact: Poor cross-browser performance effectively narrows browser choice and makes large code reviews harder to complete.
- Watch next: Compare reproducible traces before and after the cited WebKit fixes across ordinary pages and very large pull requests.
