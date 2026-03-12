# Writing my own text editor, and daily-driving it

- Score: 217 | [HN](https://news.ycombinator.com/item?id=47331034) | Link: https://blog.jsbarretto.com/post/text-editor

### TL;DR
A developer wrote their own text editor and now uses it daily, highlighting how tailoring your primary work tool can greatly boost comfort and productivity. HN commenters echo this, with several people using homegrown editors for a decade or more and describing strong “fit” and joy. Others discuss the practical side: outsourcing hard parts to LSP, Tree-sitter, fzf, or existing GUI/terminal stacks, and the surprising difficulty of finding reusable, modern text-editing cores for GUI apps.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Personal editors as life tools → Long-time users (10–19 years) say custom editors repay effort many times in joy and productivity.
- Pragmatic architecture → Reuse LSP, Tree-sitter, fzf; design suckless-style tweakable core; early weeks are bug hell, then compounding productivity.
- Libraries and GUI pain → GUI-first devs struggle to find embeddable text cores; suggestions: modern terminals, Scintilla, SDL+TTF, raylib—counterpoint: stb_textedit is powerful but painful and outdated.

---

### LLM perspective
- View: Writing your own editor is a deep-skill, niche project; best for enthusiasts who live in text all day.
- Impact: Most developers should heavily customize existing editors; library gaps especially hurt those needing lightweight, custom GUIs.
- Watch next: Better standalone text-core libraries, richer terminal capabilities, and composable editor frameworks could make custom editors far more accessible.
