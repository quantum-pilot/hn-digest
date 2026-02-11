# Parse, Don't Validate (2019)

- Score: 220 | [HN](https://news.ycombinator.com/item?id=46960392) | Link: https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/

- TL;DR  
Type-driven design is framed as “parse, don’t validate”: transform unstructured/weakly-typed inputs into richer types that *encode* invariants (e.g., `NonEmpty`, `Map`, smart constructors) at system boundaries. That turns partial functions into total ones, eliminates scattered checks, and lets the compiler enforce invariants, avoiding “shotgun parsing” where errors surface late after state changes. The article gives concrete Haskell patterns but the core idea—design data so illegal states are unrepresentable—is broadly applicable, which HN debates across static vs dynamic, OO, and usability concerns.

- Comment pulse  
  - This is old static-typing wisdom → in practice many codebases still pass strings/dicts everywhere and skip domain types—counterpoint: it’s not “natural”; it has to be learned.  
  - Key value is locality and proof-carrying types → parse/translate at the edge, then rely on strong types internally to remove defensive checks.  
  - Parsing vs validation isn’t either/or → use rich types plus separate validators to accumulate many user-facing errors (e.g., big CSV imports).

- LLM perspective  
  - View: Treat this as a design discipline: model invariants in types first, then write code that merely shuffles verified data.  
  - Impact: Mainstream OO languages can approximate this with value objects, enums, and factories/smart constructors.  
  - Watch next: Libraries that auto-generate parsers/validators from schemas and surface domain-specific types in IDEs/tooling.
