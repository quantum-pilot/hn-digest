# Zed is our office

- Score: 437 | [HN](https://news.ycombinator.com/item?id=45916196) | Link: https://zed.dev/blog/zed-is-our-office

- TL;DR
  - Zed pitches its editor as a virtual office: built-in voice, screen share, and CRDT-backed real‑time editing organized in hierarchical “channels” for meetings, projects, and personal focus. No extensions; GitHub auth, follow-cursor, permissions; collaboration is alpha and free. Vision: keep conversations, edits, and AI agents linked to code. HN likes the ambition but flags basic-editor instability, container/AI friction, rendering quirks, and unclear self-hosting/SLA for enterprises; some dislike comms in IDEs. Others welcome occasional high‑quality pairing vs worse third‑party tools.

- Comment pulse
  - Stability first → file change/diff bugs, containerized dev breaks AI; reverting to Neovim; revisit at 1.0 (Spring 2026). — counterpoint: works well out‑of‑box for Rust.
  - Enterprise concern → need self‑hosting and SLA; unclear in docs, though community says on‑prem is possible.
  - Philosophy → reject comms/multiplayer in IDE; prefer solitude. Some value Zed’s pairing for rare incidents; panel can be hidden.

- LLM perspective
  - View: They’re productizing their internal workflow; success hinges on rock-solid core editing and reliability before collaboration sticks.
  - Impact: Best for teams pairing/mobbing; solo or small polyglot shops may see cognitive overhead without clear ROI.
  - Watch next: Latency/scale benchmarks vs Live Share, container support status, on‑prem collab docs, fixes for file watching, wrap toggle, sharpness.
