# Windows native app development is a mess

- Score: 309 | [HN](https://news.ycombinator.com/item?id=47475938) | Link: https://domenic.me/windows-native-dev/

## TL;DR

The author tried to build a tiny Windows utility (black out side monitors while gaming) using Microsoft’s “modern” stack (WinUI 3 + Windows App SDK) and found the ecosystem fragmented and underpowered. Even basic tasks—tray icon, global hotkey, monitor change events—required dropping to old Win32 APIs via fragile interop layers. Packaging is painful (expensive code signing, terrible unsigned MSIX sideloading, store rejection), and .NET distribution is stuck on 4.8.1, forcing bloated AOT binaries. Many commenters conclude: stick with Win32/WPF or use web/Electron-like stacks instead.

---

## Comment pulse

- Use plain Win32 → Tiny, fast, stable; app fits in kilobytes and still runs across decades. — counterpoint: C++’s memory unsafety remains a serious 2026 tradeoff.  
- Avoid WinUI 3/WinAppSDK → Immature, incomplete, and frequently abandoned; WPF/WinForms, Qt, Avalonia, Uno, Delphi, etc. are more reliable and controllable.  
- Win32 as foundation → Learn it, then layer your own thin wrapper; gives full control, long-term compatibility, and escape hatches when higher-level toolkits fail.

---

## LLM perspective

- View: For small utilities, “stable and old” (Win32/WPF) often beats Microsoft’s constantly-reset “modern” UI stacks.  
- Impact: Solo devs and small teams will keep drifting to Electron/Tauri or third-party UI frameworks, not WinUI 3.  
- Watch next: Whether Microsoft ships current .NET via Windows Update, meaningfully funds WinUI 3, or open-sources WPF/WinUI enough for the community to take over.
