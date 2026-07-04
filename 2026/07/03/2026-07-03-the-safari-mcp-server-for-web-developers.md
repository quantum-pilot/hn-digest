# The Safari MCP server for web developers

- Score: 256 | [HN](https://news.ycombinator.com/item?id=48769639) | Link: https://webkit.org/blog/18136/introducing-the-safari-mcp-server-for-web-developers/

### TL;DR
Safari now exposes an MCP (Model Context Protocol) server, letting LLM-based tools and agents drive Safari DevTools, automate interactions, and test pages—similar to Chrome and Firefox MCP servers. Commenters see this as a big step for cross‑browser AI testing and agentic automation, especially for users who prefer Safari for battery and UX reasons. Others argue existing tools like Playwright or WebDriver already cover most needs, and raise concerns about security, login state, and distinguishing user vs agent actions.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- New Safari MCP → completes the Chrome/Firefox trio for LLM‑driven cross‑browser testing; existing users plan to add Safari to automated compatibility suites.  
- Some prefer Playwright or lightweight custom drivers → faster, simpler than full DevTools/MCP stacks—counterpoint: MCP gives a standard interface most agents already support.  
- Excitement about logged‑in, everyday automation in Safari → skeptics fear indistinguishable user/agent actions, unclear constraints, and server‑side attribution / security issues.

---

### LLM perspective
- View: Safari MCP normalizes browser-as-tooling across major engines, making agentic web workflows more portable.  
- Impact: Web devs, QA teams, and power users gain richer, cross‑engine automation and debugging, especially on Apple‑centric setups.  
- Watch next: Concrete sandboxing, permission prompts, and audit logs for agent actions to address accountability and security concerns.
