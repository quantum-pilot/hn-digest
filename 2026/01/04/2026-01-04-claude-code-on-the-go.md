# Claude Code On-the-Go

- Score: 175 | [HN](https://news.ycombinator.com/item?id=46491486) | Link: https://granda.org/en/2026/01/02/claude-code-on-the-go/

### TL;DR
A developer runs six parallel Claude Code agents entirely from an iPhone by SSH-ing into a pay-per-use Vultr VM over Tailscale, using mosh and tmux for resilient, persistent sessions. A hook in Claude Code triggers webhooks to Poke, sending push notifications whenever the agent needs input, enabling asynchronous, “micro-moment” development (coffee line, train, couch). HN responses range from enthusiasm for the mobility and infrastructure tricks to concern that this normalizes 24/7 white‑collar work and deeper dependence on LLMs.

---

### Comment pulse
- Always-on coding risks 24/7 expectations → LLMs plus mobile dev could erase work–life boundaries under current capitalist incentives — counterpoint: individuals can still enforce boundaries.  
- Many prefer simpler stacks → Claude mobile app with permissive environments or home machine + Tailscale offer similar benefits without custom hooks and infra.  
- Ecosystem emerging → Others are building multiplexed, containerized Claude servers, web UIs, and clever hacks (file paste, ttyd, speech-to-text) to improve mobile/remote workflows.

---

### LLM perspective
- View: This pattern reframes LLM coding as background “batch work” punctuated by brief human decisions, not continuous pairing.  
- Impact: Benefits solo devs, freelancers, and on-call engineers who can move work into idle moments without carrying a laptop.  
- Watch next: Native “mirror” mobile clients for dev agents, standardized notification hooks, and better ergonomic input (voice, tiny laptops, hardware keyboards).
