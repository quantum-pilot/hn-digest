# YAML document from hell (2023)

- Score: 197 | [HN](https://news.ycombinator.com/item?id=45344554) | Link: https://ruudvanasseldonk.com/2023/01/11/the-yaml-document-from-hell

- TL;DR
  - YAML’s “human-friendly” design hides footguns: 1.1 vs 1.2 differences (e.g., no/off → false), sexagesimal literals (22:22), unsafe tags, non‑string keys, and accidental number parsing. The author advises TOML or generating JSON (via Nix/Python) instead of templating YAML. HN largely agrees on the hazards; many mitigate by always quoting strings and linting, note that YAML parsers accept pure JSON/JSON-with-comments, and criticize spec bloat and tooling inconsistencies (e.g., Ansible).

- Comment pulse
  - Quote everything → Avoids implicit bools/numbers; add yamllint to enforce. — counterpoint: Mandatory quoting reintroduces delimiters, undermining YAML’s main ergonomic draw.
  - Use JSON under YAML parsers → YAML is a superset; pure JSON or JSON-with-comments often works. Caveat: fails if app relies on non-string keys.
  - Spec overreach caused surprises → 'no/off' and sexagesimals led to Norway-type bugs; docs/tools (e.g., Ansible) remain inconsistent years after 1.2.

- LLM perspective
  - View: Treat YAML as input, not logic → avoid templating; generate JSON or restrict to a documented YAML subset.
  - Impact: Standardize parsers and rules → pin YAML version, disable dangerous tags, require quoted strings, enforce with CI.
  - Watch next: Parser updates and ecosystems → PyYAML/libyaml 1.2 support, GitHub Actions handling of on:, real-world adoption of RCL/CUE/Nix for config.
