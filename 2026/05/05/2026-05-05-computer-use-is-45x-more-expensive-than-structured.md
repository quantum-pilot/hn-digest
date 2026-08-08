# Computer Use is 45x more expensive than structured APIs

- Score: 286 | [HN](https://news.ycombinator.com/item?id=48024859) | Link: https://reflex.dev/blog/computer-use-is-45x-more-expensive-than-structured-apis/

### TL;DR

Reflex compared Claude Sonnet operating one admin task through screenshots and clicks versus structured HTTP tools. The unaided vision agent silently missed three off-screen reviews; after receiving a 14-step walkthrough, it succeeded but averaged 53 cycles, 17 minutes, and 551,000 input tokens. The API agent completed five runs identically in eight calls, about 20 seconds, and 12,151 tokens—roughly 45× fewer—because responses exposed filtering and pagination directly. The authors favor generated APIs for owned applications, reserving vision for third-party or legacy interfaces, while noting the narrow benchmark.

### Comment pulse

- Practitioners endorsed API- and CLI-first automation — counterpoint: visual control remains necessary when applications cannot be modified.
- Accessibility trees offer a structured middle layer, potentially improving both agent efficiency and neglected app accessibility.
- A hybrid could explore once, compile navigation into reusable workflows, then execute without repeated screenshot reasoning.

### LLM perspective

- The comparison measures interface entropy as much as model ability: pixels hide state that schemas expose explicitly.
- Reusable workflows need versioning, change detection, secret isolation, and safe replay when interfaces drift.
- Watch broader models, larger datasets, cached screenshots, hybrid DOM/vision agents, and total engineering cost.
