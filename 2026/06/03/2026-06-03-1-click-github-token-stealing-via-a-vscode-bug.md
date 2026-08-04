# 1-Click GitHub Token Stealing via a VSCode Bug

- Score: 633 | [HN](https://news.ycombinator.com/item?id=48371562) | Link: https://blog.ammaraskar.com/github-token-stealing/

### TL;DR

For returning github.dev users, a malicious repository could steal the service’s broad OAuth token after one link click. A Jupyter webview forged keyboard events, accepted a recommended local workspace extension, then used its keybinding to bypass publisher trust and install token-stealing code; the credential could modify every accessible repository, not just the opened one. Desktop VS Code was also affected with extra steps. Microsoft shipped a next-day stopgap requiring notebook confirmation and blocking trust bypass. HN praised the response speed but saw ambient authority as the deeper flaw.

### Comment pulse

- Least privilege was the missing boundary → Codespaces already issues repository-scoped tokens; github.dev should copy that model or use human-approved staging.
- Extensions remain powerful Node.js applications → publisher trust does not prevent filesystem access or compromised dependencies after installation.
- Fast remediation earned praise → Microsoft patched within a day — counterpoint: prior silent fixes and poor researcher credit encouraged full disclosure.

### LLM perspective

- **View:** UI events crossing a sandbox boundary must carry capabilities, not inherit ambient application authority.
- **Impact:** Browser IDE users need explicit approval before untrusted notebooks or extensions execute with repository credentials.
- **Watch next:** Permanent fixes for synthetic key events, local-extension trust, OAuth scoping, and desktop webview parity.
