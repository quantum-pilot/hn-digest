# Automatic Programming

- Score: 196 | [HN](https://news.ycombinator.com/item?id=46835208) | Link: https://antirez.com/news/159

### TL;DR
Antirez (creator of Redis) proposes “automatic programming” as the new normal: humans drive design, specs, and review while LLMs handle most code-writing. He contrasts this with “vibe coding,” where people toss in vague prompts and accept the first draft, leading to shallow, low-owned code. For him, well-guided AI output is genuinely “your” work, built atop a collective training corpus, and the scarce value shifts from typing code to having clear vision, architecture, and judgment.

---

### Comment pulse
- Spec-first + multi-round AI self-review feels like a mini-waterfall revival: higher quality, fewer surprises, but skeptics note specs often fail against messy reality.  
- Guided “zen coding” yields robust implementations from strong specs; unguided vibe coding tends to produce first-draft code and encourages skipping architecture and cleanup.  
- Training data as “collective gift” is contested: some call it non-consensual appropriation; others say all software reuses predecessors—counterpoint: open-source licenses didn’t anticipate LLM training.

---

### LLM perspective
- View: Automatic programming treats LLMs as powerful compilers from high-level intent; real leverage is in specification, decomposition, and review.  
- Impact: Senior engineers shift toward system design and spec authoring; organizations must formalize review/ownership of AI-generated changes.  
- Watch next: Court decisions on training legality and GPL implications, plus benchmarks comparing spec-driven AI workflows vs traditional agile teams.
