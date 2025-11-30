# Hachi: An Image Search Engine

- Score: 117 | [HN](https://news.ycombinator.com/item?id=46087549) | Link: https://eagledot.xyz/hachi.md.html

### TL;DR
Hachi is a fully self-hosted image search engine for personal data, built with a strong emphasis on minimal dependencies, custom infrastructure, and privacy. It indexes images across drives/devices without duplicating originals, combining a Nim-based metadata store, a simple vector index, and locally run ML models (CLIP-like + face recognition) to enable semantic and attribute-based search. The HN discussion praises the engineering ambition and personal-search focus, while questioning long‑term viability of self-hosted ML and noting widespread demand for high-quality private search across personal archives.

---

### Comment pulse
- Personal-search gap → Users want unified, private search across photos, files, and history; OS and mainstream tools feel fragmented or shallow.  
- DIY depth → Custom meta-index and vector DB impress tinkerers; they like minimal deps and cross-device design—counterpoint: evolving embeddings may outpace local stacks.  
- Self-hosted ML debate → Some see on-device models as brittle amid rapid progress; author argues model swapping is easy, core challenge is fast, rich indexing.

---

### LLM perspective
- View → Core value is architecture: unified, non-duplicating index over heterogeneous personal data with semantic + hard filters.  
- Impact → Power users, photographers, and small teams gain serious local search without cloud lock-in or data leak risk.  
- Watch next → Swap in stronger image encoders, add text/audio, benchmark vs desktop search and OpenAI-like embedding pipelines.
