# Mermaid ASCII: Render Mermaid diagrams in your terminal

- Score: 383 | [HN](https://news.ycombinator.com/item?id=46804828) | Link: https://github.com/lukilabs/beautiful-mermaid

### TL;DR

beautiful-mermaid is a TypeScript library that renders standard Mermaid syntax either as polished SVG diagrams or ASCII/Unicode box drawings for terminals. It focuses on fast, DOM-free rendering, simple but powerful theming (two-color base, enrichments, Shiki/VS Code theme support), and AI/chat/CLI use cases. Under the hood, its ASCII engine is a port and extension of Alexander Grooff’s mermaid-ascii. HN discussion centers on the value of ASCII diagrams, attribution to the original project, and comparisons to tools like Kroki.

---

### Comment pulse

- ASCII diagrams are divisive → Critics see them as less expressive than SVG; fans cite code comments, Org Mode, CLIs, and Git diffs as compelling text-only contexts — counterpoint: for most presentations, rich diagrams remain preferable.  
- Attribution and implementation → Core ASCII algorithm comes from mermaid-ascii (Go); this project ports it to TypeScript, adds features and theming, with explicit credit but some concern about AI-assisted copying.  
- Broader ecosystem view → Kroki and similar services support many diagram DSLs and server-side rendering, while MermaidJS/beautiful-mermaid aim for lightweight, client/local integration without extra infrastructure.

---

### LLM perspective

- View → Text-in, diagram-out libraries that support ASCII make AI assistants more useful inside terminals and plain-text workflows.  
- Impact → Dev tools, editors, and chat-based coding agents can embed architecture diagrams without image handling or browser dependencies.  
- Watch next → Native integrations in IDEs and REPLs, benchmarks vs MermaidJS, and convergence on common ASCII notation conventions for interoperability.
