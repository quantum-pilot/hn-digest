# Threat actors expand abuse of Microsoft Visual Studio Code

- Score: 273 | [HN](https://news.ycombinator.com/item?id=46713526) | Link: https://www.jamf.com/blog/threat-actors-expand-abuse-of-visual-studio-code/

### TL;DR

A DPRK-linked recruitment campaign hides commands in malicious repositories' VS Code tasks.json files. After victims approve Workspace Trust, macOS executes a remote JavaScript payload through Node.js; the backdoor fingerprints hosts, checks a command server every five seconds, and runs returned JavaScript in child processes. Jamf observed an updated payload about eight minutes after infection and published indicators. HN argued over whether a prominent trust prompt is sufficient, with critics favoring restricted-mode defaults and clearer disclosure that trusting can execute shell commands.

### Comment pulse

- VS Code defense → Workspace Trust deliberately gates executable project features; users can isolate unknown repositories in restricted folders.
- UX criticism → a bright affirmative button and vague wording train reflexive consent without conveying that opening a project may run shell commands.
- Broader risk → package scripts, extensions, launch settings, and outbound tools make repository trust wider than any single automatic-task toggle.

### LLM perspective

- View: Security depends on informed consent, but one startup modal cannot communicate a developer workspace's compound execution surface.
- Impact: Recruiter-themed repositories turn routine candidate workflows into cross-language malware delivery, especially when users expect only source review.
- Watch next: Restricted-mode defaults, task provenance previews, workspace-policy enforcement, outbound controls, and repository scanning.
