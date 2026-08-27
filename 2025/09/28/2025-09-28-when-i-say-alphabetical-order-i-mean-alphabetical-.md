# When I say “alphabetical order”, I mean “alphabetical order”

- Score: 313 | [HN](https://news.ycombinator.com/item?id=45404022) | Link: https://sebastiano.tronto.net/blog/2025-09-28-alphabetic-order/

### TL;DR

Sebastiano Tronto discovered that Windows, Google Drive, Dolphin, GNOME, and phone file managers applied “natural” numeric sorting rather than strict lexicographic order to timestamped photo names. One phone inserted an underscore before milliseconds while the other did not, causing numeric runs to be interpreted differently and grouping the files by device instead of capture time. Command-line `ls` sorted them as expected. The author fixed the issue by normalizing filenames and objected to software silently substituting guessed intent for literal ordering, though Dolphin offered a buried setting.

### Comment pulse

- Most commenters preferred natural sorting because it places `file-9` before `file-10`, but wanted clearer labels or an option.
- Others noted numeric interpretation produces surprising results for hashes, identifiers, decimals, and inconsistent naming schemes.

### LLM perspective

- View: Natural sorting is a sensible default, but hidden semantics make “sort by name” unreliable for machine-generated identifiers.
- Impact: Explicit modes and visible labels would preserve usability without forcing power users to rename data.
- Watch next: Whether file managers expose portable lexicographic sorting and define how mixed numeric tokens are parsed.
