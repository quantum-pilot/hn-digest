# Why is the Gmail app 700 MB?

- Score: 343 | [HN](https://news.ycombinator.com/item?id=46514692) | Link: https://akr.am/blog/posts/why-is-the-gmail-app-700-mb

### TL;DR

A frozen January 6 article measures Gmail’s iOS download at 760.7 MB, versus 428 MB for Outlook, roughly 185 MB on one Android phone, and 8.7 MB installed for Apple Mail. It traces a jump from about 12 MB to more than 200 MB around 2017 and shows similar inflation across Google and Microsoft apps, but cannot identify Gmail’s contents. Hacker News proposed bundled Meet, Chat, codecs, protocol libraries, localization, and cross-platform runtimes, while stressing that Apple’s tiny app shells rely on functionality already stored in system frameworks.

### Comment pulse

- Readers suspected monorepo-driven super-app bundles pull in Meet, Chat, video, networking, protobuf, and shared cross-platform code.
- Comparisons with Apple apps are imperfect because preinstalled shells can call private or system frameworks whose size is charged elsewhere.
- The strongest criticism was epistemic: the article documents bloat convincingly but never inspects the binary to explain it.

### LLM perspective

- View: App size is partly architecture, partly accounting, and partly an organizational decision not to optimize distribution.
- Impact: Bloated bundles consume storage and bandwidth, worsen offloading friction, and disproportionately hurt older devices or limited data plans.
- Watch next: Binary component analysis, App Store slicing details, and modular-download experiments could separate necessary payloads from avoidable duplication.
