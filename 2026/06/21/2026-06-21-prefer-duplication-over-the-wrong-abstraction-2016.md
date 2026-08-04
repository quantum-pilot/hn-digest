# Prefer duplication over the wrong abstraction (2016)

- Score: 414 | [HN](https://news.ycombinator.com/item?id=48620090) | Link: https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction

### TL;DR

Sandi Metz argues an abstraction can cost more than duplication when similar callers evolve for different reasons. Teams preserve the shared layer through flags, parameters, and conditionals until it interleaves distinct behaviors and becomes fragile. Her recovery method is deliberate reversal: inline the abstraction into every caller, keep only each caller’s required path, delete the shared construct, then let duplication reveal better boundaries. HN largely agreed, adding a test: duplication is dangerous when divergence would be a bug; otherwise locality and distinct change reasons outweigh forced DRYness.

### Comment pulse

- Single source of truth remains non-negotiable → if two copies must change together, divergence is a defect and duplication creates invisible long-distance coupling.
- Change locality is the deciding property → code that merely looks alike should stay separate unless its instances evolve for the same reasons.
- Duplication supplies evidence → UnitLoader, CorpseLoader, and EffectLoader can expose commonality before an EverythingLoader accumulates speculative branches — counterpoint: team silos also duplicate real concepts.

### LLM perspective

- **View:** Abstraction quality is temporal: the right interface encodes shared reasons for change, not a snapshot of similar implementation.
- **Impact:** Maintainers regain understandable local code and safer feature work; reviewers must tolerate temporary repetition while resisting genuinely duplicated policy.
- **Watch next:** Track boolean flags, caller-specific branches, coordinated edits, and rollbacks; inline when customization grows, then re-extract only common behavior.
