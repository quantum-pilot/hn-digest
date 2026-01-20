# "Anyone else out there vibe circuit-building?"

- Score: 131 | [HN](https://news.ycombinator.com/item?id=46679896) | Link: https://twitter.com/beneater/status/2012988790709928305

### TL;DR
HN discusses “vibe circuit-building” with LLMs: using them not as autonomous circuit designers, but as helpers for part selection, block-level integration, and learning. One project proposes pre-validated hardware “blocks” on a fixed grid; the LLM only chooses and arranges them, guaranteeing manufacturable-by-construction prototypes. Commenters like this for quick boards but doubt it scales to dense, cost-optimized production. Overall, LLMs are seen as powerful assistants if you already understand electronics and rigorously verify their suggestions.  
*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Block-based hardware design with LLM selection → avoids hallucinated values, speeds prototyping, enforces layout rules—counterpoint: rigid modules break down when you need tight packing and cost optimization.  
- Hobbyists “vibe” with LLMs → rapid exposure to new parts and circuit ideas; accelerates learning, but analog advice and device choices are often wrong and must be checked.  
- Experts use LLMs for reviews, part hunting, napkin math, and distributor APIs → great productivity boost, yet constraint-handling is weak and board re-spins make human sign-off non-negotiable.  

---

### LLM perspective
- View: Treat circuits like software packages: human-verified hardware blocks, LLM for composition, and EDA tools enforcing electrical/layout rules.  
- Impact: Speeds early prototypes for hobbyists, firmware engineers, and mechanical teams who lack deep EE background, while preserving expert review for production.  
- Watch next: Integrated flows where LLMs talk directly to EDA/MCAD, run DRC/SI checks, and are benchmarked on “passes manufacturing without re-spin.”
