# Incomplete list of mistakes in the design of CSS

- Score: 184 | [HN](https://news.ycombinator.com/item?id=46227619) | Link: https://wiki.csswg.org/ideas/mistakes

### TL;DR
The piece catalogs long-standing design mistakes in CSS: overloaded properties like `display`, confusing layout primitives (floats, centering, z-index), and unhelpful defaults for things like headings and margins. Hacker News commenters add historical context: table-based layout was ugly but worked, and the early CSS alternatives regressed usability for years. Many see CSS’s quirks as artifacts of browser wars, rushed implementation, and backward compatibility rather than user-centered design, leaving developers with a powerful but often unintuitive system.  
*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Anti-table dogma → Pushing people to floats created a long layout dark age; flexbox/grid finally restored predictable centering and page structure — counterpoint: pre-CSS table abuse was genuinely disastrous.
- Confusing primitives → Overloaded `display`, z-index, vertical alignment, and default heading margins/styles feel arbitrary, encouraging misuse and harming accessibility and maintainability.
- Process failures → Many oddities stem from browser-war hacks and spec–implementation gaps, with little real-world designer research and heavy backward-compatibility constraints.

---

### LLM perspective
- View: CSS evolved reactively from HTML tag-soup, so its core APIs reflect accumulated compromises more than a cohesive model.
- Impact: Everyday developers pay the cost in cognitive load, debugging layout edge cases instead of focusing on product behavior.
- Watch next: Track proposals for simplification layers, opinionated frameworks, and better browser devtools that hide legacy quirks behind higher-level layout abstractions.
