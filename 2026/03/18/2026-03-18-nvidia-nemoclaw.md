# Nvidia NemoClaw

- Score: 220 | [HN](https://news.ycombinator.com/item?id=47427027) | Link: https://github.com/NVIDIA/NemoClaw

### TL;DR

NVIDIA’s alpha NemoClaw stack installs a fresh OpenClaw agent inside OpenShell, combining Landlock, seccomp, network namespaces, filesystem restrictions, policy-controlled egress, and intercepted inference routed to NVIDIA’s cloud Nemotron model. A versioned blueprint configures the gateway, sandbox, provider, and policies; minimums include Ubuntu 22.04, 4 vCPUs, 8 GB RAM, Docker, and a roughly 2.4 GB image. HN readers treated the project as a promising but incomplete security layer for useful always-on agents.

### Comment pulse

- Narrow proxy accounts and scoped credentials reduce service-level blast radius — counterpoint: restrictions can remove the autonomy users wanted.
- Some welcomed OpenShell’s network gateway, while others saw NemoClaw chiefly as a funnel toward NVIDIA inference and compute.
- Risk tolerance divided sharply between trying confined agents now and rejecting any system trusted with consequential personal accounts.

### LLM perspective

- **View:** Agent security needs separate boundaries for operating-system containment and capabilities over external services.
- **Impact:** Teams must inventory delegated actions, not merely filesystem and syscall access.
- **Watch next:** Production providers, policy ergonomics, violation telemetry, and adversarial testing beyond the alpha.
