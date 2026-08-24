# How to choose colors for your CLI applications (2023)

- Score: 142 | [HN](https://news.ycombinator.com/item?id=46810904) | Link: https://blog.xoria.org/terminal-colors/

### TL;DR

Luna Razzaghipour tests the terminal’s 16 named colors across macOS Basic, Ubuntu Tango, Solarized, and Sorcerer, showing that palette names do not guarantee contrast. Bright colors, black, white, and even bold can become unreadable because themes remap slots and some terminals render bold as bright. Only 11 of 32 regular-or-bold combinations survive the author’s compatibility screen. HN commenters favor default colors, user configurability, and avoiding semantic meaning conveyed by red versus green alone.

### Comment pulse

- Use terminal defaults and avoid fixed backgrounds → users can then configure a readable foreground/background pair globally.
- Color should remain optional and runtime-configurable → operators may inherit unknown themes or troubleshoot on poor displays.
- Red-versus-green semantics fail some color-blind users and vary culturally → pair color with text, symbols, or other redundant cues.

### LLM perspective

- View: ANSI color names describe slots, not perceptual colors; application authors cannot assume brightness or contrast.
- Impact: Conservative palettes improve accessibility and prevent invisible diagnostics during urgent terminal work.
- Watch next: Test light, dark, Solarized, bold-as-bright, no-color, and common color-vision deficiencies in CI snapshots.
