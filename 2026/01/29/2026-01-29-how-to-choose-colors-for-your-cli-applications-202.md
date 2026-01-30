# How to choose colors for your CLI applications (2023)

- Score: 142 | [HN](https://news.ycombinator.com/item?id=46810904) | Link: https://blog.xoria.org/terminal-colors/

### TL;DR
The post walks through how the same ANSI “16‑color” choices look under several popular terminal themes (macOS Basic, Tango, Solarized, Sorcerer) and shows that many combinations become unreadable or repurposed (notably Solarized’s bright colors and brblack). Bold can also silently map to “bright” colors. After eliminating problematic cases, only about 11 of 32 foreground/bold combinations are reliably legible. The author urges CLI authors to use this restricted subset or provide proper theming rather than assuming their own terminal setup.

---

### Comment pulse
- Stick to 8/16 ANSI colors, avoid explicit backgrounds, and let users configure schemes per terminal; beyond that, applications must expose runtime color configuration.  
- Many ops disable color entirely after unreadable black‑on‑black or dark‑on‑dark consoles; “you can customize it” doesn’t help at 3 a.m. on a random server.  
- Minimalist palette for CLIs versus rich TUIs: some want only default/red/green; others note colorblindness, cultural meanings, and argue for configurability over hard conventions.  

---

### LLM perspective
- View: Treat CLI color as an accessibility concern; design for hostile themes, not just your favorite dark scheme.  
- Impact: Library authors (logging, CLIs, TUIs) should codify “safe palettes” and expose per‑profile themes by default.  
- Watch next: Shared test suites that screenshot tools across popular themes and color‑vision simulations to automatically flag unreadable combinations.
