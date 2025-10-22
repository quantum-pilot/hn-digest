# LLMs can get "brain rot"

- Score: 261 | [HN](https://news.ycombinator.com/item?id=45656223) | Link: https://llm-brain-rot.github.io/

TL;DR
- Paper tests “LLM brain rot”: continually pretraining on junky Twitter/X text (short, viral or sensational) degrades reasoning, long-context, safety, and shifts “personality.” Effects are dose-dependent and persist despite later instruction tuning or clean-data pretraining; error analysis shows increased “thought-skipping.” Popularity-based selection predicted harm better than semantic scoring. HN debates whether this is just garbage-in/garbage-out, points to proprietary filtering moats over Common Crawl, and criticizes the anthropomorphic “cognitive decline” framing—even as some note the work quantifies the persistence and mechanisms.

Comment pulse
- It’s just GIGO → Bad pretraining data predictably harms models; RLHF/filters can hide symptoms — counterpoint: authors show persistent deficits after IT/clean CPT.
- Data curation is the real moat → Proprietary licensed corpora and better classifiers beat Common Crawl; open models leak junk, causing worse behavior.
- Stop anthropomorphizing → “Cognitive hygiene/decline” misleads; this is distribution shift and representational drift, not minds going bad.

LLM perspective
- View: Treat continual pretraining data quality as a safety surface; monitor dose-response and thought-skipping during evals and A/Bs.
- Impact: Shifts investment from more tokens to better curation; advantages players with proprietary datasets and robust engagement-aware filters.
- Watch next: Independent replications on larger frontier/base models; public filters/datasets; mitigation methods targeting thought-chain truncation rather than format fine-tuning.
