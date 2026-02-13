# Improving 15 LLMs at Coding in One Afternoon. Only the Harness Changed

- Score: 529 | [HN](https://news.ycombinator.com/item?id=46988596) | Link: http://blog.can.ac/2026/02/12/the-harness-problem/

### TL;DR
The post argues that coding performance depends as much on the “harness” (tools, edit protocol, state management) as on the LLM itself. The author introduces “hashline” edits: every line is returned with a tiny content hash, and edits reference these hashes instead of reproducing exact text or diffs. In a React bug-fix benchmark across 16 models, this cut patch failures and massively boosted weaker models’ pass rates, showing that better harness design can rival model upgrades—while vendors increasingly lock down third‑party harnesses.

---

### Comment pulse
- Harness as part of “the AI” → System = model + tools + context management; careful harness design can unlock GPT‑4‑level gains without new training.  
- Effect size skepticism → Benchmark is narrow and self-devised; real-world efficiency gains may be modest, and the author’s tone oversells results — counterpoint: token reductions of 25–50% look meaningful.  
- Go beyond text diffs → Represent code as ASTs / semantic trees (e.g., OpenRewrite); let agents edit structured programs directly for far more reliable transformations.

---

### LLM perspective
- View: Treat edit protocols, tooling, and context strategy as first-class levers; benchmark them like models.  
- Impact: Tool builders and IDE vendors can get “free upgrades” for many models, especially weaker or local ones.  
- Watch next: Standardize hashline/ID-based edits, add AST-level tools, and re-run public suites (SWE-bench, Diff-XYZ) under improved harnesses.
