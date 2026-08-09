# Why I forked httpx

- Score: 231 | [HN](https://news.ycombinator.com/item?id=47514603) | Link: https://tildeweb.nl/~michiel/httpxyz.html

### TL;DR

Michiel forked Python’s HTTPX into httpxyz after a released zstd decoder proved broken, his fix stalled, and no HTTPX release appeared after November 2024. He also cites hidden issues, disabled discussions, years of unfinished 1.0 work, and prior breaking minor releases; OpenAI and Anthropic already exclude 1.0 in dependency constraints. Httpxyz promises conservative maintenance, no rewrite, shared stewardship, and Codeberg hosting. Immediate migration is optional, and plugin compatibility remains uncertain. HN agreed maintenance is a valid concern but questioned adding another client fork.

### Comment pulse

- Some urged joining Niquests or using Pyreqwest instead, citing stronger performance and avoiding further ecosystem fragmentation.
- Announcing a contemplated fork can sound threatening — counterpoint: unmerged fixes and blocked participation make an implemented fork legitimate leverage.
- Readers blamed Python’s weak standard HTTP client, while others noted friendly, comprehensive async HTTP APIs challenge most language ecosystems.

### LLM perspective

- **View:** A maintenance fork succeeds through dependable releases and governance, not merely dissatisfaction with upstream.
- **Impact:** Users gain an escape path but must absorb namespace, extension, and dependency compatibility costs.
- **Watch next:** Release cadence, security response, downstream adoption, plugin support, and collaboration with competing clients.
