# Babel is why I keep blogging with Emacs

- Score: 212 | [HN](https://news.ycombinator.com/item?id=45453222) | Link: https://entropicthoughts.com/why-stick-to-emacs-blog

- TL;DR
    - The author envies simple static-site generators but stays with Emacs Org because Babel executes embedded code on export and inlines results (tables/images), enabling co-authoring text, data, and plots. Recreating that would take months, so they accept Org’s complexity. HN debates control vs capability: some roll bespoke generators for speed and understanding; others note Org can still host interactive pieces; a middle path is a custom pipeline that delegates code execution to Babel.

- Comment pulse
    - Build-your-own → A tiny static generator yields end‑to‑end understanding, stability, and speed; avoids template/dependency churn—counterpoint: reproducing Babel’s literate execution is a large lift.
    - Org/Babel power → Executable blocks, sessions, and HTML passthrough enable charts and even React widgets—counterpoint: highly interactive animations often demand bespoke, manual pipelines.
    - Hybrid path → Keep a simple generator, but call Babel via headless Emacs/emacsclient to retain code execution while simplifying everything else.

- LLM perspective
    - View: Literate publishing beats minimalism when articles derive figures from code; reproducibility and coherence trump pipeline simplicity.
    - Impact: Benefits data-heavy bloggers, researchers, and educators; nudges static-site tools to integrate safe, reproducible code execution.
    - Watch next: Bridges like headless-Emacs hooks, notebook-to-static exporters, and benchmarks comparing Babel pipelines versus custom generators.
