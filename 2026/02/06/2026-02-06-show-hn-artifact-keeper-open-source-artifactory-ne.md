# Show HN: Artifact Keeper – Open-Source Artifactory/Nexus Alternative in Rust

- Score: 142 | [HN](https://news.ycombinator.com/item?id=46909037) | Link: https://github.com/artifact-keeper

### TL;DR

Artifact Keeper presents itself as an MIT-licensed, self-hosted alternative to JFrog Artifactory and Sonatype Nexus with no paid feature gates. Its Rust backend claims native support for 45-plus package formats, Trivy and Grype scanning, policy enforcement, SSO, edge replication, WASM plugins, migration tooling, and Docker or Kubernetes deployment. Commenters welcomed an affordable escape from costly enterprise platforms but questioned whether a three-week AI-assisted build is production-ready, citing untested policies, missing SBOM features, unclear CVE refresh, support burden, permissive licensing, and a disputed format count.

### Comment pulse

- A large JFrog user described $500,000-plus annual spend and 140 TB stored, but stressed support, unusual failures, policy depth, and CVE freshness.
- Coding agents may shift build-versus-buy economics—counterpoint: commenters doubted most teams would maintain bespoke registries or trust rapidly generated infrastructure.
- MIT maximizes adoption and scrutiny but permits proprietary competitors; the author prefers community first, leaving any support business undefined.

### LLM perspective

- View: The pitch is compelling, but registries earn trust through protocol fidelity, durability, security maintenance, and recovery evidence.
- Impact: Small teams gain controls without license gates; adopters inherit operational risk and must validate formats, policies, and recovery.
- Watch next: Protocol conformance, load tests, CVE refresh, SBOM support, air-gap updates, disaster recovery, deployments, and maintainer activity.
