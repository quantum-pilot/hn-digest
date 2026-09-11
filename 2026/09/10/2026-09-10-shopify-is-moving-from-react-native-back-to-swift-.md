# Shopify is moving from React Native back to Swift and Kotlin

- Score: 1058 | [HN](https://news.ycombinator.com/item?id=49643982) | Link: https://shopify.engineering/back-to-native

### TL;DR

Shopify says improved coding agents erased enough of React Native’s cross-platform cost advantage to justify rebuilding its mobile apps in Swift and Kotlin. Its Shop rewrite reportedly reached stores in 12 weeks; the larger Shopify app is underway. The company describes Helix, a checkpointed workflow requiring tests, visual review, adversarial review, and human approval, plus a headless CLI for faster agent feedback. Commenters split between seeing native development newly practical and questioning maintenance, validation, staffing, and whether Shopify’s scale generalizes.

### Comment pulse

- Agents can make dual-native development practical → one commenter reports rebuilding a 15–20-screen app overnight, then polishing it for days.
- Two codebases still impose costs → skeptics question Android evaluation without platform expertise and warn that generated implementations still require maintenance.
- Shopify’s conclusion may not generalize → debate centers on organizational scale, app complexity, and whether staffing comparisons are meaningful.

### LLM perspective

- View: This is less a framework verdict than a claim that agent economics can overturn architecture decisions.
- Impact: Mobile teams may reevaluate abstraction layers when agents can translate, test, and review platform-specific implementations reliably.
- Watch next: Compare long-term defect rates, parity effort, accessibility, performance, and developer staffing after every migration ships.
