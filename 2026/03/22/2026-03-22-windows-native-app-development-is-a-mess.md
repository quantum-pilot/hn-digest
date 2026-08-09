# Windows native app development is a mess

- Score: 309 | [HN](https://news.ycombinator.com/item?id=47475938) | Link: https://domenic.me/windows-native-dev/

### TL;DR

A developer building Display Blackout found Microsoft’s current native-app path deeply fragmented. WinUI 3 and the Windows App SDK still require frequent P/Invoke calls to mature Win32 APIs for display events, global hotkeys, nonactivating windows, tray icons, and sizing. C# distribution adds another dilemma: depend on a runtime Windows does not ship, or bundle ahead-of-time output that makes a tiny utility about 9MB. MSIX sideloading and code signing are costly or awkward, while Store review rejected the app as insufficiently distinctive.

### Comment pulse

- Many veterans recommend Win32, MFC, WPF, or WinForms because decades-old applications still compile and run across Windows releases.
- Others favor Qt or Avalonia — counterpoint: even stable Win32 brings C++ safety, DPI, theming, string, and 64-bit migration pain.
- WinUI 3 drew unusually broad warnings from developers who had tried it.

### LLM perspective

- **View:** Microsoft preserved compatibility better than it created a coherent modern desktop platform.
- **Impact:** Small developers are pushed toward cross-platform or web-derived stacks even when building Windows-only utilities.
- **Watch next:** Whether Microsoft’s own flagship applications converge on one native toolkit and signal a durable investment path.
