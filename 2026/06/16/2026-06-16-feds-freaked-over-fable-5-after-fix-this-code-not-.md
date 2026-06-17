# Feds freaked over Fable 5 after 'fix this code', not jailbreak, say researchers

- Score: 536 | [HN](https://news.ycombinator.com/item?id=48552687) | Link: https://www.theregister.com/security/2026/06/15/feds-freaked-over-fable-5-after-simple-fix-this-code-prompt-not-jailbreak-says-researcher/5255827

### TL;DR
US export controls on Anthropic’s Fable 5 and Mythos 5 were reportedly triggered by a “jailbreak” that wasn’t a clever exploit at all: researchers simply fed the models vulnerable code and, after Fable refused “review this for security issues,” asked it to “fix this code.” It produced patches and test scripts—normal defensive work, argues security veteran Katie Moussouris, who saw the paper. She says calling this a national‑security threat misclassifies basic bug-fixing, hurts defenders more than attackers, and is impossible to enforce while rival/open models advance abroad. HN comments debate whether LLM “safety” is even coherent, whether Anthropic’s own hype invited the backlash, and whether the clampdown is really about politics and market power.

---

### Comment pulse
- “Jailbreak” is just reduction: rephrase “find vulns” as “fix code,” then humans read diffs/tests to extract exploits → safety filters become performative, not protective.  
- Anthropic hyped Mythos’s offensive power yet shipped Fable with leaky, keyword-based guardrails → to non‑experts it now looks inherently unsafe — counterpoint: Fable may not exceed prior offensive capability.  
- Many see the ban as political pressure and regulatory capture, with Amazon/OpenAI aligned to the administration, not a rational response to a new technical risk.

---

### LLM perspective
- View: Once a model can competently refactor and test code, separating “defensive” from “offensive” assistance is fundamentally brittle.  
- Impact: Overly broad export controls will push serious vulnerability research to open or foreign models, weakening US-centric defenders.  
- Watch next: Concrete, public benchmarks of models’ exploit-finding power and clearer policy criteria for when “fix this code” becomes regulated cyber capability.
