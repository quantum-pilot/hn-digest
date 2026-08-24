# Parse, Don't Validate (2019)

- Score: 220 | [HN](https://news.ycombinator.com/item?id=46960392) | Link: https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/

### TL;DR

The essay’s type-driven design rule says boundary checks should return a precise representation preserving what was learned, rather than approve raw input and discard the proof. A nonempty-list type lets downstream code safely take a first element without repeated checks; maps can rule out duplicate keys. Parsing early makes illegal states harder to represent and avoids shotgun validation after state changes begin. Commenters endorsed boundary translation but debated whether its benefit is centralized checking or type-carried evidence, and noted that user-facing validators may still be needed to collect friendly errors.

### Comment pulse

- Validation that returns nothing loses knowledge → downstream functions must repeat checks or trust comments and supposedly impossible branches.
- Precise types move proof to construction → call sites cannot omit conversion because later functions require the refined value.
- Friendly errors can justify a front validator → counterpoint: successful input should still become the structured type consumed internally.

### LLM perspective

- View: The slogan is about preserving evidence, not renaming predicates: parsing converts uncertainty into an invariant the program can carry.
- Impact: Developers gain safer internal APIs and fewer partial operations, while paying modeling, conversion, and type-complexity costs at boundaries.
- Watch next: Language-specific patterns, aggregate error reporting, performance, mutable invariants, authorization before parsing, schema evolution, and empirical defect reduction.
