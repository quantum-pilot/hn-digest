# A sufficiently detailed spec is code

- Score: 588 | [HN](https://news.ycombinator.com/item?id=47434047) | Link: https://haskellforall.com/2026/03/a-sufficiently-detailed-spec-is-code

### TL;DR
- The author argues that claims about “agentic coding” building systems from natural-language specs are misleading: to be precise enough, the spec inevitably turns into pseudo-code.  
- OpenAI’s Symphony “SPEC.md” is used as a case study: it embeds schemas, algorithms, even literal code, yet still fails to generate a correct Haskell implementation via an LLM and exhibits flaky behavior.  
- Two misconceptions are targeted: that specs are easier than code, and that spec-writing is naturally more thoughtful; under speed/outsourcing incentives, you just get sloppier, code-shaped documents.  

---

### Comment pulse
- LLMs can interpolate missing code details from terse prompts → works for small, common tasks; fails reliably for complex, novel requirements—counterpoint: “reliably” is doing too much work there.  
- Brooks’ “No Silver Bullet” echoed → fully detailed specs are essentially code; vibe-coding fits CRUD/to‑do apps but collapses for unique or correctness-critical software.  
- Spec as envelope of valid programs → crafting it is often harder than a single implementation, especially for performance and security, which specs rarely exhaustively capture.  

---

### LLM perspective
- View: Treat “spec → system” as aspirational; today’s sweet spot is “spec + code → faster human iteration,” not full automation.  
- Impact: Teams must budget for better specs, tests, and review when adopting agents, or they just industrialize slop.  
- Watch next: Rigorous benchmarks of spec-to-implementation conformance, plus tools marrying formal methods with LLMs for constrained synthesis.
