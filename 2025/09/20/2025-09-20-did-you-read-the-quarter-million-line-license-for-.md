# Did you read the quarter-million-line license for your Slack app?

- Score: 103 | [HN](https://news.ycombinator.com/item?id=45308503) | Link: https://mastodon.mit.edu/@Eggfreckles/114825126857396420

### TL;DR

Slack’s macOS application includes a 15.2 MB, 272,516-line license file, but commenters clarify that it is not a single Slack license or terms-of-service agreement. It aggregates notices for third-party components embedded through Chromium, repeating licenses such as Apache 2.0, MIT, and LGPL across many dependencies. The discussion used the file as evidence of Electron’s software footprint and licensing complexity, while questioning why identical texts are not deduplicated. Others connected dependency bulk with concerns about ownership, self-hosting, and business reliance on hosted chat.

### Comment pulse

- The title is misleading → the file collects many dependency notices rather than one quarter-million-line agreement.
- Attribution does not scale cleanly → repeated permissive-license texts create a large compliance artifact that few users will inspect.
- Application bulk signals broader dependence → commenters compared Slack with self-hostable alternatives and older, smaller software stacks.

### LLM perspective

- View: License-file size measures dependency and attribution structure, not contractual burden on the end user.
- Impact: Packagers inherit compliance complexity while users face storage overhead and opaque software composition.
- Watch next: Explore SPDX metadata, deduplicated license bundles, dependency inventories, and reproducible compliance generation.
