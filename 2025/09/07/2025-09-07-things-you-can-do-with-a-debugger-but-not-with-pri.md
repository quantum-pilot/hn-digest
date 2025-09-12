# Things you can do with a debugger but not with print debugging

- Score: 249 | [HN](https://news.ycombinator.com/item?id=45156414) | Link: https://mahesh-hegde.github.io/posts/what_debugger_can/

- TL;DR
    - The article argues debuggers unlock capabilities print/logs can’t: full call-stack inspection, on-the-fly expression evaluation and state edits, exception breakpoints at throw sites, changing execution without code edits, and team-wide checked-in debug configs. HN agrees debuggers are powerful but notes print is universal across languages and remote contexts. Commenters add hardware/watchpoint and time-travel debugging as killer features, complain conditional breakpoints can be slow/unreliable, warn debuggers sometimes misreport state, and propose REPLs as a flexible complement that can hand off to a GUI debugger.

- Comment pulse
    - Print is universal across polyglot/remote systems → teams seldom master debuggers everywhere — counterpoint: watchpoints/stack inspection catch bugs logs can’t.
    - Hardware/watchpoints, invariant watches, and time-travel → pinpoint memory corruption fast; scripts at breakpoints encode cross-team knowledge.
    - Conditional breakpoints and some IDE debuggers can be slow/misleading → fall back to print+breakpoint, int3/Debugger.Break, or a REPL.

- LLM perspective
    - View: Pair standardized debug configs with selective debugger features; keep REPLs for remote/polyglot gaps.
    - Impact: Faster root-cause analysis; safer experiments without code edits; smoother onboarding via shared launch configs.
    - Watch next: Wider time-travel availability, faster conditional breakpoints, first-class cloud/Kubernetes live-debug tooling.
