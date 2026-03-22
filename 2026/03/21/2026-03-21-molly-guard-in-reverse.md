# Molly guard in reverse

- Score: 204 | [HN](https://news.ycombinator.com/item?id=47455138) | Link: https://unsung.aresluna.org/molly-guard-in-reverse/

- TL;DR  
    - The article contrasts classic “molly guards” (physical or digital protections that add friction before dangerous actions) with “reverse molly guards”: flows that automatically proceed if you do nothing. For long, complex operations—OS updates, renders, backups—reverse molly guards prevent jobs from idling all night on trivial prompts and give users confidence they can walk away. HN commenters connect this to poka‑yoke and defensive design, share tooling and outage war stories, and note the original Molly behind the term.

- Comment pulse  
    - Physical poka‑yoke/defensive design → shift knobs, kettles, fuse boxes and furniture constrain actions so mistakes become impossible — counterpoint: many kettles still scald users.  
    - Software molly-guard tools → intercept reboot/poweroff or network changes and demand extra confirmation, turning painful past outages into guardrails and teaching moments.  
    - Reverse molly guards vs forced reboots → users want long jobs to auto‑continue, yet OS vendors increasingly push unattended security updates that silently restart machines.

- LLM perspective  
    - View: Treat confirmation as scarce: require it only when harm is likely; otherwise default to timed auto‑proceed with clear cancellation.  
    - Impact: OS, render farms, CI/CD and backup systems can drastically cut wasted wall‑clock time and frustration by eliminating pointless overnight prompts.  
    - Watch next: instrument flows to log abandoned prompts vs auto‑proceeds, A/B‑test timeouts, and expose policies so admins can tune strictness per environment.
