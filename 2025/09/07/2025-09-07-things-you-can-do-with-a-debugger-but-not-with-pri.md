# Things you can do with a debugger but not with print debugging

- Score: 249 | [HN](https://news.ycombinator.com/item?id=45156414) | Link: https://mahesh-hegde.github.io/posts/what_debugger_can/

### TL;DR

The article argues that debuggers offer capabilities print statements cannot easily match: inspecting the complete call stack, evaluating or mutating expressions in paused frames, stopping where exceptions are thrown, changing execution without source edits, and sharing checked-in launch configurations. It acknowledges that debugger setup, especially remotely, often pushes developers toward logging. Commenters defend print’s universality across languages and environments, while adding hardware watchpoints, conditional breakpoints, and reverse execution to the debugger case. They also warn that optimized builds, unreliable tooling, or slow conditions can make debugger observations misleading.

### Comment pulse

- Print advocates value portability and low setup; debugger advocates value state inspection and precise execution control.
- Several commenters treat REPLs, logging, and debuggers as complementary rather than mutually exclusive tools.

### LLM perspective

- View: The practical divide is not power but setup cost, observability needs, and trust in the debugging environment.
- Impact: Shared debugger configurations can turn advanced inspection from individual expertise into routine team infrastructure.
- Watch next: Better remote and optimized-build support that preserves debugger advantages without fragile setup.
