# Problems with D-Bus on the Linux desktop

- Score: 258 | [HN](https://news.ycombinator.com/item?id=46278857) | Link: https://blog.vaxry.net/articles/2025-dbusSucks

### TL;DR

The Hyprland developer argues D-Bus permits loosely typed, poorly documented, vendor-specific interfaces and exposes an overly permissive session bus, making interoperability and sandboxing fragile. After encountering conflicting portal conventions, he began hyprwire, a strict typed transport, and hyprtavern, a permission-aware discoverable bus with per-application secret storage. Both are early work; documentation, bindings, and protocols remain incomplete. Commenters share some D-Bus frustrations but question fragmentation, the security model, absent tests, and why established alternatives such as Binder were not reused.

### Comment pulse

- Strict schemas and permissions could improve sandboxed desktop IPC → D-Bus flexibility often shifts validation into every application.
- Critics prefer repairing or wrapping deployed infrastructure → another bus creates migration and ecosystem costs.
- The secret-store threat model is disputed: sandboxing blocks broad access, while unsandboxed processes may bypass bus-level protections.

### LLM perspective

- View: Hyprtavern identifies real contract problems, but its replacement case depends on proving interoperability and operational maturity.
- Impact: Parallel buses let Hyprland experiment gradually while transferring compatibility work to proxies and application maintainers.
- Watch next: Published wire specifications, threat models, conformance tests, language bindings, portal proxies, and measurable performance.
