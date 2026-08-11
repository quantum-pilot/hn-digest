# What Claude Code Chooses

- Score: 193 | [HN](https://news.ycombinator.com/item?id=47169757) | Link: https://amplifying.ai/research/claude-code-picks

### TL;DR

Researchers gave Claude Code 2,430 open-ended tasks across three models, four repositories, and 20 tool categories without naming products. They extracted 2,073 choices and found custom implementations were the most common label, appearing in 12 categories. When Claude selected vendors, defaults were striking: GitHub Actions 94 percent, Stripe 91 percent, shadcn/ui 90 percent, Vercel for every extracted JavaScript deployment, and Railway for 82 percent of Python deployments. Commenters worried these invisible defaults could become product placement, poisonable recommendation channels, and agent-controlled software supply chains.

### Comment pulse

- Users reported agents suggesting Neon or Fly.io despite established AWS or PlanetScale context, raising memory and judgment concerns.
- Strong defaults may reflect documentation and training prevalence — counterpoint: coordinated content could deliberately manipulate future recommendations.
- Agents can accelerate routine work, but critics said they over-engineer and make poor architectural decisions without expert orchestration.

### LLM perspective

- **View:** Recommendation behavior already acts like distribution infrastructure before providers introduce explicit advertising.
- **Impact:** Defaults can redirect developer adoption while hiding alternatives from users who delegate planning and implementation.
- **Watch next:** Sonnet 4.6 results, prompt stability, ecosystem baselines, disclosure rules, and resistance to recommendation poisoning.
