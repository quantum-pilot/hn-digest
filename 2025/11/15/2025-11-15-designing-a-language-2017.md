# Designing a Language (2017)

- Score: 162 | [HN](https://news.ycombinator.com/item?id=45935342) | Link: https://cs.lmu.edu/~ray/notes/languagedesignnotes/

### TL;DR

These course notes frame programming-language design as an iterative loop connecting intended capabilities, abstract syntax, concrete syntax, formal definition, prototyping, and implementation feedback. They urge designers to study paradigms, language concepts, existing languages, and users before selecting features. Extensive checklists expose decisions around types, functions, control flow, concurrency, reflection, and syntax, while examples show how progressively richer teaching languages exercise compiler construction. The central lesson is that coherent tradeoffs and repeated testing matter more than accumulating fashionable features.

### Comment pulse

- Readers stressed having a clear design philosophy, including strong convictions about which features do not belong.
- Several defended toy languages as valuable learning exercises even when they are never intended for production adoption.

### LLM perspective

- View: A language’s exclusions reveal its design more clearly than a long feature inventory.
- Impact: Iterating from user goals through syntax and implementation exposes incoherence before it becomes permanent complexity.
- Watch next: Prototype programs should test the language’s hardest semantic choices, not merely demonstrate pleasant syntax.
