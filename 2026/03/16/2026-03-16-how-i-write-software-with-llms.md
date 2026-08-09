# How I write software with LLMs

- Score: 468 | [HN](https://news.ycombinator.com/item?id=47394022) | Link: https://www.stavros.io/posts/how-i-write-software-with-llms/

### TL;DR

Stavros Korokithakis says agents let him focus on making products rather than typing code, while retaining architectural understanding on technologies he knows. His OpenCode workflow uses a strong architect model for explicitly approved plans, a cheaper developer for implementation, and independent models to review each diff; feedback loops back or escalates. Repeated human QA catches architectural omissions and security edge cases even after tests pass. HN valued the transcript but questioned whether this ceremony beats one well-contextualized model, citing coordination cost, rapidly obsolescing scaffolds, and domain expertise as the differentiator.

### Comment pulse

- Multi-model review offers independent blind spots → same-model personas often agree — counterpoint: one experiment matched a $12 agent council for $0.30.
- Familiarity sets the ceiling → architecture stays coherent when the operator knows the domain; unfamiliar mobile work accumulated compounding bad choices.
- Validation outlasts prompting tricks → precise tasks, tests, live QA, and correct chunk size matter more than anthropomorphic role labels.

### LLM perspective

- **View:** The durable pattern is human-owned architecture plus executable feedback, not any fixed architect–developer–reviewer topology.
- **Impact:** Experienced builders can trade code reading for specification and QA; novices risk scaling mistakes they cannot recognize.
- **Watch next:** Controlled single-versus-multi-agent comparisons, total cost, escaped defects, maintenance after months, and performance as models change.
