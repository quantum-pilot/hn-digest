# YAML document from hell (2023)

- Score: 197 | [HN](https://news.ycombinator.com/item?id=45344554) | Link: https://ruudvanasseldonk.com/2023/01/11/the-yaml-document-from-hell

### TL;DR

The author argues YAML’s human-friendly surface hides a large, evolving specification, version-dependent parsing, surprising scalar coercions, aliases, tags, and non-string keys. The same document can mean different things under YAML 1.1 and 1.2, while templating adds another layer of fragile complexity. Suggested alternatives include TOML for simple configuration, JSON variants with comments, a deliberately restricted YAML subset, or generating JSON through Nix or Python. Commenters agreed that quoting strings avoids many traps, but questioned whether that defeats YAML’s main ergonomic appeal.

### Comment pulse

- Implicit typing creates footguns → innocent-looking values such as no, off, or numeric forms can change types unexpectedly.
- Defensive quoting reduces ambiguity → linters can enforce it, though needing them weakens the simplicity claim.
- JSON compatibility offers an escape hatch → many YAML consumers can accept generated JSON or mixed JSON-style syntax.

### LLM perspective

- View: YAML’s risk comes from invisible semantics, not indentation alone.
- Impact: Configuration errors can cross tools, parser versions, and environments without obvious textual changes.
- Watch next: Pin parser versions, lint restricted subsets, quote strings, and add cross-implementation golden tests.
