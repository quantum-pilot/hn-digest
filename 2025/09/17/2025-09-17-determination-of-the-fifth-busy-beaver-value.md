# Determination of the fifth Busy Beaver value

- Score: 270 | [HN](https://news.ycombinator.com/item?id=45273999) | Link: https://arxiv.org/abs/2509.12337

- TL;DR
  - bbchallenge proves S(5)=47,176,870: the longest-running 5‑state, 2‑symbol Turing machine halts after 47,176,870 steps. They enumerate 181,385,789 machines and, via a pipeline of formally verified deciders in Coq (Rocq)—loops, abstract n‑gram CPS, counting (RepWL), regex/FSM (FAR/WFAR)—classify every machine as halting or non‑halting, with a handful of “sporadics” handled by manual proofs. The work showcases massively collaborative, reproducible proof engineering; this preprint consolidates last year’s result into a citable, formally verified account.

- Comment pulse
  - Formal pipeline over brute force → Coq‑BB5 skips long simulation; low‑step loop detection finds halters; only 183 needed long runs — counterpoint: counts differ from legacy.
  - Champion’s behavior → high‑level Collatz‑like iteration; complex yet terminating; BB6 contenders may also exploit Collatz heuristics.
  - Collaboration as method → bbchallenge.org coordinated proofs; parallels with Lean blueprint projects, ConwayLife, Googology; this preprint packages last year’s discovery for citation.

- LLM perspective
  - View: Combining abstract interpretation with proof assistants scales to exhaustive classifications of small universal models.
  - Impact: New stress-tests for Coq/Lean tooling, automata libraries, and decider design; datasets for verification and static-analysis research.
  - Watch next: BB6 partial proofs, generalized deciders, reproducible Coq artifacts, compute budgets, and community governance for large formal collaborations.
