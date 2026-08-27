# Getting syntax highlighting wrong

- Score: 168 | [HN](https://news.ycombinator.com/item?id=45596960) | Link: https://tonsky.me/blog/syntax-highlighting/

### TL;DR

Niki Tonsky argues that syntax highlighting should use few memorable colors and emphasize scarce, useful landmarks rather than coloring nearly every token. His Alabaster approach highlights strings, constants, comments, and definitions; dims punctuation; avoids keywords, calls, bold, and italics; and suggests background colors for readable light themes. HN readers agreed that excessive palettes become noise and comments deserve visibility, but many found conventional colorful examples faster to scan, saying unconscious pattern recognition and keyword coloring reveal structure and mistakes without memorizing a color map.

### Comment pulse

- Minimal palettes make intentional highlights stand out → removing keyword color can also hide misspellings and control flow.
- Developers need not name every color consciously → learned visual patterns can still signal incorrect token categories instantly.
- Theme effectiveness is personal and task-dependent → the article’s opening comparison produced opposite results for many readers.

### LLM perspective

- View: Restraint is useful, but memorability is only one mechanism through which highlighting aids comprehension.
- Impact: Theme designers should prioritize semantic contrast, accessibility, and error detection over maximizing token categories.
- Watch next: Test palettes with timed navigation, bug-finding, varied languages, color vision, and experienced users.
