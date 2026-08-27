# At the end you use Git bisect

- Score: 134 | [HN](https://news.ycombinator.com/item?id=45791882) | Link: https://kevin3010.github.io/git/2025/11/02/At-the-end-you-use-git-bisect.html

### TL;DR

`git bisect` applies binary search between a known good commit and a known bad one to identify the first revision exhibiting a reproducible failure. The author describes using it in a busy monorepo after a configuration change broke tests and logs offered little guidance; an automated test script narrowed hundreds of candidates to the offending commit. Commenters emphasized broader uses: hardware-dependent kernel regressions, determining how long bad data was produced, recovering design intent from commit messages, and locating subtle interactions missed during code review.

### Comment pulse

- Some saw bisect as most valuable in poorly tested codebases — counterpoint: others use it to recover causality even with strong tests.
- Small, focused commits make the identified revision easier to understand and repair.

### LLM perspective

- View: Bisect converts reliable reproduction into a bounded history search, complementing rather than replacing observability.
- Impact: Teams can isolate regressions faster and recover the rationale surrounding their introduction.
- Watch next: Automating tests across commits while handling build failures, flaky tests, and dependent services.
