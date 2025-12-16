# Problems with D-Bus on the Linux desktop

- Score: 258 | [HN](https://news.ycombinator.com/item?id=46278857) | Link: https://blog.vaxry.net/articles/2025-dbusSucks

### TL;DR
Author (Hyprland maintainer) argues D‑Bus’s concept—shared IPC bus—is sound but its design is fatally flawed: weak typing, hand‑wavy, scattered specs, and almost no built‑in permissions, leading to fragile integrations and insecure “secret” storage. They’re building a replacement stack: hyprwire (strictly typed Wayland‑style wire protocol) plus hyprtavern, a new bus with mandatory per‑app permissions and a secure, non‑enumerable key‑value secret store as a core spec. HN debates whether this is overdue hardening or yet another fragmenting wheel reinvention.

---

### Comment pulse
- Many fear another IPC standard fragments Linux; they argue D‑Bus could be fixed with specs and threat models — counterpoint: sandboxing needs stricter, default‑secure primitives.  
- Some suggest basing a new bus on Android’s Binder, citing billions of devices and a Rust kernel implementation, but note limited non‑Android user‑space support.  
- Others share D‑Bus pain points and ridicule GNOME’s secret‑service stance, highlighting desktop crashes and DoS bugs from browser‑driven D‑Bus floods as a ripe research area.

---

### LLM perspective
- D‑Bus replacement can succeed only if it coexists and offers drop‑in wins for 2–3 flagship apps and DEs.  
- Hardening desktop IPC benefits sandboxed user apps and password managers; system‑wide security still depends on kernel isolation and filesystem policies.  
- Watch for formal specs, language bindings, and D‑Bus proxy shims; adoption will be measurable via Flatpak portals and DE integrations.
