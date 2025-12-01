# Windows drive letters are not limited to A-Z

- Score: 351 | [HN](https://news.ycombinator.com/item?id=46096556) | Link: https://www.ryanliptak.com/blog/windows-drive-letters-are-not-limited-to-a-z/

### TL;DR
Windows’ “drive letters” are just names in the NT Object Manager namespace, not hard‑coded A–Z slots. Any single UTF‑16 code unit followed by `:\` that `RtlDosPathNameToNtPathName_U` maps into `\??\` behaves like a drive: you can create `+:` or `€:` and use them in `cmd.exe`. Higher‑level tools (Explorer, PowerShell, many libraries) still enforce A–Z or ASCII, causing inconsistencies and weird edge cases like `€:` turning into `¬:`. HN discussion highlights NT’s richer namespace, mount points, and DOS-era legacy quirks.

---

### Comment pulse
- NT Object Manager gives a global namespace (`\Device`, `\Registry`, etc.), with DOS-style paths as a compatibility layer; PowerShell PSDrives expose arbitrary backends. — counterpoint: Unix already exposes certs and system state as files, just less uniformly.
- Partitions aren’t limited to letters: NTFS volumes can be mounted into directories (via Disk Management or PowerShell), useful to trick installers or stitch heterogeneous storage under `C:\`.
- Commenters marvel at NT’s flexible, underused kernel features versus the dated DOS façade; cursed examples like `€:\` and blocked emoji drives show how UI layers lag behind.  

---

### LLM perspective
- View: Path-handling code that assumes `[A-Z]:\` is complete is subtly wrong on modern Windows and can misclassify real paths.
- Impact: Systems languages, build tools, and security software should consider NT namespace behavior, not just Win32 conventions, for correctness and hardening.
- Watch next: More tests around non-ASCII “drives,” better Object Manager tooling, and potential guidance from Microsoft on supporting or formally deprecating such edge cases.
