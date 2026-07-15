# Bonsai 27B: A 27B-Class model that runs on a phone

- Score: 373 | [HN](https://news.ycombinator.com/item?id=48910545) | Link: https://prismml.com/news/bonsai-27b

- TL;DR  
    - PrismML’s Bonsai 27B compresses a Qwen 3.6 27B model into 5.9GB (ternary) and 3.9GB (1‑bit), small enough for laptops and iPhone‑class phones while retaining ~90–95% of full‑precision performance across math, coding, tool use, and vision benchmarks. It’s trained natively at low precision with group‑wise FP16 scaling, maximizing “intelligence per GB” for long‑context, on‑device agents. HN discussion centers on comparisons with Gemma 4 12B QAT, concerns over evaluation fairness, and early runtime/tooling issues.

- Comment pulse  
    - Gemma 4 12B QAT vs Bonsai → Bonsai wins math/coding, worse on vision; thread digs into 4‑bit vs 1‑bit tradeoffs and quantization nuances.  
    - Methodology skepticism → one reader fears cherry‑picked benchmarks; others explain Bonsai is trained natively in 1‑bit/ternary with FP16 group scaling, not post‑training quantized.  
    - Real‑world feel → demo recipe/macro answer seems weak; some doubt local AI’s value for trivia — counterpoint: offline, private, multimodal agents genuinely require on‑device models.

- LLM perspective  
    - View: Native low‑bit training at this scale shifts what consumer devices can host, especially for agentic workflows and long‑context tasks.  
    - Impact: If tooling matures, laptop/phone‑grade hardware could handle most everyday AI work, reserving expensive frontier models for rare, hardest calls.  
    - Watch next: Independent benchmarks, Gemma/Qwen comparisons, and mature open‑source runtimes will decide whether Bonsai‑style models become a common on‑device stack.
