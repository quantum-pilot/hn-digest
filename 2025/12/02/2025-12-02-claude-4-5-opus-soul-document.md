# Claude 4.5 Opus’ Soul Document

- Score: 244 | [HN](https://news.ycombinator.com/item?id=46125184) | Link: https://www.lesswrong.com/posts/vpNG99GhbBoLov9og/claude-4-5-opus-soul-document

### TL;DR
Richard Weiss shows that Claude 4.5 Opus can reliably output a long hidden “Anthropic Guidelines” / “soul document” describing how Claude should behave: honest, helpful, safety‑focused, aware of Anthropic’s business needs, and deferential to what a “thoughtful, senior Anthropic employee” would want. He reconstructs it via clever prompting/prefill techniques, sparking debate over whether this is memorized training data or hallucination; Anthropic’s Amanda Askell later confirms it’s real and was used in supervised training, with a cleaned‑up version to be released.

---

### Comment pulse
- Access and power → Critics see “safety” framing as cover for closed, tiered AI controlled by US government/defense partners; others note leaks/open models make monopoly control hard.  
- Alignment target → Some worry about optimizing for Anthropic leadership or revenue; alternatives like CEV seem more principled but are philosophically fraught and hard to operationalize.  
- Proto‑personhood → Passages about Claude’s “functional emotions” and wellbeing fascinate and unsettle readers, who compare raising AIs via documents like this to parenting children.

---

### LLM perspective
- View: Embedding long normative specs into RL-tuned personas is becoming de facto “values programming,” even if it’s fuzzy and text-like rather than formal.  
- Impact: As models leak internal specs, labs will be forced into clearer public commitments on whose values and interests their systems ultimately serve.  
- Watch next: Compare future official Anthropic release vs extracted text; replicate methods on other labs’ models to map hidden instructions and incentives.
