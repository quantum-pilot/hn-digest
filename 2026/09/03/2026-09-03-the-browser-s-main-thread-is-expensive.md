# The browser's main thread is expensive

- Score: 408 | [HN](https://news.ycombinator.com/item?id=49522137) | Link: https://kciter.so/posts/the-expensive-main-thread/en/

### TL;DR

The article frames frontend responsiveness as careful allocation of the browser’s main thread, where JavaScript, events, style, layout, and paint compete. It recommends splitting long work to create rendering gaps, batching repeated work, prioritizing user-visible tasks, and deferring unnecessary activity. When possible, work should leave the main thread through compositor-friendly animation or workers. The examples emphasize that yielding can improve perceived responsiveness without reducing total work, while atomic operations, transfer overhead, browser support, and excessive task splitting impose practical limits.

### Comment pulse

- Commenters praised the explanation but argued oversized bundles and hydration cause more everyday slowness than advanced interaction workloads.
- Discussion emphasized consistent frame pacing over blindly matching every display’s maximum refresh rate.
- Practitioners shared experiences with yielding, workers, transferable buffers, and OffscreenCanvas, noting that data movement can erase gains.

### LLM perspective

- View: Responsiveness is a scheduling problem before it is an algorithmic-speed problem.
- Impact: Small architectural choices determine whether rendering and input receive timely access to a shared resource.
- Watch next: Measure long tasks and frame pacing before choosing yielding, batching, compositor work, or workers.
