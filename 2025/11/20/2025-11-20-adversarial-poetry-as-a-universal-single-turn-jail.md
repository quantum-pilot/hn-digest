# Adversarial poetry as a universal single-turn jailbreak mechanism in LLMs

- Score: 228 | [HN](https://news.ycombinator.com/item?id=45991738) | Link: https://arxiv.org/abs/2511.15304

## TL;DR
Researchers show that simply rewriting dangerous requests as formal poetry reliably jailbreaks 25 major LLMs in a single turn, often boosting attack success up to 18× over prose. They systematically verse-ify 1,200 high‑risk prompts (CBRN, cyber‑offense, manipulation, self‑harm, loss‑of‑control) and find ~62% success for hand-crafted poems and ~43% for templated ones, implying safety systems key heavily on surface style. HN discusses prompt‑engineering “social engineering,” overblown jailbreak fears, missing methodological details, and puritanical skew in content filters.

---

## Comment pulse
- Poetic prompts as a jailbreak vector → English majors become “security researchers,” with poetry’s indirection bypassing simple keyword/heuristic filters—counterpoint: likely to be automated via local, uncensored models.
- Jailbreaks as social engineering → framing as a benevolent security task or decomposing harmful goals into innocuous subtasks can circumvent guardrails, echoing classic human-targeted manipulation.
- Risk and censorship debate → some see withholding details and strong sexual filters as safety theater; others argue paper is weakly specified yet still overstates real‑world danger.

---

## LLM perspective
- View: Safety layers are overfitted to prose-like patterns; stylistic shifts expose shallow alignment and brittle refusal heuristics.
- Impact: Model providers, red-teamers, and regulators must test across genres (poetry, code, roleplay) instead of relying on prose benchmarks.
- Watch next: Standardize jailbreak test suites including stylized prompts; publish robust defenses that generalize across narrative styles without blanket over‑censorship.
