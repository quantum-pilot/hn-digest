# Show HN: Davit, a Apple Containers UI

- Score: 159 | [HN](https://news.ycombinator.com/item?id=48821848) | Link: https://davit.app

### TL;DR

Davit is a free, MIT-licensed SwiftUI dashboard for Apple’s container platform on Apple-silicon Macs running macOS 15 or later. It talks to Apple’s daemon directly over XPC, without Docker Desktop, Electron, web views, or its own agents. The 17 MB app can install the runtime, manage containers, images, volumes, networks and registries, stream logs and stats, open terminals, browse files, import Compose projects, and build Dockerfiles. HN testers reported smooth first-run setup and praised its native feel, while noting OrbStack’s established Docker compatibility and the project’s conspicuous AI-assisted development.

### Comment pulse

- Native integration impressed early users → runtime installation and an nginx test worked immediately, with no Electron layer or Docker Desktop dependency.
- OrbStack remains the comparison point → its speed, integration, and Docker-command compatibility are proven — counterpoint: Davit is free and Apple-native.
- Visible AI authorship drew scrutiny → every early commit credited Claude; commenters treated that as both an obvious stylistic tell and a quality signal.

### LLM perspective

- **View:** Davit makes Apple’s emerging container stack approachable while preserving native architecture and a small operational footprint.
- **Impact:** Direct XPC integration could accelerate adoption among Mac developers who want graphical management without Docker Desktop’s bundled stack.
- **Watch next:** Compose compatibility, resource overhead, networking ergonomics, release stability, and whether mature competitors add Apple-container backends.
