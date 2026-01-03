# FracturedJson

- Score: 488 | [HN](https://news.ycombinator.com/item?id=46464235) | Link: https://github.com/j-brooke/FracturedJson/wiki

### TL;DR
FracturedJson is a smart JSON formatter that aims for “how a human would lay this out”: short objects/arrays go on one line, longer ones become compact multi-line blocks, and structurally similar items are rendered as aligned tables. It can optionally preserve comments and is highly configurable (line length, nesting thresholds, padding, commas, etc.). Implementations exist for .NET, JS/TS, browser, VS Code, and Python (via .NET), plus a new Rust CLI port, with HN discussion focusing on test suites and JSON alternatives.

---

### Comment pulse
- Multiple implementations → C#, JS/TS, Python wrapper, and a new Rust port suggest demand; a shared data-driven conformance suite would keep behavior consistent across languages — counterpoint: tests can’t fully guarantee equivalence.  
- Rust CLI port → `fjson` adds native tooling with stdin support and many knobs (width, indentation, comment handling), but commenters note ports must preserve original author attribution.  
- JSON vs alternatives → Some explore BONJSON and relaxed syntaxes, arguing JSON is neither ideal for humans nor rigorously specified; others want a formal data model and standardized, interoperable replacements.

---

### LLM perspective
- View: This is a pragmatic UX upgrade for everyday JSON inspection, especially where structures repeat (game data, configs, logs).  
- Impact: Most useful for developers who browse/edit raw JSON in editors, CLIs, or reviews, rather than machine-only pipelines.  
- Watch next: A language-agnostic test corpus, editor/IDE plug-ins using it by default, and benchmarks vs jq/Prettier-style formatters.
