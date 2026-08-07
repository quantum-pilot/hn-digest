# On non-rooted Android 17, ADB uninstall of system apps fails

- Score: 216 | [HN](https://news.ycombinator.com/item?id=49193173) | Link: https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation/issues/1426

### TL;DR

An Android debloater project proposes making “Disable” the default because Android 17 blocks ADB uninstallation of system apps on non-rooted devices. Disabling is reversible and may stop background execution more safely, but can preserve storage use and app visibility, interact differently with updates, and has received less package-by-package testing than uninstalling. HN treated the change as another reduction in device-owner control. Suggested alternatives—GrapheneOS, LineageOS, or GNU/Linux phones—remain constrained by supported hardware, battery optimization, app compatibility, Play Integrity, banking software, and OEM behavior that can re-enable packages.

### Comment pulse

- Custom ROMs remove bloat — counterpoint: they do not make arbitrary phones OS-installable, and GrapheneOS device availability remains narrow.
- Mobile GNU/Linux faces missing drivers, poor power management, weak GPU support, and apps that reject uncertified firmware or emulation.
- Some equated root with ownership; others argued appliances can be owned without exposing a decades-old computer administration model.

### LLM perspective

- View: Disabling is the safer fallback for a constrained tool, but it does not resolve who ultimately controls system software.
- Impact: Debloater maintainers must retest package behavior; stock-ROM users lose a storage, privacy, and persistence option.
- Watch next: Verify Android 17 behavior, background execution after disabling, OEM re-enablement, storage recovery, per-package defaults, and custom-ROM availability.
