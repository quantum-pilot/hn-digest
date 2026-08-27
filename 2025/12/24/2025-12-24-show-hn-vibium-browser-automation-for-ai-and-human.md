# Show HN: Vibium – Browser automation for AI and humans, by Selenium's creator

- Score: 200 | [HN](https://news.ycombinator.com/item?id=46377597) | Link: https://github.com/VibiumDev/vibium

### TL;DR

Vibium packages browser lifecycle, a WebDriver BiDi proxy, and an MCP server into a roughly 10MB Go binary, with synchronous and asynchronous JavaScript APIs layered above it. Installation downloads Chrome automatically, and V1 exposes navigation, CSS-based finding, clicks, typing, screenshots, and visible-by-default sessions across major desktop platforms. HN welcomed Selenium creator Jason Huggins’s return and the zero-setup goal, but found the current agent surface too narrow: JavaScript evaluation, DOM mutation, network interception, accessibility discovery, Python, and Java remain absent or planned.

### Comment pulse

- Developer experience → Vibium adopts Playwright’s fast, approachable automation model while using standardized WebDriver BiDi.
- Capability gap → agents cannot reliably derive selectors from screenshots, inspect accessibility structure, or intercept network traffic yet.
- Adoption path → Selenium’s installed base may welcome an agentic bridge — counterpoint: Playwright already offers mature multi-language automation.

### LLM perspective

- View: Zero setup is compelling, but autonomous browsing depends more on observability and actionability than minimal command count.
- Impact: Early users get simple scripted flows; complex debugging and resilient agent navigation still require established tools.
- Watch next: Evaluate-tool support, accessibility locators, network controls, non-JavaScript clients, cross-platform reliability, and comparative benchmarks.
