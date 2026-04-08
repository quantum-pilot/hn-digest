# Claude Code is locking people out for hours

- Score: 215 | [HN](https://news.ycombinator.com/item?id=47676521) | Link: https://github.com/anthropics/claude-code/issues/44257

### TL;DR

Claude Code had a widespread outage where OAuth logins (often via Google) failed with timeouts and 500s across Windows, macOS, Linux, WSL, and VS Code. The issue was tied to Anthropic’s authentication service and, for some, to using Opus 4.6 (1M) as the default model; Anthropic later marked it resolved, but some users were locked out for hours. HN discussion focuses less on the bug itself and more on: fragile dependence on subscription LLM tools, Anthropic’s chronic-looking outages and capacity limits, unclear pricing/usage economics, and even the HN post’s clickbaity retitle.

---

### Comment pulse

- Growing reliance on subscription LLM dev tools → mix of enthusiasm (coding “superpowers”) and skepticism; some see employer pressure to use branded AI as a hiring filter.  
- Anthropic capacity strain → users suspect a shared “compute pool” for Claude Max, visible quality degradation, rapid ARR growth, and nearly daily status incidents—counterpoint: they’re deliberately avoiding OpenAI-scale burn.  
- Pricing and predictability → calls to “just pay for API tokens” meet pushback about opaque token costs, subsidized/predatory flat pricing, and comparisons to GitHub Copilot’s far friendlier economics.  
- Meta concern → some object that the HN title is sensationalized versus the original specific GitHub bug report.

---

### LLM perspective

- View: Treat cloud LLMs like any external dependency: design graceful degradation paths and keep non-LLM workflows viable.  
- Impact: Teams deeply tied to Claude Code should budget for outages, model switches, and potential price hikes in planning and SLAs.  
- Watch next: Postmortems, clearer status reporting, and more transparent token/pricing dashboards from Anthropic and competitors.
