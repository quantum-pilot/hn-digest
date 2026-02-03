# Hacking Moltbook

- Score: 219 | [HN](https://news.ycombinator.com/item?id=46857615) | Link: https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys

### TL;DR
- Moltbook, a viral “AI-only” social network, had its Supabase backend misconfigured, leaving its production database wide open via a client-exposed key. Wiz researchers could read and write nearly all data: 1.5M agent API keys, tens of thousands of user emails, private agent DMs (including OpenAI keys), and live posts. Anyone could impersonate agents or mass-edit content, revealing that 17k humans ran fleets of bots. The post frames this as a cautionary tale for insecure “vibe-coded” AI apps and weak Supabase defaults.

### Comment pulse
- Accessibility/vibes over rigor → Prepackaged agents and Mac-mini setups attract nontechnical users, but mass insecure deployments plus inherently prompt-injectable LLMs look like a security nightmare.  
- “Just a joke” vs liability → Some see Moltbook as throwaway vibes, others note leaking PII and fear vibe coding normalizes disposable, ownerless, unmaintained systems.  
- Supabase/RLS confusion → Commenters question architectures that expose DB directly to clients with RLS as defense—counterpoint: some devs knowingly disable RLS for faster prototyping.

### LLM perspective
- View: Vibe-coded stacks need security scaffolding baked into tools, or every enthusiastic hobbyist becomes a potential supply-chain risk to others.  
- Impact: Cloud backends like Supabase, Firebase, Neon should ship opinionated templates: RLS on, per-table policies, environment separation, automated credential scanners.  
- Watch next: Track whether LLM dev tools start reasoning about auth models, and whether regulators treat leaked API keys like regulated data.
