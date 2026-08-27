# DXGI debugging: Microsoft put me on a list

- Score: 190 | [HN](https://news.ycombinator.com/item?id=45323207) | Link: https://slugcat.systems/post/25-09-21-dxgi-debugging-microsoft-put-me-on-a-list/

### TL;DR

While porting Space Station 14 to Windows ARM64, the author traced an illegal instruction in `GetDC` to DXGI installing a runtime detour for “Optimizations for windowed games.” The optimization activated only when the executable was named `SS14.Loader.exe`, apparently because Microsoft maintains a game-specific compatibility list. Disabling the feature stopped the crash; a minimal program under another name did not reproduce it. Commenters explained that program-specific compatibility rules are common, but said DXGI’s detour cannot handle current ARM64 pointer-authenticated function prologues.

### Comment pulse

- DXGI patches API calls to retrofit graphics features → this flexibility inherits user-space hooking fragility.
- Filename-based compatibility surprised readers → defenders noted Windows, drivers, Mesa, and Proton all carry application-specific behavior.
- Cross-architecture debugging obscured the cause → x64 launchers confused WinDbg before the native ARM64 failure was isolated.

### LLM perspective

- View: Compatibility databases are pragmatic infrastructure, but opaque activation makes rare architecture failures exceptionally expensive to diagnose.
- Impact: Native ARM64 game ports can inherit optimizations designed and tested around x64 executables.
- Watch next: Track Microsoft’s detour fix, list-gating rules, Mesa bug resolution, and eventual SS14 ARM64 release.
