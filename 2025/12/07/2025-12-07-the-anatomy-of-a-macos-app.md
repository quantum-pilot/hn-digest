# The Anatomy of a macOS App

- Score: 171 | [HN](https://news.ycombinator.com/item?id=46181268) | Link: https://eclecticlight.co/2025/12/04/the-anatomy-of-a-macos-app/

### TL;DR

macOS applications evolved from Classic Mac resource forks into NeXT-style .app directory bundles. A modern bundle places executables, resources, frameworks, metadata, signatures, receipts, helpers, and extensions under Contents; Info.plist tells LaunchServices and RunningBoard how to start and integrate it. Universal apps keep Intel and Arm code in fat Mach-O binaries rather than changing directory structure. Commenters clarified that notarization may be technically optional but distribution friction makes it practically important, while noting custom layouts can work if paths and signing remain valid.

### Comment pulse

- Notarization’s burden divides developers → it reduces scary launch failures — counterpoint: fees, identity checks, and opaque company verification impede independent distribution.
- Standard directories favor predictability → unconventional library folders can pass notarization, but commenters found no practical benefit.
- Historical nuance matters → PowerPC Classic applications stored executable code in data forks, unlike older 68K CODE resources.

### LLM perspective

- View: The bundle is both packaging convention and security boundary, making metadata integrity operationally significant.
- Impact: Developers gain simple installation and removal, but release engineering inherits signing, receipt, and notarization obligations.
- Watch next: Gatekeeper policy changes, notarization evidence, universal-binary signing behavior, and extension-directory rules.
