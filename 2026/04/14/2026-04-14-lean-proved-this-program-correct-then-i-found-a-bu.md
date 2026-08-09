# Lean proved this program correct; then I found a bug

- Score: 376 | [HN](https://news.ycombinator.com/item?id=47759709) | Link: https://kirancodes.me/posts/log-who-watches-the-watchers.html

### TL;DR

A Claude-guided fuzzing campaign ran 105.8 million executions against lean-zip, finding no memory-safety failures in its verified compression/decompression code. It did uncover a heap overflow in Lean 4’s C++ runtime, triggered when scalar-array allocation arithmetic wraps near `SIZE_MAX`, plus an out-of-memory denial of service in lean-zip’s unverified ZIP parser. Both sat outside the proven boundary. The result supports formal verification’s value while showing that specifications, unverified I/O code, runtimes, compilers, and hardware remain part of the deployed system’s trust envelope.

### Comment pulse

- Many called the title misleading because no verified code failed. — counterpoint: users experience the whole binary, not an abstract proof boundary.
- Practitioners say proofs still sharply localize faults, but incomplete or incorrect specifications can certify behavior humans never intended.
- One proposal makes proof assumptions machine-checkable runtime guards, exposing when deployment leaves the verified operating envelope.

### LLM perspective

- **View:** Verification reduces uncertainty; it does not eliminate trust dependencies.
- **Impact:** Security claims should enumerate proved modules, excluded paths, resource bounds, and runtime assumptions.
- **Watch next:** Land the runtime fix, validate archive sizes, and fuzz other Lean allocation APIs.
