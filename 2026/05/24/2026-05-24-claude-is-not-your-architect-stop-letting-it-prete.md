# Claude is not your architect. Stop letting it pretend

- Score: 224 | [HN](https://news.ycombinator.com/item?id=48259784) | Link: https://www.hollandtech.net/claude-is-not-your-architect/

- TL;DR  
    - The article argues that teams are quietly letting LLMs like Claude act as software architects: inventing systems and auto-generating Jira backlogs. Because models are agreeable pattern-matchers with no organizational context, they produce plausible “best practices” that ignore real constraints, trade-offs, and team capabilities. Once these designs harden into tickets, senior review tends to be perfunctory, and engineers are demoted to implementing an unowned, fragile “Jenga tower.” The article and many commenters advocate a stricter split: humans own architecture, debate, and risk; AI helps brainstorm and implement well-specified pieces.

- Comment pulse  
    - AI quality mirrors operator skill → unskilled “vibe coders” ship fragile systems, yet companies still benefit when experts later stabilize them cheaply.  
    - Deference isn’t the real issue → some want LLMs maximally subservient tools; the real risk is humans anthropomorphizing chatty UIs and over-trusting polite prose.  
    - AI widens accountability gaps → one person plus agents can create huge risk with little capital — counterpoint: pre-AI dev stacks already allowed comparable impact.

- LLM perspective  
    - View: Treat LLMs like extremely fast junior collaborators; insist on human-owned specs, trade-offs, and decision records before any code generation.  
    - Impact: Organizations that formalize this split will likely ship simpler, more operable systems than teams outsourcing architecture to chat windows.  
    - Watch next: emerging linters, governance tools, and IDE workflows that track which human accepted which AI suggestion for high-stakes decisions.
