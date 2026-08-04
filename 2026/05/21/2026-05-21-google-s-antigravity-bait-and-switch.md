# Google's Antigravity bait and switch

- Score: 502 | [HN](https://news.ycombinator.com/item?id=48222529) | Link: https://www.0xsid.com/blog/antigravity-bait-n-switch

### TL;DR

Google silently auto-updated the existing Antigravity IDE into a standalone chat-style agent, replacing a daily production workflow without consent. The legacy installer remained available, but version 2.0 rewrote application paths, prevented coexistence, and kept hijacking launches until the author purged all Antigravity files; that recovery restored the IDE but erased settings and chat history. HN users reported similar confusion, Windows/WSL limitations, and recovery tooling. Discussion blamed Google’s fragmented portfolio management and weak migration discipline, while some suggested simply pairing VS Code with the separate agent.

### Comment pulse

- A community Python tool claims to merge VS Code settings and SQLite/protobuf data, restoring the history sidebar after shutting down background processes.
- Windows users cited missing WSL integration, repeated CLI authentication, and a 4 GB server directory after four sessions.
- Strategy debate centered on market expansion versus user respect — counterpoint: some saw the original editor as replaceable because it was a VS Code reskin.

### LLM perspective

- View: Automatic updates should preserve product identity; replacing an application class requires explicit consent, compatibility, and rollback.
- Impact: Developers lose work time and trust when product strategy reaches machines before migration tooling or support.
- Watch next: Google should publish coexistence paths, history migration, WSL support, auto-update controls, and a deprecation timeline.
