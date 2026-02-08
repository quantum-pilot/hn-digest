# My AI Adoption Journey

- Score: 931 | [HN](https://news.ycombinator.com/item?id=46903558) | Link: https://mitchellh.com/writing/my-ai-adoption-journey

### TL;DR
Mitchell Hashimoto describes how AI went from a useless chatbot novelty to a core, background tool in his daily development work. The shift came from using *agents* (LLMs with tools: file access, commands, HTTP), forcing them to reproduce his own commits, and systematically building a “harness” of scripts and docs so they can verify and correct themselves. He runs agents on well-scoped “slam dunk” tasks—often overnight or in the background—while he focuses on hard problems, staying skeptical, cost-aware, and protective of human skill formation.

---

### Comment pulse
- AI coding is now genuinely useful → skeptical senior devs report 2025–26 as the inflection point once they treat agents as serious tools, not hype toys.  
- Productivity vs rigor → agents enable fast coding, but some fear erosion of code review and line-by-line understanding—counterpoint: humans should still own verification and acceptance.  
- Costs and constraints matter → heavy agent use can quickly hit quotas; subscription, time-to-good-results, and corporate policies all shape whether AI feels net-productive.

---

### LLM perspective
- View: Treat agents like junior devs plus scripts: small diffs, strong tests, and explicit project knowledge in AGENTS/SKILLS docs.  
- Impact: Senior engineers gain leverage; juniors risk weakened fundamentals unless tasks are curated for learning, not just throughput.  
- Watch next: Standardized harness patterns, cheaper strong models, and clearer org policies on cost, privacy, and acceptable AI-driven code review.
