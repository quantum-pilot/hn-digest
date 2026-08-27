# Google Titans architecture, helping AI have long-term memory

- Score: 363 | [HN](https://news.ycombinator.com/item?id=46181231) | Link: https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/

### TL;DR

Google Research presents Titans, an architecture whose deep neural memory updates during inference, and MIRAS, a framework describing sequence models through memory structure, learning objective, retention, and update algorithm. Titans uses gradient-based “surprise,” momentum, and forgetting to select information for longer-term storage while retaining attention for precise short-term context. Google reports stronger results than selected transformer and recurrent baselines, including very long-context tasks, but the supplied evidence is the researchers’ own account. Commenters questioned robustness to junk inputs and the absence of official downloadable models.

### Comment pulse

- Readers debated whether surprise-based memory could be polluted by improbable junk and whether training would suppress it.
- Several welcomed open papers but contrasted them with organizations releasing usable code and weights.

### LLM perspective

- View: Test-time memory is promising, but selective retention creates a new robustness surface.
- Impact: Successful implementations could reduce long-context costs while retaining details beyond fixed recurrent states.
- Watch next: Independent reproductions, released weights, and adversarial tests of memory poisoning and forgetting.
