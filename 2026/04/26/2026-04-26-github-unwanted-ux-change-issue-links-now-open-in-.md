# GitHub unwanted UX change: issue links now open in a popup

- Score: 223 | [HN](https://news.ycombinator.com/item?id=47910546) | Link: https://github.com/orgs/community/discussions/192666

## TL;DR
GitHub quietly changed issue links so they opened in a modal overlay instead of navigating to the issue page, aiming to speed up slow cross‑repo loads and keep users “in context.” Developers hated it: it broke standard web expectations, workflows like copying URLs or using AI agents, widescreen layouts, and assistive technologies. After strong community backlash (both on GitHub and HN), GitHub engineers explained the performance motivation, admitted they “missed the mark,” and fully reverted the change.

## Comment pulse
- Performance band‑aid vs root cause → HN wants GitHub to fix slow cross‑repo rendering, not ship “janky” UX experiments as workarounds.  
- Big‑company UX drift → incentives favor constant redesign, fragmented ownership, and Azure DevOps/Jira‑style modals over stable, predictable, “do nothing if not better” interfaces.  
- Broken browser mental model → modal issue viewers violate “click = go there,” feel slower, hurt accessibility, and reinforce the sense GitHub’s UI has deteriorated since going JS‑heavy.

## LLM perspective
- View: Treat major interaction changes as opt‑in experiments with fast rollback, not defaults that override long‑standing browser norms.  
- Impact: Developer efficiency, accessibility tooling, and ecosystem scripts/userscripts all depend on link semantics staying stable.  
- Watch next: Whether GitHub exposes user‑level feature flags and publishes concrete cross‑repo performance fixes instead of UX workarounds.
