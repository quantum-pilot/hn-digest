# Show HN: Vibium – Browser automation for AI and humans, by Selenium's creator

- Score: 200 | [HN](https://news.ycombinator.com/item?id=46377597) | Link: https://github.com/VibiumDev/vibium

## TL;DR
Vibium is a new browser-automation stack from Selenium’s creator, aimed at both humans and AI agents. A small Go “Clicker” binary manages Chrome via WebDriver BiDi and exposes an MCP server, while a JS/TS client offers simple sync/async APIs (`npm install vibium` handles binaries and Chrome setup automatically). It currently covers core actions (launch, navigate, find, click, type, screenshot). HN discussion centers on how it compares to Playwright, missing power features (JS injection, network interception), and its role as a modern bridge for Selenium’s huge installed base.

---

## Comment pulse
- Playwright vs Selenium vs Vibium → Playwright leads in DX now, but Selenium remains globally entrenched; Vibium aims to be Selenium users’ upgrade path to agentic automation.  
- Missing power features → No JS injection, DOM mutation, or network interception yet, but they’re explicitly on the roadmap—counterpoint: many users need network monitoring from day one.  
- Agent ergonomics → Current MCP tools are minimal; contributors are experimenting with `browser_evaluate` and accessibility-tree–based navigation to let agents reason from screenshots to actionable selectors.

---

## LLM perspective
- View: Treat Vibium as a low-friction browser backend for agents, not yet a full Playwright replacement for power users.  
- Impact: Most useful to AI tooling builders and Selenium-heavy orgs wanting a gentler, standards-based path into MCP-style agents.  
- Watch next: Arrival of Python/Java clients, JS evaluation/network hooks, and benchmarks of agent reliability versus Playwright-driven automation.
