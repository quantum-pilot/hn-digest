# Tokenomics: Quantifying Where Tokens Are Used in Agentic Software Engineering

- Score: 165 | [HN](https://news.ycombinator.com/item?id=48430923) | Link: https://arxiv.org/abs/2601.14470

- TL;DR  
    - The paper measures where tokens are actually spent inside an LLM-based multi-agent software engineering workflow (ChatDev with a GPT‑5 reasoning model). Across 30 SDLC tasks, most tokens are burned not on initial code generation but on iterative code review and refinement, which account for about 59% of usage. Input tokens dominate overall (≈54%), highlighting inefficiencies from repeatedly re-sending context between agents. The authors propose that optimizing collaboration protocols and context management, not just models, is key to controlling costs and emissions.

- LLM perspective  
    - View: Treat token usage as a first-class metric in agent workflow design, similar to latency and test coverage.  
    - Impact: Teams running multi-agent coding bots at scale; platform providers pricing and throttling long-running “review” loops.  
    - Watch next: Benchmarks comparing single-agent vs multi-agent SDLC flows, with per-stage token, latency, quality, and defect-rate tradeoff curves.
