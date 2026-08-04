# The Letter S, by Donald Knuth (1980) [pdf]

- Score: 261 | [HN](https://news.ycombinator.com/item?id=48216016) | Link: https://gwern.net/doc/design/typography/1980-knuth.pdf

### TL;DR

Knuth’s 1980 paper treats the letter S as a programmable design problem, using mathematical control points, slopes, and transitions to encode a typographer’s intent rather than merely trace an outline. The exercise grew from his effort to preserve the quality of The Art of Computer Programming after publishers moved away from metal typesetting, helping motivate METAFONT and TeX. HN commenters supplied detailed production history, praised the resulting books, debated why coded type design remained difficult, and flagged suspiciously duplicated glyphs in one scanned figure.

### Comment pulse

- Correctors said Volume II’s second edition used early TeX/METAFONT and an Alphatype phototypesetter, not revived Linotype; one participant described custom firmware and DVI transport.
- METAFONT sought reusable design logic, but typographers often think visually; Euler ultimately modeled outlines because simulating pen motion proved too difficult.
- Figure 9’s repeated pixel-identical glyphs prompted speculation about a scanning bug rather than an intentional comparison.

### LLM perspective

- View: Formalizing visual judgment exposes tacit rules, but the formal model may cost more effort than direct expert drawing.
- Impact: Knuth’s persistence made reproducible mathematical typography available to authors while preserving consistent design across machines and editions.
- Watch next: Compare source figures against scans, document reconstruction artifacts, and test parameterized glyphs across weights, sizes, and rasterizers.
