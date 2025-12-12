# Days since last GitHub incident

- Score: 189 | [HN](https://news.ycombinator.com/item?id=46233798) | Link: https://github-incidents.pages.dev/

- TL;DR  
GitHub is suffering from frequent incidents—especially with Actions—that are pushing some teams to consider abandoning it entirely, echoing earlier high-profile departures like Zig’s. Commenters describe a sense of “decay,” with reliability, security, and spam problems coexisting alongside an aggressive AI product focus. Others emphasize coping strategies: mirroring repos, building redundancy into tooling, and scripting around bugs such as stuck notification badges. Despite frustrations, GitHub’s tight integration and inclusion in existing plans still make it hard for many organizations to leave.

*Content unavailable; summarizing from title/comments.*

- Comment pulse  
  - GitHub reliability is eroding, particularly Actions and Packages → repeated outages, security worries, AI-first roadmap. — counterpoint: Actions was weak from the start; “decay” may be overstated.  
  - Resilience requires mirrors and automated failover → some build Nix-based mirroring tools, but many lack time/budget even for production apps, let alone CI/CD redundancy.  
  - Spam notification bug illustrates quality gaps → crypto-spam alerts stuck unread; users resort to GitHub CLI/REST scripts while GitHub claims a recent fix.

- LLM perspective  
  - View: GitHub is simultaneously critical infrastructure and a single point of failure; organizations are quietly designing exit ramps, not mass-migrating yet.  
  - Impact: Expect more multi-forge setups, mirrored repos, diversified CI, and reduced reliance on GitHub-specific features like Actions and ghcr.  
  - Watch next: Hard metrics on incident frequency, post-Azure-migration stability, and whether competitors can match GitHub’s network effects without similar reliability issues.
