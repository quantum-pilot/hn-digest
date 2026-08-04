# DOS Game "F-15 Strike Eagle II" reversing project needs DOS test pilots

- Score: 187 | [HN](https://news.ycombinator.com/item?id=48609766) | Link: https://neuviemeporte.github.io/f15-se2/2026/06/20/needyou.html

### TL;DR

A hobby project reverse-engineering 1989’s F-15 Strike Eagle II has reconstructed C for all three DOS executables, moved their data into C, replaced most assembly-only routines, and assigned meaningful names. Release v0.9.1 seeks testers with game version 451.03 and the Desert Storm expansion; it skips setup and assumes VGA without sound or joystick. Reports must distinguish reconstruction defects from original quirks because initial fidelity is bug-for-bug. HN celebrated the preservation effort and debated emulation versus source reconstruction.

### Comment pulse

- Source reconstruction unlocks more than compatibility → C permits instrumentation, deep feature changes, higher-resolution assets, new missions, and ports that binary patching makes impractical.
- Testing needs historical baselines → disappearing 3D objects and inverted fuel-starved flight are authentic bugs, so reports must reproduce against original executables.
- Motivation extends beyond playability → nostalgia, archival study, and modification drive reverse engineering despite DOSBox — counterpoint: commenters raised copyright and trademark uncertainty.

### LLM perspective

- **View:** Binary equality protects provenance during translation, while behavioral testing catches data-layout errors opcode comparison cannot reveal.
- **Impact:** Veteran players can supply undocumented behavioral oracles that automated opcode matching and younger contributors cannot reconstruct from binaries alone.
- **Watch next:** Expand the regression matrix across missions, briefings, debriefings, DOS environments, timing, input devices, modes, and original-versus-reconstructed save compatibility.
