# List animals until failure

- Score: 321 | [HN](https://news.ycombinator.com/item?id=46842603) | Link: https://rose.systems/animalist/

### TL;DR
A browser game by Vivian Rose challenges you to list as many animals as possible under time pressure, with bonus seconds for each valid entry. Animals must have Wikipedia pages, and overly overlapping terms (e.g., “bear” then “polar bear”) don’t both score. The implementation leans on Wikipedia/Wikidata and manual tuning, not LLMs. HN players enjoyed the cognitive workout and humor, but ran into edge cases and misclassifications that expose how messy real-world taxonomy and knowledge-graph matching can be.

---

### Comment pulse
- Cognitive strain → Rapid recall under a ticking timer quickly exhausts semantic memory; people visualize animals but can’t retrieve names, even moments after stopping.  
- Taxonomy quirks → Wikipedia/Wikidata rules mis-handle overlaps (jellyfish vs man-o-war, bobcat vs lynx, kudu→turtle), revealing fuzzy species/colony boundaries — counterpoint: strict practical rules beat perfect biology.  
- Spin‑offs and lineage → A speech-recognition clone lets groups shout animals at a screen; commenters link inspirations to a viral tweet and classic Sporcle-style quizzes.

---

### LLM perspective
- View: Neat example of a small, well-crafted, non-LLM app that still hinges on large curated knowledge bases and tricky entity resolution.  
- Impact: Useful micro-tool for cognitive testing, party games, and informal education about species diversity and classification limits.  
- Watch next: Better synonym handling, tunable strictness (species vs broader groups), multiplayer/speech modes, and anonymized logs for cognitive-science or UX studies.
