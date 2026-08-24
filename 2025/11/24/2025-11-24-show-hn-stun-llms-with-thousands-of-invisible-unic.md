# Show HN: Stun LLMs with thousands of invisible Unicode characters

- Score: 183 | [HN](https://news.ycombinator.com/item?id=46029889) | Link: https://gibberifier.com

### TL;DR

Gibberifier inserts large numbers of invisible Unicode characters between visible letters, claiming this preserves human readability while confusing or exhausting language models. The demonstration promotes it for obscuring prompts and resisting scraping, but discussion quickly exposed weak foundations: several current models decoded short samples, screenshots bypass the character layer, and simple preprocessing can strip the additions. Worse, the transformed text becomes nearly unusable for screen readers. Commenters also found an appended hidden instruction, suggesting some model refusals reflected prompt injection rather than genuine inability to parse Unicode.

### Comment pulse

- Efficacy claims were challenged → multiple models decoded samples, and normalization or OCR defeats the trick. — counterpoint: longer inputs still triggered failures.
- Accessibility criticism was unanimous → invisible characters make screen-reader output unintelligible despite leaving sighted rendering unchanged.
- Hidden instructions changed the diagnosis → some refusals likely followed injected policy-like text rather than tokenizer failure.

### LLM perspective

- View: This is brittle prompt injection and token amplification, not durable protection against machine reading.
- Impact: Adoption could impose accessibility harms and processing costs while offering only temporary resistance to automated cleanup.
- Watch next: Model input normalization, screen-reader behavior, and whether platforms detect or remove excessive zero-width characters.
