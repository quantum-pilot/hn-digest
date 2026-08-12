# I fixed Windows native development

- Score: 633 | [HN](https://news.ycombinator.com/item?id=47022891) | Link: https://marler8997.github.io/blog/fixed-windows/

### TL;DR

Jonathan Marler’s `msvcup` replaces the usual Visual Studio installation path with a small command-line tool that downloads only Microsoft’s native compiler, linker, headers, libraries, and Windows SDK from official manifests and CDNs. It supports side-by-side versions, repeatable installs, target cross-compilation, lock files, wrapper executables, and CMake integration without globally mutating the environment. The project already serves Windows CI for Tuple’s WebRTC work, but deliberately omits the IDE and raises a bootstrap question: users initially obtain the installer executable from GitHub.

### Comment pulse

- Developers welcomed a smaller, scriptable toolchain, especially for CI and projects that need several compiler or target versions.
- Others noted Visual Studio supports unattended or LTSC installs, though commenters disputed whether those options solve size and opacity.
- The main security concern was trusting a downloaded bootstrap binary — counterpoint: the source is inspectable and subsequent payloads come from Microsoft.

### LLM perspective

- **View:** Separating compiler provisioning from IDE installation turns Windows toolchains into explicit build inputs rather than workstation state.
- **Impact:** Open-source projects can reduce contributor support burden by pinning identical SDK payloads across local and CI environments.
- **Watch next:** Signed releases, bootstrap hashes, component-coverage growth, and resilience when Microsoft changes manifests or CDN packages.
