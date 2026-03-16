# Chrome DevTools MCP

- Score: 271 | [HN](https://news.ycombinator.com/item?id=47390817) | Link: https://developer.chrome.com/blog/chrome-devtools-mcp-debug-your-browser-session

### TL;DR
Chrome DevTools MCP now lets AI coding agents attach directly to your *already-open* Chrome session, reusing your logged‑in state and active DevTools context. With Chrome 144’s updated remote debugging flow and a new `--autoConnect` flag, agents can inspect selected elements or network requests, then run tasks via tools like Gemini CLI. The browser prompts for each debug session and shows an automation banner. HN discussion compares this to Playwright/CLI workflows, debates whether MCP is “dead,” and raises strong security and token‑cost concerns.

---

### Comment pulse
- Many power users prefer Playwright + headless Chrome and custom CLIs → more control, lower token use, no MCP overhead — counterpoint: MCP helps centralize auth, RBAC, and ops in enterprises.  
- Several independent tools already give agents DOM/CDP access (chrome-cdp-skill, browserbox) → flexible but “duct-taped,” with serious prompt‑injection and full‑session‑exposure risks.  
- Some call Gemini CLI awful and MCP obsolete; others at/near Google say both are widely used internally and improving, especially with centralized MCP services.

---

### LLM perspective
- View: For day‑to‑day debugging, attaching agents to your real, logged‑in session is a big usability step over synthetic profiles.  
- Impact: Frontend and full‑stack devs get hybrid manual/agent workflows; enterprises gain a sanctioned path for browser‑automation agents.  
- Watch next: Better safety rails for prompt injection, richer panel data exposure, and benchmarks vs Playwright‑style agent stacks on reliability and cost.
