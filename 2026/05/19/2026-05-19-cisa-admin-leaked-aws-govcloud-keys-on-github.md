# CISA Admin Leaked AWS GovCloud Keys on GitHub

- Score: 402 | [HN](https://news.ycombinator.com/item?id=48190454) | Link: https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/

### TL;DR

A Nightwing contractor working for CISA left a public GitHub repository containing high-privilege credentials for three AWS GovCloud accounts, plaintext passwords for dozens of internal systems, build/deployment material, tokens, and Artifactory access. Researchers say the contractor disabled GitHub’s secret-blocking protection; after notification, the repository vanished but cloud keys remained valid for another 48 hours. CISA says it has no indication of resulting compromise and is investigating. HN focused on missing controls, contractor oversight, staff cuts, and plaintext secrets reaching code hosts or LLM tools.

### Comment pulse

- Commenters called the plaintext CSV, weak passwords, ignored warning, and disabled secret scanning gross negligence — counterpoint: Firefox exports suggest careless file synchronization, not sabotage.
- Agent workflows broaden exposure: encrypt local environment files, prefer short-lived scoped credentials and workload identity, and prevent models from reading secrets by default.
- Political blame split between CISA workforce cuts and contractor failure; several emphasized that the agency still lacked supervision and last-resort automated controls.

### LLM perspective

- View: Secret scanning is a backstop, not a substitute for eliminating static administrative credentials and enforcing least privilege.
- Impact: Compromised build repositories could enable credential theft, lateral movement, or supply-chain persistence across newly deployed government software.
- Watch next: Confirm rotation scope, audit access logs since November, disclose affected systems, verify artifact integrity, and review Nightwing’s controls.
