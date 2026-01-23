# Threat actors expand abuse of Microsoft Visual Studio Code

- Score: 273 | [HN](https://news.ycombinator.com/item?id=46713526) | Link: https://www.jamf.com/blog/threat-actors-expand-abuse-of-visual-studio-code/

### TL;DR

DPRK‑linked “Contagious Interview” operators are now abusing Visual Studio Code’s `tasks.json` to compromise developers who clone and *trust* malicious GitHub/GitLab repos, often sent as take‑home interview assignments. Once trusted, VS Code runs a task that silently executes `curl | node`, pulling a JavaScript backdoor from Vercel. The malware fingerprints the host, beacons to a C2 every 5 seconds, and executes arbitrary JS, later upgrading to a more capable Node agent. HN discussion centers on VS Code’s workspace‑trust UX and broader dev‑tool supply‑chain risk.

---

### Comment pulse

- VS Code team: workspace trust dialog is the core protection; attacks depend on users ignoring warning. — counterpoint: design nudges people toward “Trust” by default.  
- Commenters liken this to supply-chain attacks: unlike installing packages, simply opening a repo can execute `tasks.json` across languages, surprising many developers.  
- Suggested mitigations: default to restricted mode, defer trust prompts, enhance wording, and optionally scan repos for suspicious scripts or configuration-driven execution hooks.

---

### LLM perspective

- View: Editor-integrated execution is unavoidable; priority is reshaping workflows so powerful automation is opt‑in per repo, not globally enabled.  
- Impact: Recruiter-themed campaigns and cloned repos remain high-risk for Mac devs; orgs with junior engineers and lax training are exposed.  
- Watch next: IDE vendors adding heuristic scanning for configs, finer trust scopes, and policies to disable auto-tasks on unvetted repositories.
