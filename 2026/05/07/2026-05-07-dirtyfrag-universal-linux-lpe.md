# Dirtyfrag: Universal Linux LPE

- Score: 346 | [HN](https://news.ycombinator.com/item?id=48053623) | Link: https://www.openwall.com/lists/oss-security/2026/05/07/8

## TL;DR
Dirty Frag is a new “universal” local privilege escalation affecting current Linux kernels on major distributions. It chains two bugs: an IPsec ESP Extended Sequence Number (ESN) issue that lets an unprivileged user corrupt page cache contents (e.g., overwrite `/usr/bin/su`), and a separate RxRPC/rxkad bug used to gain controlled writes via encrypted traffic. It shares the same core authencesn ESN sink as the earlier Copy Fail vuln, so simple algif_aead blacklisting is insufficient. No official patches exist yet; mitigations revolve around disabling esp4, esp6, and rxrpc modules and flushing affected page cache. Discussion centers on the real root cause, distro defaults for risky modules, and how LLMs both helped find and may have obscured related bugs by narrowing human exploration.

---

## Comment pulse
- Dirty Frag’s ESP part reuses the same authencesn ESN bug as Copy Fail → fixing/blacklisting algif_aead alone never removed the underlying sink.

- Mitigation: blacklist `esp4`, `esp6`, `rxrpc`, unload them, then drop caches correctly (`echo 1 | sudo tee /proc/sys/vm/drop_caches`)—counterpoint: if already rooted, you must assume full compromise.

- Debate over responsibility: obscure networking/crypto modules are auto-loaded yet rarely needed → some call this 1999-style insecurity, others argue maintainers can’t safely guess what to remove.

---

## LLM perspective
- View: This shows how deep crypto/network plumbing bugs can be repurposed via multiple front-ends, making “fix surface symptom” strategies fragile.

- Impact: Any untrusted local code (malware, shared hosts, CI runners) becomes far more dangerous on unpatched kernels.

- Watch next: concrete kernel fixes for authencesn and RxRPC, distro module-hardening policies, and workflows where LLMs aid broad exploration instead of tunnel-vision.
