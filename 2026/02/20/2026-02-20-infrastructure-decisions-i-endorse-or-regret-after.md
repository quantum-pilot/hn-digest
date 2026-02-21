# Infrastructure decisions I endorse or regret after 4 years at a startup (2024)

- Score: 493 | [HN](https://news.ycombinator.com/item?id=47043345) | Link: https://cep.dev/posts/every-infrastructure-decision-i-endorse-or-regret-after-4-years-running-infrastructure-at-a-startup/

### TL;DR
An infra lead recounts four years scaling an AI-ish startup on AWS/EKS, green-lighting managed databases (RDS, ElastiCache), GitOps with Flux and Helm, Karpenter autoscaling, ExternalDNS/ExternalSecrets, Notion/Linear/Slack, and strong identity plus cost/postmortem processes. Regrets include EKS managed add-ons, Datadog’s pricing, AWS premium support, shared databases, SealedSecrets, Bottlerocket, and delaying FaaS and OpenTelemetry. HN replies mostly agree, but debate AWS vs GCP support, Datadog’s value, and whether Terraform and Kubernetes contradict the “less is better” mantra.

### Comment pulse
- Cost control → Monthly reviews plus proactive billing alarms; PGAnalyze praised for Postgres. Datadog polarizing: pricey, but some see huge value when deeply adopted.  
- Cloud/support choice → Many report responsive AWS account teams used mainly when exploring new services; others argue GCP’s global architecture and resource model are saner.  
- IaC and complexity → Terraform/OpenTofu seen as least-bad vs CloudFormation; some strongly prefer CDK or Ansible. “Less is better” mocked given Kubernetes+GitOps stack.  

### LLM perspective
- View: Practical playbook for infra leads scaling on AWS/K8s; focus on managed databases, GitOps, autoscaling, and strong identity early.  
- Impact: Encourages startups to buy managed databases, centralize identity, and automate postmortems/alerts early, rather than chase marginal infra cost optimizations.  
- Watch next: Compare serverless vs K8s costs under real workloads, and track OpenTelemetry, ExternalSecrets, and Karpenter maturity across major clouds.
