# Nix Derivation Madness

- Score: 149 | [HN](https://news.ycombinator.com/item?id=45772347) | Link: https://fzakaria.com/2025/10/29/nix-derivation-madness

### TL;DR

The author discovers that a Nix store output can name a missing deriver even though local evaluation produces a different `.drv`. Fixed-output derivations explain the mismatch: changing irrelevant derivation attributes changes their `.drv` paths and dependent derivation trees, while content-addressed output paths remain identical. Consequently, multiple derivations can map to one output, and some inputs can disappear without changing it. Commenters call the `deriver` field misleading rather than buggy and point toward build traces, stronger provenance, and content-addressed derivations as clearer models.

### Comment pulse

- `deriver` is not unique provenance → cache metadata may preserve an older derivation path than current local evaluation produces.
- Content addressing changes expectations → identical outputs can legitimately arise from different derivations, while irreproducible builds may diverge.
- Better build traces could help → explicit origin maps may improve SBOMs, diagnostics, and tooling without pretending outputs have one parent.

### LLM perspective

- View: Nix’s reproducibility story needs separate identities for recipes, build events, and resulting content.
- Impact: Auditors cannot infer exact provenance from the `Deriver` field alone when fixed-output inputs churn.
- Watch next: Follow build-trace provenance work, CA-derivation semantics, and documentation replacing hash-derivation-modulo concepts.
