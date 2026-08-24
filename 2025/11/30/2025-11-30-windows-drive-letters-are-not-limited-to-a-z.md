# Windows drive letters are not limited to A-Z

- Score: 351 | [HN](https://news.ycombinator.com/item?id=46096556) | Link: https://www.ryanliptak.com/blog/windows-drive-letters-are-not-limited-to-a-z/

### TL;DR

Windows drive syntax is a convention layered over NT’s Object Manager, not a kernel rule reserving A through Z. The Win32 path converter accepts any single UTF-16 code unit before a colon, so Command Prompt and `subst` can use symbols or many non-ASCII characters. Explorer, PowerShell, and language libraries often impose narrower rules, creating compatibility mismatches. Characters outside the Basic Multilingual Plane need surrogate pairs and fail path classification. One volume API adds another quirk by apparently truncating a euro sign into ¬.

### Comment pulse

- Object Manager links explain the flexibility → familiar drive names are aliases into a broader namespace, not fundamental filesystem roots.
- Library assumptions create edge cases → Rust accepts only alphabetic prefixes while Zig chose closer Windows compatibility for decoded BMP characters.
- Directory mount points avoid letters entirely → useful for storage layouts, though installers may misread capacity or reject unusual targets.

### LLM perspective

- View: Path parsers should treat platform APIs as behavioral specifications, because intuitive drive-letter rules are observably incomplete.
- Impact: Cross-platform libraries can misclassify valid paths when byte-oriented parsing diverges from Windows’ UTF-16 semantics.
- Watch next: Tests should compare shells, system APIs, and libraries across symbols, BMP characters, and surrogate pairs.
