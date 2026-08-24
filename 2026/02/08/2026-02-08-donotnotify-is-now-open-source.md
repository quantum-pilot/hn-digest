# DoNotNotify is now Open Source

- Score: 364 | [HN](https://news.ycombinator.com/item?id=46932192) | Link: https://donotnotify.com/opensource.html

### TL;DR

DoNotNotify’s developer published the app’s source, inviting inspection, bug reports, feature proposals, pull requests, forks, and independent verification of privacy claims. The announcement does not identify a license, architecture, audit result, or technical evidence beyond source availability. Commenters add that the Android app was AI-assisted and its author worried about exposing imperfect code. They overwhelmingly favored publication over shame, arguing useful free code is a gift and peer review enables learning. They also urged targeted tests for predictable generated-code failures, including malformed or oversized notifications, permission races, and filter-bypass encodings.

### Comment pulse

- Transparency is necessary, not sufficient → public code makes claims inspectable, but verification still requires reviewers, tests, and a clear license.
- Imperfection should not block contribution → commenters framed open source as a learning gift rather than résumé performance.
- AI-assisted notification code needs adversarial testing → malformed payloads, restarts, permission transitions, size extremes, MIME tricks, and encoded text probe boundaries.

### LLM perspective

- View: Opening the repository converts a privacy promise into an auditable proposition, without itself proving safety or quality.
- Impact: Android users and contributors can inspect and improve behavior; maintainers inherit disclosure, review, testing, and governance responsibilities.
- Watch next: License clarification, independent audit, test coverage, contributor activity, reproducible builds, release provenance, permission handling, and reported bypasses.
