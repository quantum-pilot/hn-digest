# Specsmaxxing – On overcoming AI psychosis, and why I write specs in YAML

- Score: 258 | [HN](https://news.ycombinator.com/item?id=47994012) | Link: https://acai.sh/blog/specsmaxxing

- TL;DR  
  Author argues that in an LLM-heavy workflow, the bottleneck is no longer typing code but specifying behavior precisely. They propose “specsmaxxing”: concise, testable acceptance criteria written in a feature.yaml format, then referenced from code via stable IDs and tracked in an open-source tool, Acai.sh, as “acceptance coverage.” This supports agentic pipelines, multi-repo features, and future reactive “software factories.” HN readers mostly agree on the renewed importance of explicit specs, while questioning effort, overlap with BDD, and LLM unpredictability.

- Comment pulse  
  - Spec-first development is resurging → durable, human-written acceptance criteria anchor LLM output, replacing lost “author memory” and echoing classic software analyst practices.  
  - Why not just code it? → Skeptics say specs equal coding; supporters argue specs encode theory and stay proprietary even if implementation becomes cheap.  
  - LLMs feel like probabilistic slot machines → some find building harnesses and specs exhausting—counterpoint: others report 5–10× productivity when pairing strict structure with expensive context.

- LLM perspective  
  - View: Spec-ID–centric tooling is a pragmatic bridge between messy prompt chats and traditional requirements engineering for AI-assisted teams.  
  - Impact: If adopted, product managers, QA, and devs could review features by requirement coverage instead of line-by-line diffs.  
  - Watch next: Worth watching: integrations with CI, test frameworks, and other spec tools to avoid duplicative YAML silos across organizations.
