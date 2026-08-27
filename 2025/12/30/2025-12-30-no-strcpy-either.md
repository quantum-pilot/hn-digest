# No strcpy either

- Score: 175 | [HN](https://news.ycombinator.com/item?id=46433029) | Link: https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/

### TL;DR

curl has eliminated `strcpy` after previously removing `strncpy`, replacing both with a helper that receives destination size and source length, copies only when the full string plus terminator fits, and keeps validation adjacent to the write. Daniel Stenberg argues this prevents checks drifting away during decades of maintenance and removes a magnet for bogus AI vulnerability reports. HN largely supports explicit lengths but questions the helper’s silent failure behavior and debates whether C’s null-terminated strings are the deeper flaw.

### Comment pulse

- Explicit lengths improve safety and speed → `memcpy` avoids null-byte scanning and input-dependent branching.
- The helper should report failure → clearing the destination silently can hide release-build errors after assertions disappear.
- C string APIs reflect old constraints → `strncpy` served fixed-width fields, not safe bounded string copying.

### LLM perspective

- View: A narrow wrapper converts dispersed conventions into one enforceable local invariant.
- Impact: curl maintainers trade call-site brevity for safer long-term refactoring and clearer static analysis.
- Watch next: Whether silent failure causes bugs, and whether the helper evolves to return status.
