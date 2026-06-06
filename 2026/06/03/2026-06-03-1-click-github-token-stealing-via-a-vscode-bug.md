# 1-Click GitHub Token Stealing via a VSCode Bug

- Score: 633 | [HN](https://news.ycombinator.com/item?id=48371562) | Link: https://blog.ammaraskar.com/github-token-stealing/

### TL;DR
- A VSCode web bug let any malicious github.dev link, when opened once, install an attacker’s extension and steal your GitHub OAuth token.  
- The flaw: webviews forward real and synthetic `keydown` events to the host, so injected JS in a Jupyter notebook could trigger VSCode shortcuts.  
- By abusing workspace extension recommendations and local workspace extensions, the attacker bypassed publisher trust checks and exfiltrated the all-repos token.  
- Clearing github.dev site data or avoiding untrusted github.dev links mitigated risk; Microsoft has deployed stopgap fixes.

---

### LLM perspective
- View: This shows how small UX conveniences in sandboxed components can silently dissolve critical security boundaries.  
- Impact: GitHub users, enterprises, and extension authors must revisit trust assumptions around web-based IDEs and workspace-provided configuration.  
- Watch next: Hardening of webview messaging, stricter command gating, and clearer browser-style security prompts for in-editor actions.
