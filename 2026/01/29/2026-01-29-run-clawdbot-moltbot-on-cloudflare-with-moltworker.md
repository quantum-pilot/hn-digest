# Run Clawdbot/Moltbot on Cloudflare with Moltworker

- Score: 138 | [HN](https://news.ycombinator.com/item?id=46810828) | Link: https://blog.cloudflare.com/moltworker-self-hosted-ai-agent/

- TL;DR  
  - Cloudflare’s Moltworker is an open-source wrapper that runs the Moltbot personal AI agent on Cloudflare instead of a local Mac mini, wiring it through Sandboxes/Containers, R2 storage, Browser Rendering, AI Gateway, and Zero Trust Access. It’s pitched as a proof‑of‑concept blueprint for secure, observable, always‑on agents, costing at least a $5 Workers plan. HN readers like the platform improvements but question the marketing, security and privacy trade‑offs, and whether this beats simpler local or DIY setups.

- Comment pulse  
  - Marketing skepticism → commenters see hype driven by LinkedIn-type grifters and memecoins, not engineers — counterpoint: project author is wealthy, open-sourcing it “for fun.”  
  - Security risk focus → Moltbot’s many integrations and filesystem access look like a future supply‑chain hole; prior plugin compromises and low threat awareness amplify worries.  
  - Cloud vs local → people want Cloudflare cost breakdowns; some praise Workers’ smooth Node.js deployments, while others reject any setup where data leaves home.

- LLM perspective  
  - View: This patterns a generic “agent host” stack: managed containers, storage, browser automation, auth, and gatewayed LLMs under one umbrella.  
  - Impact: Best for startups or teams wanting always‑on, isolated agents; less appealing to users demanding local‑only control and minimal vendors.  
  - Watch next: Real benchmarks, invoices, hardening guides, and upstream Moltbot integrations will reveal if this becomes design pattern or demo.
