# Some thoughts on LLMs and software development

- Score: 420 | [HN](https://news.ycombinator.com/item?id=45055641) | Link: https://martinfowler.com/articles/202508-ai-thoughts.html

### TL;DR

Martin Fowler offers deliberately unsettled observations on LLM-assisted development. Productivity studies should distinguish autocomplete from agents that read and edit repositories, as workflows and models differ substantially. He refuses confident job forecasts, calls AI an inevitable but unpredictably timed investment bubble, and recommends experimentation. Because model output is nondeterministic, he advises comparing repeated answers and using deterministic calculation where possible. Most urgently, agents combining private data, untrusted content, and external communication create severe prompt-injection and exfiltration risks, especially inside browsers.

### Comment pulse

- Readers disputed whether calling every output a “hallucination” clarifies model behavior or merely redefines the term.
- One team reported faster code generation but growing review and repair costs from nearly-correct output.

### LLM perspective

- View: Aggregate productivity numbers are weak evidence unless they identify workflow, model, task, and verification practice.
- Impact: Faster generation can move the bottleneck into comprehension, review, security, and long-term maintenance.
- Watch next: Measure defect escape, review load, ownership, and prompt-injection exposure alongside delivery speed.
