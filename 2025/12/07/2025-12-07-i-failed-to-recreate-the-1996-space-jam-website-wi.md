# I failed to recreate the 1996 Space Jam Website with Claude

- Score: 250 | [HN](https://news.ycombinator.com/item?id=46183294) | Link: https://j0nah.com/i-failed-to-recreate-the-1996-space-jam-website-with-claude/

### TL;DR

Using Claude Opus 4.1, the author supplied a screenshot and original assets for the 1996 Space Jam homepage, then logged repeated reconstruction attempts. Claude recognized the planet-orbit concept but produced inaccurate geometry while declaring success. Explicit reasoning, coordinate grids, color diffs, side-by-side screenshots, regional crops, and 200% zoom only anchored increasingly precise adjustments to the wrong layout. The author cautiously attributes this gap to coarse visual representation and self-evaluation bias. Commenters corrected a key premise: the original layout used HTML tables, not absolute positioning.

### Comment pulse

- Historical structure changed the task → a commenter’s one-shot Opus 4.5 attempt used tables, matching the original implementation method.
- Visual weakness is task-specific → LLMs may miss intricate layouts while succeeding quickly on difficult, text-rich programming work.
- Preservation need not mean reconstruction → retaining the tiny original HTML and assets avoids lossy screenshot-to-code translation.

### LLM perspective

- View: Semantic scene understanding does not guarantee metric visual precision.
- Impact: Screenshot-driven frontend work still needs measured geometry, external validation, and human correction.
- Watch next: Models with pixel-coordinate tools, independent visual graders, and experiments separating reference images from self-generated feedback.
