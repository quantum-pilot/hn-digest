# DXGI debugging: Microsoft put me on a list

- Score: 190 | [HN](https://news.ycombinator.com/item?id=45323207) | Link: https://slugcat.systems/post/25-09-21-dxgi-debugging-microsoft-put-me-on-a-list/

- TL;DR
  - Porting Space Station 14 to Windows ARM64 revealed crashes in USER32!GetDC when using ANGLE. Root cause: DXGI installs a runtime detour for “Optimizations for windowed games” (forces flip-model swapchains). That detour breaks on ARM64 with pointer authentication, producing illegal instructions. It only triggers when the binary matches Microsoft’s allowlist (SS14.Loader.exe). Disabling the optimization avoids crashes; the dev is pausing ARM64 support and pursuing alternatives (Mesa’s OpenGL-on-D3D12 or ditching OpenGL). HN highlights broader detour use, similar ARM64 crashes, and common per-executable shims.

- Comment pulse
  - DXGI detours patch OS calls → Detours don’t handle ARM64 PAC prologues, causing illegal instructions; AutoSR also crashes similarly.
  - Filename-based behavior is normal → Windows and drivers ship per-executable shims; IFEO and game-specific profiles exist—counterpoint: It’s brittle and opaque for developers.
  - Not just Windows pain → Cross-OS graphics stacks have similar quirks; most devs won’t hit them unless mixing architectures, APIs, and emulation.

- LLM perspective
  - View: Short-term mitigations: disable the optimization per app, avoid listed filenames, or use true flip-model swapchains.
  - Impact: ARM64 gaming on Windows risks trust erosion if OS-level shims silently break native apps using OpenGL-on-D3D or ANGLE.
  - Watch next: Fixes to track: DXGI detours PAC-safe, ARM64 gating off, ANGLE flip-model swapchains, Mesa D3D12 OpenGL artifact patches shipping via Store.
