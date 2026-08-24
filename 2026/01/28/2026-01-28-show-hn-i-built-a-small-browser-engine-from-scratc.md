# Show HN: I built a small browser engine from scratch in C++

- Score: 118 | [HN](https://news.ycombinator.com/item?id=46795540) | Link: https://github.com/beginner-jhj/mini_browser

### TL;DR

A Korean high-school senior spent eight weeks building an educational browser engine while learning C++. The Qt-based project tokenizes HTML, constructs a DOM, parses and cascades CSS, computes block and inline layouts, paints text and images, and supports links, navigation history, asynchronous image loading, and caching. Its deliberately limited engine delegates networking and graphics primitives to Qt and lacks much web-platform complexity. The author emphasizes systematic debugging, careful review of AI-assisted rendering code, pragmatic scope, and understanding each borrowed idea rather than producing a production browser.

### Comment pulse

- Readers praised the learning achieved, especially using AI and tutorials while debugging and explaining the resulting code independently.
- Commenters stressed HTML, layout, and networking are far deeper than this toy — counterpoint: its explicit goal was education, not standards completeness.
- Suggested next steps included a simple HTTP server or contributing to Dillo; one warning advised testing against independent protocol implementations.

### LLM perspective

- View: The strongest deliverable is a concrete mental model of browser stages, not standards coverage.
- Impact: A bounded reimplementation can teach parsing, state, layout, asynchronous I/O, testing, and debugging in one cohesive system.
- Watch next: Malformed-HTML tests, independent servers, richer layout cases, accessibility, and whether the author contributes to an established browser.
