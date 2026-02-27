# I don't know how you get here from “predict the next word”

- Score: 162 | [HN](https://news.ycombinator.com/item?id=47162059) | Link: https://www.grumpy-economist.com/p/refine

### TL;DR

Economist John Cochrane tried Refine, an AI tool for deep reviewing academic papers, on his 80‑page booklet on inflation and was stunned: it surfaced core arguments, logical tensions (e.g., FTPL vs New Keynesian regimes, interest-rate transmission, monetarist alternatives), and even algebra errors at “top 5% referee report” quality. He predicts AI will reshape refereeing, editing, and coding workflows, but later worries about “LLM capture,” where whatever stance dominates the models’ training data could steer economic consensus. HN discusses how such behavior emerges from “next token prediction,” large training corpora, and multi-pass pipelines, and where current models still fall short of true “understanding.”

---

### Comment pulse

- It’s not magic → rich training data plus expensive, multi-pass workflows over a single document can produce far deeper analysis than one-shot long-context prompts.  
- “Predict the next token” is mathematically equivalent to predicting longer spans → in practice, models learn to model whole documents, not just local word transitions.  
- Debate over understanding → some see emerging “mental models”; others point to logical failures and math errors as evidence of shallow pattern-matching.

---

### LLM perspective

- View: Domain-specific critique tools like Refine show that orchestration and workflow matter as much as raw model quality.  
- Impact: Academic reviewing, grant panels, and technical editing will likely standardize AI pre-screens, changing what human experts focus on.  
- Watch next: Independent audits of domain tools’ biases, plus multi-paradigm “ensembles” to avoid single-school capture in fields like macroeconomics.
