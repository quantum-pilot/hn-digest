# Let's compile Quake like it's 1997

- Score: 198 | [HN](https://news.ycombinator.com/item?id=48318522) | Link: https://fabiensanglard.net/compile_like_1997/

### TL;DR

Fabien Sanglard recreates a late-1990s Windows build of Quake using Windows NT 4, Visual C++ 6, and id’s archived source. Opening WinQuake.dsw works only when its legacy workspace files survive transfer intact. The first rebuild fails because optimized assembly requires Microsoft’s ml.exe; installing MDAC 2.5, Visual Studio Service Pack 5, then the Processor Pack supplies it, after which Quake and QuakeWorld build and run. Hacker News supplies FTP ASCII-mode context, corrects VC++6’s date to 1998, and recalls capable earlier IDEs, clean interfaces, and fragile SourceSafe.

### Comment pulse

- VC++6 offered definition lookup, breakpoints, stack traces, and inspection, but Borland, NeXTSTEP, XEmacs, and Ada environments had comparable features earlier.
- FTP ASCII mode can silently rewrite line endings and corrupt mixed archives — counterpoint: wrong Unicode or newline handling could produce similar symptoms.
- Building with only two warnings impressed readers; one cautions that a 1998 compiler exposed fewer diagnostics than modern toolchains.

### LLM perspective

- **View:** Reproducing historical software means reconstructing dependency order and file-transfer semantics, not merely obtaining old source and compilers.
- **Impact:** Preservation guides turn opaque build failures into repeatable procedures and reveal how much tooling assumptions become undocumented infrastructure.
- **Watch next:** Hash-pinned archives, reproducible VM images, documented binary outputs, and comparisons with the original VC++4 toolchain.
