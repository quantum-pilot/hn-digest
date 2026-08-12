# Infrastructure decisions I endorse or regret after 4 years at a startup (2024)

- Score: 493 | [HN](https://news.ycombinator.com/item?id=47043345) | Link: https://cep.dev/posts/every-infrastructure-decision-i-endorse-or-regret-after-4-years-running-infrastructure-at-a-startup/

### TL;DR

In this 2024 retrospective after four years scaling startup infrastructure, the author endorses managed foundations and boring, interoperable tools: AWS and EKS, RDS, Redis, ECR, GitOps, Terraform, Helm, Kubernetes integrations, identity management, incident reviews, and routine cost scrutiny. Regrets cluster around rigid managed add-ons, shared databases, proprietary telemetry, sealed secrets, expensive Datadog pricing, and hard-to-debug Bottlerocket nodes. The recurring lesson is to pay for protection of critical data, automate team toil, preserve portability early, assign ownership clearly, and avoid optional complexity such as service meshes.

### Comment pulse

- Practitioners mostly recognized the tradeoffs but disputed Datadog’s value and whether AWS support justifies choosing the platform.
- “Less is better” drew laughs beside Kubernetes’s large stack — counterpoint: the author rejects additional layers where benefits remain speculative.
- Terraform remained the least-bad consensus; CDK, Pulumi, Ansible, and OpenTofu advocates contested that choice.

### LLM perspective

- **View:** The strongest endorsements are operating practices, not products: recurring reviews and ownership make imperfect tools manageable.
- **Impact:** Teams should budget for coordination because shared resources and opaque tooling externalize failures onto infrastructure staff.
- **Watch next:** Repeat retrospectives measuring incidents, migration effort, deployment visibility, engineer toil, and per-service costs.
