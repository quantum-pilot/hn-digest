# Why it took 4 years to get a lock files specification

- Score: 118 | [HN](https://news.ycombinator.com/item?id=45556741) | Link: https://snarky.ca/why-it-took-4-years-to-get-a-lock-files-specification/

### TL;DR

Python’s `pylock.toml` specification emerged after years of debate over what a portable lock file must represent: wheels, source distributions, source trees, platform markers, extras, dependency groups, hashes, and installer-independent metadata. The wheel-only PEP 665 failed because existing workflows required source packages and build dependencies. PEP 751 then cycled through multi-use graphs, project sets, and a single-use compromise before consensus restored multi-use support and acceptance in March. PDM, uv, and pip now offer some support, though uv retains its richer native lock format.

### Comment pulse

- Readers praised uv’s execution speed while noting it benefits from the packaging standards that lengthy consensus work produced.
- Others saw the process as evidence that broad compatibility and volunteer governance can institutionalize delay.

### LLM perspective

- View: The delay reflects real cross-platform semantics and ecosystem politics, not merely difficulty serializing dependencies.
- Impact: A neutral interchange format can reduce tool lock-in even when native formats retain additional features.
- Watch next: Default adoption, round-trip fidelity, source-build security, and whether major tools converge on interoperable behavior.
