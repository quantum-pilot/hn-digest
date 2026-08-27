# The Anatomy of a macOS App

- Score: 171 | [HN](https://news.ycombinator.com/item?id=46181268) | Link: https://eclecticlight.co/2025/12/04/the-anatomy-of-a-macos-app/

### TL;DR

macOS applications are directory bundles rather than single executables. Inside `Contents`, `MacOS` holds executable code, `Resources` carries icons and interface assets, and `Info.plist` declares launch, version, document, and compatibility metadata. Modern bundles may also contain frameworks, XPC services, extensions, login items, code signatures, App Store receipts, and notarization tickets. This self-contained structure simplifies installation and removal while protecting components through signing. Universal applications retain the same layout, with Intel and Arm code combined inside fat Mach-O binaries.

### Comment pulse

- Developers debated notarization’s security value, annual fee, identity checks, and increasingly inconvenient bypass process.
- Readers clarified that a notarized app can omit a stapled ticket, though online verification may then be required.
- Others noted nonstandard subdirectories can work with correct runtime paths, despite offering little practical advantage.

### LLM perspective

- View: The bundle is both packaging convention and the integrity boundary for modern macOS software.
- Impact: Developers must understand metadata, signatures, and embedded helpers because launch behavior depends on all three.
- Watch next: Inspect a real app bundle and compare signed, notarized, App Store, and universal variants.
