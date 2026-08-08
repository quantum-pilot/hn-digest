# Kitesurf: Agent-first browser that runs in V8 isolates

- Score: 157 | [HN](https://news.ycombinator.com/item?id=49208393) | Link: https://blog.cloudflare.com/kitesurf/

### TL;DR

Cloudflare introduced Kitesurf, a browser built specifically for agents and running entirely on Workers, free during Browser Run’s beta. It targets lower CPU and memory use than Chromium for screenshots and HTML extraction by omitting human-facing priorities and isolating untrusted pages. A stateful Engine exposes Chrome DevTools Protocol compatibility; per-page PageScript isolates execute DOM, JavaScript, and WebAssembly; disposable PageRenderer workers produce images or PDFs. Rust, WebAssembly, Blitz, Stylo, restricted outbound networking, and RPC underpin the design. Kitesurf already passes more than 215,000 Web Platform Tests.

### Comment pulse

- Blitz’s author said Cloudflare intends to open-source and upstream its patches, and requested standardized WebDriver BiDi support.
- Users cited grocery carts, hostile admin interfaces, receipt searches, product comparisons, translation, and visual research as practical agent-browser tasks.
- Critics questioned Cloudflare operating both anti-bot infrastructure and agent browsers — counterpoint: Browser Run traffic is identified and cryptographically signed as bot traffic.

### LLM perspective

- View: Agent browsers can trade rendering polish for isolation, structured access, scale, and lower cost.
- Impact: CDP compatibility lets existing automation clients adopt the new engine without workflow rewrites.
- Watch next: Real-site compatibility, security under hostile pages, WebDriver BiDi, and delivery of promised open-source patches.
