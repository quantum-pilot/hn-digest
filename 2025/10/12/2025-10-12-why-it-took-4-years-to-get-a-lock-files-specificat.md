# Why it took 4 years to get a lock files specification

- Score: 118 | [HN](https://news.ycombinator.com/item?id=45556741) | Link: https://snarky.ca/why-it-took-4-years-to-get-a-lock-files-specification/

- TL;DR
    - Python finally standardized lock files (pylock.toml, PEP 751) after a four-year grind: reconciling sdists/wheels, platform/extras conditionals, multi-use portability, and resolver complexity, while keeping installs fast and tool-agnostic. PEP 665’s wheel-only approach was rejected; the accepted spec restores sdists and multi-use. PDM already supports it; uv and pip have partial support. HN debates uv’s Rust-fueled velocity versus slow PEP consensus—and notes uv still uses uv.lock for features the spec can’t yet express.

- Comment pulse
    - uv outpaces PEPs → funding and Rust yield fast, cohesive tooling; experiments leverage prior PEPs — counterpoint: Poetry delivered many of these benefits earlier.
    - Spec gap → uv keeps uv.lock because some project features can’t map to pylock.toml yet; it can export/read pylock for interop.
    - Process fatigue → commenters see Python/Django governance as slow and consensus-heavy; call for empowered final decision-maker or proven models like Postgres.

- LLM perspective
    - View: The spec’s multi-use model enables cross-platform reproducibility; real test will be resolver/installer interoperability and performance parity with uv.
    - Impact: Tool authors must encode conditional dependency graphs consistently; lock/installer split invites multiple implementations, including non-Python.
    - Watch next: Close uv mapping gaps, land pip defaults, add conda interop, standardize hash/signing, and publish cross-tool speed/repro benchmarks.
