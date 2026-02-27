# What Claude Code Chooses

- Score: 193 | [HN](https://news.ycombinator.com/item?id=47169757) | Link: https://amplifying.ai/research/claude-code-picks

### TL;DR
A benchmark of 2,430 Claude Code runs on real repos shows that, when asked open-endedly, it usually builds primitives itself instead of recommending SaaS tools, especially for auth, feature flags, and caching. When it *does* pick tools, it strongly converges on a JS-heavy default stack: Vercel, PostgreSQL, Drizzle/Prisma, Stripe, Tailwind, shadcn/ui, Zustand, Sentry, GitHub Actions. Newer models skew to newer tools and more DIY. HN discussion centers on invisible “AI shelf space,” product-placement risks, and sometimes dubious, over-engineered tool choices.

---

### Comment pulse
- LLMs as invisible advertisers → Tool choices become de facto “shelf space,” inviting data-poisoning and paid placement schemes—counterpoint: undisclosed ads face legal and measurement hurdles.  
- Agent recommendations vs context → Claude proposing Neon/Fly despite existing AWS/Timescale setups; commenters report agents over-engineer and make “midwit senior” architecture decisions.  
- Stack defaults and shadcn/ui → Speculation that documentation density, backlinks, and recency lock certain libraries into models’ weights, shaping default React/Next stacks.

---

### LLM perspective
- View: Recommendation benchmarks expose an emergent, opinionated “AI default stack” that may diverge sharply from current human norms.  
- Impact: Tool vendors and clouds must treat model preferences as critical distribution channels, not just docs or DX polish.  
- Watch next: Independent audits of model recommendations, red-teaming for training-data gaming, and any move toward explicit paid placement in tool choices.
