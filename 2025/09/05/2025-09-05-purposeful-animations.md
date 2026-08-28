# Purposeful animations

- Score: 542 | [HN](https://news.ycombinator.com/item?id=45139088) | Link: https://emilkowal.ski/ui/you-dont-need-animations

### TL;DR

Interface animation should explain a change, confirm input, preserve spatial continuity, or occasionally add delight—not exist as decoration. Frequency matters: effects that feel pleasant once can become friction when repeated hundreds of times, and keyboard-driven actions should respond immediately. The author recommends fast UI motion, generally under 300 milliseconds, plus context-aware behavior such as delaying only the first tooltip. Commenters push the rule further: animate mainly when users might otherwise miss a state transition, and ensure interaction never waits for visual polish to finish.

### Comment pulse

- Readers criticize Apple animations that block input, stack sequentially, or preserve the wrong setting when users act before motion ends.
- Several prefer nearly imperceptible 150–200 millisecond transitions, while warning that overly brief motion can resemble a rendering glitch.

### LLM perspective

- View: Animation earns its latency budget only when it conveys state, causality, or navigation better than an immediate change.
- Impact: Nonblocking, interruptible motion can improve comprehension; ornamental motion compounds into measurable friction for expert and frequent users.
- Watch next: Reduced-motion support, input interruption, keyboard paths, repeated-use testing, dropped frames, and task-completion time.
