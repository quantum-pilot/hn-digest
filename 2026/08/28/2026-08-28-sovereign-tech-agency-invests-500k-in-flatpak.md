# Sovereign Tech Agency invests €500k in Flatpak

- Score: 255 | [HN](https://news.ycombinator.com/item?id=49474786) | Link: https://modal.cx/blog/announcing-flatpak-sta/

### TL;DR

Germany’s Sovereign Tech Agency is investing €508,640 over two years to strengthen Flatpak’s sandboxing, infrastructure, and stewardship. Planned work includes finer audio and network permissions, VPN and writing-assistance portals, password-autofill research, entitlements, intents, tests, and permission-dialog improvements. The project also aims to expand scarce maintainer expertise through contractors and formal structures. Commenters welcome the funding but question temporary grants, backward compatibility for new permissions, storage overhead, and whether Flatpak’s defaults deliver understandable isolation in practice.

### Comment pulse

- Granularity needs compatibility → new permissions remain unusable on Flathub when older supported runtimes cannot interpret them safely.
- Grants accelerate gaps → critics want permanent public funding, while others favor project grants followed by adopter-funded support contracts.
- Sandboxing remains confusing → portals can limit access, but legacy app behavior often requires broad filesystem or device permissions.

### LLM perspective

- View: The investment targets Flatpak’s hardest layer: permission plumbing that applications, stores, and old runtimes must coordinate.
- Impact: Better portals could make image-based Linux desktops safer without forcing applications to sacrifice common capabilities.
- Watch next: Compatibility designs and measurable adoption of audio, network, and VPN permissions will determine practical value.
