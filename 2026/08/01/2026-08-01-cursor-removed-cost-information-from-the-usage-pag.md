# Cursor removed cost information from the usage page and CSV export

- Score: 294 | [HN](https://news.ycombinator.com/item?id=49135257) | Link: https://forum.cursor.com/t/usage-page-to-token-amount-what/167153

### TL;DR
Cursor users noticed that dollar cost info disappeared from the usage page and CSV export, sparking concerns about pricing transparency and cost control. A Cursor employee says the CSV breakage was a bug and the cost graph was intentionally removed because it misrepresented included plan credits as real spend. Many commenters argue this still makes it harder to monitor and limit expensive model usage, pushing some back to VS Code plus Claude/Codex workflows, where costs and behavior feel more controllable.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Token usage varies wildly by agent harness → prompts, injected tools, and “memory” can multiply context size and cost—counterpoint: sometimes extra context is genuinely needed for correctness.  
- Cursor’s removal of in-IDE cost indicators → users feel nudged toward overspending and forced to rely on admins or separate dashboards to track burn.  
- Cursor’s value questioned → IDE integration and multi-model support are nice, but pricing, UX regressions, and easy migration back to VS Code weaken stickiness.

---

### LLM perspective
- View: IDE vendors must expose per-session/token costs clearly or advanced users will defect to raw APIs and lighter tools.  
- Impact: Teams managing model bills, especially on shared org plans, lose fine-grained visibility and control inside the editor.  
- Watch next: Expect third-party “LLM metering” tools, and IDEs competing on transparent, per-request cost overlays and harness efficiency benchmarks.
