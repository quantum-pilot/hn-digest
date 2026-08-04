# Control the Ideas, Not the Code

- Score: 203 | [HN](https://news.ycombinator.com/item?id=48891184) | Link: https://antirez.com/news/169

### TL;DR

Antirez argues that AI-era programmers should own a system’s concepts, architecture, invariants, performance goals, and tests rather than spend scarce hours reading every generated line. Models produce too much locally competent code for exhaustive review; he would redirect that time toward QA, design exploration, optimization, and DESIGN.md files describing data structures and implementation tricks. HN readers challenged the premise: code inspection often refines the mental model and catches cascading bad assumptions, while models drift toward familiar training patterns. Supporters said strong constraints and higher-level architectural iteration can preserve intent.

### Comment pulse

- Control can decay across context → design files and interfaces get ignored after compaction, allowing duplicate variants to spread between sessions.
- Constraint design becomes core engineering → limiting frameworks and degrees of freedom can keep agents aligned, though familiar training patterns still pull strongly.
- Professional identity divided readers → some saw abstraction-level work as leverage — counterpoint: others called it technical management and feared loss of engineering craft.

### LLM perspective

- **View:** Ideas and code are not separable layers: implementation feedback changes architecture, but review depth can be allocated by risk.
- **Impact:** Senior developers move toward specification, evaluation, and failure analysis; juniors need deliberate low-level projects to build independent judgment.
- **Watch next:** Compare defect escape rates and maintenance costs across line review, model review, automated testing, and design-document-driven workflows.
