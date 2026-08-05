# Rust project goals: Immobile types and guaranteed destructors

- Score: 241 | [HN](https://news.ycombinator.com/item?id=49152023) | Link: https://github.com/rust-lang/rust-project-goals/blob/main/src/2026/move-trait.md

### TL;DR

An accepted 2026–2027 Rust project goal will explore explicit Move, Destruct, and Forget capabilities so types can opt out of relocation or guaranteed omission of cleanup. A !Move type would keep a stable address without making immobility a property of Pin-wrapped places; !Forget could guarantee a scoped task handle’s destructor joins borrowed async work. Compiler prototypes, RFCs, and Linux-kernel testing are planned, but Future migration is out of scope. HN welcomed the direction while stressing this is research, not an accepted language change, and may conflict with separate pin-ergonomics work.

### Comment pulse

- Status matters → acceptance authorizes exploration, not syntax or stabilization; the design can change substantially or be abandoned.
- Type-level immobility could replace Pin complexity → supporters see a long-standing hole, while ecosystem migration remains unresolved.
- Guaranteed consumption enables safer APIs → transactions and scoped tasks could require explicit completion across every control-flow exit.

### LLM perspective

- View: The proposal trades universal simplicity for stronger static guarantees around address stability and cleanup.
- Impact: Kernel, async, and resource APIs could become safer, but generic code must express capability bounds.
- Watch next: RFC trait hierarchy, in-place construction, Pin interoperability, collection behavior, and Linux validation.
