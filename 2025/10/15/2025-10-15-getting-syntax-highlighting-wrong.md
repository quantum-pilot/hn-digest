# Getting syntax highlighting wrong

- Score: 168 | [HN](https://news.ycombinator.com/item?id=45596960) | Link: https://tonsky.me/blog/syntax-highlighting/

- TL;DR
    - The author argues most editors misuse syntax highlighting: too many bright hues flatten salience. He proposes a minimal, memorable palette: emphasize strings/constants and top-level defs, dim punctuation, avoid keyword coloring, and boldly highlight explanatory comments. For light themes, use background tints to keep colors vivid without losing contrast; ignore uniform “scientific” palettes. HN is split: some rely on rich colors and pattern recognition (especially for catching typos), others prefer restrained schemes; consensus leans toward fewer, higher-signal channels.

- Comment pulse
    - Minimalist camp → Prioritize names/constants, bold comments, dim punctuation; fewer hues reduce noise and improve structure perception.
    - Power-user camp → Dense, accurate coloring leverages pattern recognition; keyword colors catch typos fast; tree-sitter/LSP makes categories reliable — counterpoint: excess hues blur salience.
    - Ergonomics/UX → Question “base text color”; suggest richer token decorations beyond color; preferences vary by language; even colorblind users report benefits from more channels.

- LLM perspective
    - View: Optimize highlighting for search and error detection; limit channels but make them high-signal; semantics beat taxonomy.
    - Impact: Theme authors, IDEs can add background tints, salience tiers, and per-token decorations; accessibility presets for color vision deficiencies.
    - Watch next: Run A/B studies: scan time, bug-spot rate, fatigue; compare minimal vs rich palettes; assess tree-sitter precision across languages.
