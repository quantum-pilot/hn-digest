# Show HN: Witr – Explain why a process is running on your Linux system

- Score: 491 | [HN](https://news.ycombinator.com/item?id=46392910) | Link: https://github.com/pranshuparmar/witr

### TL;DR
Witr is a small CLI for Linux/macOS that answers “why is this running?” for a process, port, or service. Instead of just listing processes, it traces the causal chain of PIDs and supervisors (systemd, docker, pm2, cron, interactive shells), shows context like working dir, git repo, network bindings, and surfaces warnings. HN readers like the focused design, suggest adding “what does this do” knowledge, debate GIF vs screenshot docs, and request proper distro packages instead of curl | bash installs.

### Comment pulse
- witr targets ad‑hoc SSH debugging → unifies ps, systemctl, lsof–style information into one narrative explanation of a process’s origin and context.  
- Many say built‑in commands suffice → systemctl status and lsof can map PIDs and ports to services — counterpoint: witr reduces manual cross‑referencing under pressure.  
- Security‑minded users wary of curl | bash → request deb/RPM/snap packaging and better README visuals; author agrees to add packages and replaced the fast‑looping GIF.  

### LLM perspective
- Nice example of “why” tooling on top of “what” observability; complements, not replaces, traditional monitoring and logging.  
- Most valuable for on‑call engineers and SREs triaging unknown hosts, legacy boxes, or inherited systems with sparse documentation.  
- Watch for integrations with incident tooling (PagerDuty, Slack bots) so on‑call staff can query “why” data directly from alerts.
