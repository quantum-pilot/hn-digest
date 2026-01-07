# Why is the Gmail app 700 MB?

- Score: 343 | [HN](https://news.ycombinator.com/item?id=46514692) | Link: https://akr.am/blog/posts/why-is-the-gmail-app-700-mb

### TL;DR
The post observes that Gmail for iOS has grown from ~12 MB in 2013–2016 to about 760 MB today, vastly larger than Apple’s Mail and many competitors. A comparison table shows most Apple stock apps are tiny “shells” around OS frameworks, while Google and Microsoft apps routinely occupy hundreds of megabytes. The article doesn’t explain why; HN comments attribute it to shared cross‑platform code, bundled runtimes, Meet/Chat integration, localization assets, and weak incentives to optimize for storage, especially on iOS.

---

### Comment pulse
- Historical shift → Mobile apps went from kilobytes–single-digit megabytes to hundreds, even for simple utilities; frameworks and assets now dominate binaries.

- System vs. third‑party apps → Apple’s built‑ins are thin UIs atop large private system frameworks, so direct size comparison with full third‑party bundles is misleading.

- Cross‑platform “super app” design → Google ships big shared C++ stacks, protobufs, gRPC/QUIC, Meet/Chat features in one bundle; modularization and size discipline seem deprioritized.

---

### LLM perspective
- View: App size has become an unpriced externality; neither app vendors nor platforms feel strong pressure to minimize it.

- Impact: Users with low-capacity devices, limited data, or many required enterprise apps bear the cost in storage, bandwidth, and performance.

- Watch next: Store-level size budgets, better modular download tooling, and public “app weight” rankings could reintroduce pressure to slim down.
