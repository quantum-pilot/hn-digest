# Malicious npm packages detected across Red Hat Cloud Services

- Score: 713 | [HN](https://news.ycombinator.com/item?id=48356625) | Link: https://github.com/RedHatInsights/javascript-clients/issues/492

### TL;DR
Dozens of JavaScript packages under Red Hat’s `@redhat-cloud-services` npm scope were compromised, with 90+ malicious versions pushed via a hijacked CI/CD pipeline. These are widely used client and frontend components, so any consumers must audit and roll back specific versions. Hacker News discussion centers on practical mitigations: dependency “cooldowns” (ignoring very new releases), npm’s newer publisher protections (MFA, trusted/staged publishing), stronger CI isolation, and whether the JavaScript ecosystem needs distro-style downstream maintainers rather than trusting upstreams alone.

---

### Comment pulse
- Cooldowns for dependencies → Delay installing versions for 1–3 days; pnpm, yarn, depsguard, uv support this—counterpoint: long-dwell or time‑bombed malware can bypass simple age gates.  
- Registry-side defenses → npm offers MFA, trusted publishers, staged publishing to gate CI releases, but this attack used GitHub OIDC, so malicious builds still looked “trusted.”  
- Process and culture → Suggestions include unprivileged/containerized installs, split build vs publish jobs, and tools like zizmor; some argue the JS “move fast” culture needs distro-like reviewers.

---

### LLM perspective
- View: Treat cooldowns, CI isolation, and registry security as layered controls; assume upstreams and pipelines can and will be compromised.  
- Impact: Org-wide: pin versions, audit all affected `@redhat-cloud-services` releases, tighten CI permissions, and formalize dependency update policies.  
- Watch next: Whether npm makes staged publishing mandatory and whether large users adopt curated mirrors or internal registries as a default.
