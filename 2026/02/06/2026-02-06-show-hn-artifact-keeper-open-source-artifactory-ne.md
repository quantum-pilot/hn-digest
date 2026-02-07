# Show HN: Artifact Keeper – Open-Source Artifactory/Nexus Alternative in Rust

- Score: 142 | [HN](https://news.ycombinator.com/item?id=46909037) | Link: https://github.com/artifact-keeper

### TL;DR
Artifact Keeper is a self-hosted, MIT-licensed artifact registry written in Rust that aims to be a drop‑in replacement for Artifactory/Nexus without feature-gated “enterprise” editions. It supports dozens of native package formats, security scanning via Trivy/Grype, SSO and RBAC, replication, search, migration tooling, and even mobile apps, deployable via Docker/Kubernetes. HN discussion focuses on AI-assisted development and build‑vs‑buy decisions, questions about robustness and security/compliance at large scale, and debate over permissive licensing.

### Comment pulse
- AI coding agents shift build‑vs‑buy calculus → some see 3‑week Claude‑assisted build as reason to roll custom registries, others prefer maintained, generic tooling.  
- Enterprise JFrog users intrigued but cautious → need CVE feeds, blocking policies, and SBOM‑like features plus support — counterpoint: others doubt it matches mature platforms.  
- Licensing and trust debated → MIT praised for openness but feared enables cloud competitors; format‑count mismatch breeds skepticism, yet some propose Packj and multisig‑signing integrations.  

### LLM perspective
- View: AI‑assisted greenfield projects like this show complex infrastructure can be cloned quickly, raising expectations for open, fully featured alternatives.  
- Impact: Small orgs and self‑hosters gain leverage in negotiations with Artifactory/Nexus vendors and may standardize on cheaper, auditable registries.  
- Watch next: real‑world uptime/scale metrics, HA deployments, SBOM/curation roadmap, security audits, and whether a sustainable support/commercial model emerges.
