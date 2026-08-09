# Fixing a 20-year-old bug in Enlightenment E16

- Score: 254 | [HN](https://news.ycombinator.com/item?id=47774789) | Link: https://iczelia.net/posts/e16-20-year-old-bug/

### TL;DR

A specific long PDF title froze Enlightenment E16 because its middle-ellipsis fitting loop never terminated. Repeated debugger samples revealed a two-state oscillation in a Newton-style estimate of how many characters to remove: proportional font widths made the approximate derivative overshoot forever. The patch adds a 32-iteration cap followed by a one-character fallback, clamps the removal count, and prevents division by zero, applying the safeguards to ASCII and multibyte paths. Commenters celebrated the deterministic reproducer, E16’s surprising modern lightness, and open source’s ability to keep decades-old software usable.

### Comment pulse

- Readers corrected “sadly deterministic”: a reproducible failure supplies both a test case and decisive evidence that a patch works.
- Veterans remembered Enlightenment as visually extravagant yet efficient; today its 24 MB peak footprint makes yesterday’s bling genuinely lightweight.
- Long-term availability was framed as open source’s quiet advantage — counterpoint: projects can still alienate users through unwanted redesigns.

### LLM perspective

- **View:** The bug is a textbook numerical-method failure inside UI code: convergence was assumed where only a heuristic existed.
- **Impact:** A bounded fallback preserves fast average behavior while preventing one unusual title from freezing the entire window manager.
- **Watch next:** Upstream acceptance, a regression test using the 81-character title, and similar unbounded approximation loops elsewhere in E16.
