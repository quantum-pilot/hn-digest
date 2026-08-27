# Windows drive letters are not limited to A-Z

- Score: 351 | [HN](https://news.ycombinator.com/item?id=46096556) | Link: https://www.ryanliptak.com/blog/windows-drive-letters-are-not-limited-to-a-z/

### TL;DR

Windows can treat symbols such as `+` and some non-ASCII characters as drive letters because Win32 drive paths are conventions mapped into NT Object Manager symbolic links, not an A–Z kernel limitation. `subst +: C:\foo` works in `cmd.exe`, though Explorer and PowerShell reject it. The exact behavior depends on path conversion, encoding, and a single UTF-16 code unit; one API even truncates `€` into `¬`. Commenters connected this hidden flexibility to registry, certificate, SharePoint, and directory-mounted drive namespaces.

### Comment pulse

- NT namespace insight → familiar DOS paths are one façade over a broader object hierarchy and symbolic-link system.
- Practical mounting → Windows can attach partitions beneath directories, though applications may miscalculate free space.
- Compatibility hazard → libraries disagree about whether symbol or Unicode-prefixed paths are absolute, creating parsing mismatches.

### LLM perspective

- View: The curiosity exposes a dangerous boundary between permissive kernel semantics and stricter user-space assumptions.
- Impact: Cross-language path code can misclassify valid Windows paths and mishandle security checks.
- Watch next: Test normalization libraries, encodings, shells, Explorer, and API behavior with identical unconventional paths.
