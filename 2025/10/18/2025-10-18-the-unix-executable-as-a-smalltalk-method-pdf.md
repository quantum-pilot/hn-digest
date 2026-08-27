# The Unix Executable as a Smalltalk Method [pdf]

- Score: 134 | [HN](https://news.ycombinator.com/item?id=45623917) | Link: https://programmingmadecomplicated.wordpress.com/wp-content/uploads/2025/10/onward25-jakubovic.pdf

### TL;DR

Joel Jakubovic proposes mapping Unix files to Smalltalk objects, directories to object graphs, executables to methods, and processes to method activations. This “Smalltix” framing aims to recover Smalltalk’s persistence, live updating, uniformity, and open tooling without isolating programs inside one language-specific image and VM. The obvious obstacle is process overhead when methods become tiny executables, though the paper sketches possible workarounds. Commenters connected the proposal to earlier Unix/PARC integrations, Stephen Kell’s work, and ambitions for malleable operating systems.

### Comment pulse

- The mapping inspired system-design experiments → readers saw a route toward componentized, inspectable environments on Unix foundations.
- Historical precedents matter → commenters cited Interlisp, Cedar, NeXTSTEP, and prior attempts to carry PARC ideas into Unix.

### LLM perspective

- View: The proposal’s strength is conceptual interoperability; its feasibility depends on collapsing process and storage overhead.
- Impact: Success could bring live, cross-language development closer to ordinary filesystem and executable tooling.
- Watch next: Build a prototype measuring activation latency, persistence costs, debugging ergonomics, and multi-language composition.
