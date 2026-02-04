# Coding assistants are solving the wrong problem

- Score: 162 | [HN](https://news.ycombinator.com/item?id=46866481) | Link: https://www.bicameral-ai.com/blog/introducing-bicameral

### TL;DR
AI coding assistants look impressive in demos but often don’t improve real-world delivery: they rely on precise requirements, happily code through ambiguity, and push undiscovered edge cases into sprawling, brittle changes. The true bottleneck isn’t typing code—only ~16% of dev time—but aligning business intent, architecture, and constraints. The article argues we need tools that analyze existing systems, surface state-machine/data-flow/service impacts during product discussions and reviews, and help humans reason under uncertainty, rather than bots that just emit more code.

---

### Comment pulse
- AI as power tool → Experienced devs use LLMs to tackle unfamiliar stacks and side projects faster, but only safely because they can judge and correct results.  
- AI needs stable specs → Works when business processes are well-defined; in fuzzy domains it uncritically encodes bad workflows, creating expensive downstream fixes — counterpoint: careful prompting can force design discussion first.  
- Perceived vs real speed → Chatting with AI feels productive, like ORMs did early on, but hidden complexity, reviews, and rework can erase or reverse time savings.

---

### LLM perspective
- View: The real opportunity is “requirements/architecture copilots” that expose gaps and impacts, not general-purpose vibe coders.  
- Impact: Product managers, architects, and senior devs gain leverage; junior devs get clearer contexts instead of opaque auto-generated patches.  
- Watch next: Field trials of tools that overlay state machines and data flows onto specs, measured by defect rates, rework, and tech-debt growth.
