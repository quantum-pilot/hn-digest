# A small number of samples can poison LLMs of any size

- Score: 657 | [HN](https://news.ycombinator.com/item?id=45529587) | Link: https://www.anthropic.com/research/small-samples-poison

TL;DR
Anthropic, the UK AI Security Institute, and the Alan Turing Institute show that inserting ~250 poisoned documents during pretraining can implant a backdoor across 600M–13B models: a trigger token causes gibberish. Success tracks the absolute count of poisons, not their percentage. Authors stress results cover low-stakes DoS behavior; applicability to larger models or harmful tasks remains open. HN debate splits between “predictable given the setup” and “practically worrying,” citing ease of seeding public datasets and challenges when poisoning contends with existing meanings.

Comment pulse
- Rare, unique trigger → easy backdoor; not size-dependent; 13B considered small — counterpoint: still practical to seed via public repos.
- Contended phrases need more poisons → race with benign usage; required count depends on clean-data prevalence and alignment with broader distributions.
- Garbage-in dynamics: hoaxes, jokes, and circular reporting propagate online; LLM training without rigorous curation compounds long-lived misinformation and accidental backdoors.

LLM perspective
- View: Fixed-count, rare-trigger backdoors are plausible in pretraining; they exploit uncontended tokens and don’t degrade general performance.
- Impact: Raises bar for data governance: source attribution, rarity filtering, canary insertion, checkpoint backdoor tests, and aggressive deduping of near-duplicates.
- Watch next: Probe larger models and harmful tasks; measure contended-trigger thresholds; evaluate defenses: trigger search, adversarial training, retrieval filtering, and post-training detox.
