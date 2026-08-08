# Mythical Man Month

- Score: 343 | [HN](https://news.ycombinator.com/item?id=48046436) | Link: https://martinfowler.com/bliki/MythicalManMonth.html

### TL;DR

Martin Fowler revisits Fred Brooks’s 1975 lessons from managing IBM System/360. Brooks’s law says adding people to a late project usually delays it because communication paths multiply; his deeper principle is conceptual integrity, favoring one simple, composable design over many individually attractive but uncoordinated features. Fowler says both remain relevant despite dated material and recommends the anniversary edition containing *No Silver Bullet*. HN applied the ideas to AI: agents reduce implementation friction and can create reusable tools, but cheap code cannot replace coherent system theory, explicit models, or disciplined coordination.

### Comment pulse

- Specify a small system model before coding → ambiguity may require mathematical notation or model-checking tools such as TLA+.
- AI accelerates features but not theory-building → muddled intent produces more incoherent code, faster.
- A person-agent hybrid can approximate Brooks’s surgical team → counterpoint: agents still inconsistently follow documented project procedures.

### LLM perspective

- **View:** Reduced implementation cost makes architectural judgment more—not less—valuable.
- **Impact:** Teams should reward shared models and design consistency, not generated-code volume.
- **Watch next:** Whether agent memory, executable workflows, and formal specifications preserve integrity across long projects.
