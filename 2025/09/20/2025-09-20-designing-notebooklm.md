# Designing NotebookLM

- Score: 140 | [HN](https://news.ycombinator.com/item?id=45315312) | Link: https://jasonspielman.com/notebooklm

### TL;DR

NotebookLM’s design organizes source-grounded work as Inputs → Chat → Outputs, using three responsive panels for references, conversation, and artifacts such as notes, study guides, and Audio Overviews. The designer describes rapid iteration, inline citations added from user feedback, and chat as a familiar bridge toward more dynamic AI interfaces. Commenters disputed whether the result remained simple: some praised its learning value, while others found the interface low-density, confusing, and increasingly cramped as features accumulated, especially on small screens and within narrow note panels.

### Comment pulse

- The three-panel model preserves context → sources, cited answers, and writing remain visible without constant tab switching.
- Feature growth strains the layout → large artifact controls and fixed-width notes can crowd out core work on smaller devices.
- Visual polish divided readers → supporters saw thoughtful exploration; critics felt cards, scrolling, and hierarchy obscured a simple workflow.

### LLM perspective

- View: A scalable architecture must support removing or collapsing interface weight, not merely adding new artifacts.
- Impact: Researchers gain integrated synthesis, while dense controls can exclude small-screen users and obscure source work.
- Watch next: Measure panel usage, mobile breakpoints, note readability, feature discoverability, and time to complete source-grounded tasks.
