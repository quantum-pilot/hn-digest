# Learn Prolog Now

- Score: 233 | [HN](https://news.ycombinator.com/item?id=45900978) | Link: https://lpn.swi-prolog.org/lpnpage.php?pageid=top

- TL;DR
    - Learn Prolog Now is a long-running introductory course now wired to SWI’s in-browser SWISH, so examples run live. A proxy rewrites pages to detect code and queries, though mapping between fragments is imperfect; the site urges hands-on practice and updates. HN discussion centers on pairing Prolog with LLMs: let models draft rules, solvers verify reasoning, but reliability and scale remain hard, and alternatives like Z3 may fit better. Many praise Prolog’s mind-bending pedagogy, while noting scarce industry use and integration/performance tradeoffs.

- Comment pulse
    - LLM + Prolog for reliable reasoning → model writes rules; solver verifies; prototypes exist; scaling robust synthesis is hard — counterpoint: prefer Z3; Prolog mostly brute-force search.
    - Prolog expands programmers’ logical thinking → courses convert skeptics; exercises are fun; cut/backtracking teach control — counterpoint: few find industry uses afterward.
    - Integrating logic with stateful apps is awkward → custom embedded Prolog eases interfaces, but runs ~10,000x slower than SWI; Exercism track helps newcomers.

- LLM perspective
    - View: Embedded SWISH makes Prolog hands-on; great for learning and prototyping, less suited to production without careful interfacing.
    - Impact: Expect Prolog/Z3 as verifier tools in LLM pipelines to boost reliability on symbolic tasks and rule-heavy domains.
    - Watch next: Head-to-head evaluations on logic benchmarks; SWI-SWISH improvements linking code and queries; better host-language bridges for stateful systems.
