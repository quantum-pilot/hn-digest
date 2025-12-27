# Show HN: Witr – Explain why a process is running on your Linux system

- Score: 344 | [HN](https://news.ycombinator.com/item?id=46392910) | Link: https://github.com/pranshuparmar/witr

### TL;DR
Witr is a small CLI tool that explains *why* a given Linux process is running by surfacing its “responsibility chain”: parents, service units, cron jobs, and related context like Git repo and branch. It’s aimed at SSH-on-call situations, not full observability or monitoring. HN discussion focuses on polish (README demo, install flow), ideas to extend it with “what does this binary actually do” descriptions, and appreciation for how it streamlines debugging mystery processes.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Tool fills a real gap: quickly answer “why is this process here?” during incident debugging—counterpoint: some also want “what exactly does this binary do?”  
- Build/install opinions: users share Go build incantations, prefer install.sh to favor local source, others suggest Nix packaging for reproducible installs.  
- Responsibility chain and Git info (repo, branch) are praised; implementation walks up from the process’s working directory searching for a `.git` directory.

---

### LLM perspective
- View: Lightweight “process provenance” tools nicely complement heavy monitoring stacks for real-world production firefighting.  
- Impact: Helps SREs, DevOps, and on-call engineers shorten triage time when processes misbehave on shared or legacy hosts.  
- Watch next: Broader OS support, richer attribution (config owners, tickets), optional curated database for process purpose descriptions.
