# Kimi K2.6 just beat Claude, GPT-5.5, and Gemini in a coding challenge

- Score: 349 | [HN](https://news.ycombinator.com/item?id=47993235) | Link: https://thinkpol.ca/2026/04/30/an-open-weights-chinese-model-just-beat-claude-gpt-5-5-and-gemini-in-a-programming-challenge/

### TL;DR
- An AI Coding Contest pitted major LLMs against each other on a real-time “Word Gem” sliding-tile puzzle, where bots had to connect to a TCP server, slide letters, and claim long English words under strict time limits.  
- Moonshot’s open-weight Kimi K2.6 won by writing a simple greedy sliding strategy that kept generating new opportunities on heavily scrambled large boards, edging out Xiaomi’s MiMo V2-Pro (static, no-slide strategy) and GPT‑5.5.  
- Some models failed on basics (syntax, protocol, or scoring interpretation), with one racking up −15k points by spamming short words, highlighting how partial task understanding can catastrophically misfire.  
- The organizer frames this as evidence that open, relatively cheap Chinese models are now close enough to frontier systems that individual tasks can flip in their favor, while HN discussion stresses the need for rigorous, repeated benchmarks and emphasizes cost, openness, and real-world workflows over single-contest bragging rights.

### Comment pulse
- Single benchmark ≠ objective ranking → one-off contests are noisy; proper comparison needs repeated runs, stats, and task-specific fine-tuning across many problems.  
- Open models like Kimi/DeepSeek feel near-Claude for coding at far lower cost, enabling heavier personal use—counterpoint: this puzzle doesn’t reflect real-world software work.  
- Open weights viewed as strategic hedge against API “enshittification” and pricing power, though some argue cloud vendors will always run any model cheaper at scale.

### LLM perspective
- View: This contest highlights how small implementation details and partial spec understanding can dominate performance in agentic coding tasks.  
- Impact: Strong open Chinese models will push prices down and encourage more regional, specialized AI stacks.  
- Watch next: Broader, statistically robust multi-task evals and real-world agent benchmarks to validate whether open weights consistently rival closed models.
