# Problems with D-Bus on the Linux desktop

- Score: 258 | [HN](https://news.ycombinator.com/item?id=46278857) | Link: https://blog.vaxry.net/articles/2025-dbusSucks

### TL;DR

Hyprland developer Vaxry argues that D-Bus offers useful service discovery but weak protocol discipline: scattered specifications, permissive variants, confusing portal layers, and security delegated to each service. He is building hyprwire and the unfinished hyprtavern bus around enforced types, built-in permissions, discoverable protocol objects, and a per-application encrypted key-value store. Parallel buses and translation proxies could enable gradual migration. An addendum concedes his portal example used the wrong documentation, but maintains that D-Bus should reject invalid messages structurally rather than relying on conventions.

### Comment pulse

- Critics said another bus increases fragmentation — counterpoint: sandboxed desktops need stronger defaults than trusting every same-user process.
- Readers suggested reusing Android’s Binder, whose deployment and engineering base exceed a new Hyprland-specific protocol.
- Hyprtavern currently lacks mature documentation, specifications, language bindings, and tests, weakening claims that it already surpasses D-Bus.

### LLM perspective

- View: The critique identifies real ergonomics and trust-boundary tensions, but the replacement remains a proposal with limited evidence.
- Impact: Hyprland applications may gain tighter IPC contracts while Linux developers inherit another compatibility surface.
- Watch next: Threat model, protocol documentation, audits, benchmarks, Binder comparison, proxy reliability, and adoption beyond Hyprland.
