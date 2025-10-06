# What GPT-OSS leaks about OpenAI's training data

- Score: 133 | [HN](https://news.ycombinator.com/item?id=45483924) | Link: https://fi-le.net/oss/

- TL;DR
  - By probing GPT‑oss’s embedding norms and “glitch tokens,” the author infers some rare Chinese spam/adult‑gambling phrases appeared in GPT‑5/oss training (membership inference), and observes a Spearman ~0.45 correlation with GitHub hits, hinting at possible sources. They argue tokenizer vocab leaks training traces and can induce odd failures. HN readers push back: embedding weight‑decay assumptions may be wrong; the headline overstates “trained on adult sites”; some translations seem off. Interest in broader LLM reverse‑engineering and bias after RLHF resurfaces.

- Comment pulse
  - Headline overreaches → evidence shows phrases present, not necessarily sourced from adult sites; GitHub blocklists/spam could explain presence.
  - Low L2 norms → unused tokens via weight decay; commenter: embeddings often exclude decay, maybe init/reserved effects — counterpoint: clustering remains anomalous.
  - Methodology needs tightening → some translations likely wrong; native review requested; prior work shows data extraction/membership inference is possible under constraints.

- LLM perspective
  - View: Open weights plus shared tokenizer expose measurable training traces via glitch tokens; membership inference is now practical in limited cases.
  - Impact: Tokenizer design and curation will matter more than ever; expect vocab pruning and per-region token sets to reduce leakage/cost.
  - Watch next: Replicate with non‑Chinese tokens; compare against Common Crawl and GitHub counts; test embeddings‑decay assumption; benchmark failure modes and DoS loops.
