# Claude Code for Infrastructure

- Score: 117 | [HN](https://news.ycombinator.com/item?id=46889703) | Link: https://www.fluid.sh/

### TL;DR

Fluid is a terminal agent that clones infrastructure into sandboxes, lets AI inspect and modify the copies, streams an audit log, then generates Ansible playbooks for human-approved production use. Ephemeral SSH certificates restrict access; networking and package installation require approval. The pitch is that tested context beats guessed infrastructure-as-code without giving Claude direct production access. Commenters liked the feedback loop but questioned clone fidelity, database connections, differentiation from sandboxed Claude Code, existing GitOps and container workflows, and the irony of installing a safety tool through a piped shell script.

### Comment pulse

- Isolation improves the agent loop → experiments happen on clones and become reviewable Ansible — counterpoint: realistic multi-service clones and production dependencies are difficult.
- Differentiation remains unclear → users already combine read-only credentials, GitOps, containers, VMs, or general-purpose agents for similar investigation and PR workflows.
- Trust starts at installation → commenters challenged sparse explanation and a curl-to-shell command from a product marketed around infrastructure safety.

### LLM perspective

- View: Fluid’s core contribution is a constrained execution boundary and audit trail, not model capability or infrastructure-as-code generation.
- Impact: Operators may test changes more safely, while inheriting clone creation, secret isolation, drift, fidelity, and playbook-review responsibilities.
- Watch next: Threat model, sandbox architecture, clone coverage, secret handling, rollback tests, generated-playbook quality, enterprise scale, and reproducible installation.
