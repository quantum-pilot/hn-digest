# My Homelab AI Dev Platform

- Score: 216 | [HN](https://news.ycombinator.com/item?id=48542433) | Link: https://rsgm.dev/post/ai-dev-platform/

### TL;DR
Author turns their homelab into an AI-assisted dev platform using OpenCode’s web UI, Git, and GitOps. OpenCode runs on a separate VM with root access but no direct access to production services, generating branches and PRs instead of deploying changes itself. The system helps summarize container release notes, add health checks, and refactor docker-compose stacks, all review-gated via PRs. Biggest missing piece is CI integration, since Forgejo Actions doesn’t yet expose logs via a stable public API.

---

### Comment pulse
- Similar setups emerging → Others run OpenCode or Claude via Forgejo Actions or custom runners, triggering AI with issue commands to auto-generate PRs.  
- Parallel invention → Many are independently building AI dev labs but rarely write them up, so posts like this validate patterns and share practical details.  
- Local vs VM compute → Some prefer agents on their main dev machine for faster builds/tests; a remote VM adds isolation but can bottleneck performance.

---

### LLM perspective
- View: Pattern is “AI as junior dev + PRs,” with strict network isolation and Git as the control plane.  
- Impact: Homelab practices here foreshadow how small teams will standardize AI-assisted ops and infra changes safely.  
- Watch next: Better CI log APIs, first-class “AI runner” products, and policy templates for limiting blast radius of coding agents.
