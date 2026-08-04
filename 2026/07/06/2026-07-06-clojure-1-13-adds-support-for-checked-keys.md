# Clojure 1.13 adds support for checked keys

- Score: 191 | [HN](https://news.ycombinator.com/item?id=48767211) | Link: https://clojure.org/news/2026/07/02/clojure-1-13-alpha1

### TL;DR

Clojure 1.13.0-alpha1 introduces opt-in checked map destructuring: `:keys!`, `:syms!`, and `:strs!` throw when required keys are absent, while keys after `&` can document or validate accepted-but-unbound inputs. A new `req!` lookup reports missing keys, and keyword-only PersistentArrayMaps now remain arrays through 64 entries rather than eight for faster small-map access. HN split over philosophy: supporters expect earlier, clearer failures for misspellings and bad nesting; skeptics prefer nil-punning, assertions, or boundary schemas. The feature remains additive and runtime-checked, not static typing.

### Comment pulse

- Silent nils defer diagnosis → a misspelled or misplaced required key can propagate until an unrelated failure, obscuring the original defect.
- Inline checks bridge a tooling gap → they document a function’s immediate contract without introducing a separate spec or Malli schema.
- Runtime throwing is deliberately optional → callers retain nil-punning — counterpoint: skeptics question whether assertions already cover this narrow need.

### LLM perspective

- **View:** Checked keys add a concise local contract for dynamic maps while preserving Clojure’s open-map and nil-friendly defaults.
- **Impact:** Earlier failures should reduce debugging distance for malformed inputs, especially before teams adopt comprehensive schemas.
- **Watch next:** ClojureScript parity, error-message quality, adoption patterns, and whether checked destructuring reduces production incidents without encouraging excessive exceptions.
