# macOS needs its grid back

- Score: 380 | [HN](https://news.ycombinator.com/item?id=48364800) | Link: https://blog.hopefullyuseful.com/blog/macos-needs-its-grid-back/

### TL;DR

Leopard’s original Spaces let users arrange virtual desktops in a grid, enabling stable spatial memory; Lion replaced it with today’s horizontal strip. After seeing animation-free space switching, the author built GridLion, a native wrapper that maps macOS’s linear spaces onto configurable per-display grids with hotkeys and optional previews. The app relies on private APIs and broad Accessibility and screen-recording permissions, so it cannot enter the App Store. HN strongly related to the regression, but split over whether Apple’s permission friction is disrespectful or justified protection against keylogging and surveillance.

### Comment pulse

- Permissions are too coarse → global hotkeys should expose commands without keylogging, while space thumbnails should not require unrestricted screen capture.
- Workspaces should model projects → browsers, editors, terminals, chats, and agents need OS-level grouping and restoration across applications.
- Grid versus strip reflects different cognition → fixed 2D locations build spatial memory — counterpoint: linear gestural navigation remains valid for some users.

### LLM perspective

- **View:** The missing platform primitive is secure, documented workspace control, not another third-party window manager.
- **Impact:** Private APIs force useful accessibility tools into fragile distribution, alarming permissions, and recurring compatibility risk.
- **Watch next:** Apple workspace APIs, granular capture permissions, stable ordering, cross-display moves, and project-level restoration.
