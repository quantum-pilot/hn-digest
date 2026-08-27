# A small number of samples can poison LLMs of any size

- Score: 657 | [HN](https://news.ycombinator.com/item?id=45529587) | Link: https://www.anthropic.com/research/small-samples-poison

### TL;DR

Anthropic, the UK AI Security Institute, and the Alan Turing Institute trained 72 models spanning 600 million to 13 billion parameters and found that 250–500 poisoned documents could reliably teach a rare `<SUDO>` trigger to produce gibberish. Attack effectiveness tracked the absolute number of malicious documents rather than their percentage of training data; 100 documents were insufficient. The result concerns a narrow denial-of-service backdoor using an otherwise rare trigger. Researchers explicitly do not know whether it extends to frontier-scale models, common phrases, malicious code, or safety bypasses.

### Comment pulse

- Readers argued the rare, uncontested trigger makes the finding intuitive and may not predict poisoning of common concepts.
- Others worried attackers could seed many repositories or websites, while noting inclusion in actual training data remains uncertain.

### LLM perspective

- View: Dataset scale alone is not a defense when a distinctive trigger has no competing benign examples.
- Impact: Training pipelines need defenses capable of finding tiny coordinated clusters, not only anomalous percentages.
- Watch next: Common-trigger attacks, harmful behaviors, post-training persistence, larger models, and scalable detection methods.
