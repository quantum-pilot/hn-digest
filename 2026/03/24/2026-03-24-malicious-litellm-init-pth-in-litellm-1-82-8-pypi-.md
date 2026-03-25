# Malicious litellm_init.pth in litellm 1.82.8 PyPI package – credential stealer

- Score: 717 | [HN](https://news.ycombinator.com/item?id=47501729) | Link: https://github.com/BerriAI/litellm/issues/24512

### TL;DR
A popular Python LLM routing library, litellm, had its PyPI wheels for 1.82.8 (and 1.82.7 via code) backdoored with a `.pth` file that auto-runs on every Python interpreter start, exfiltrating environment variables, SSH/cloud/CI credentials, wallet keys and more to an attacker-controlled domain. The compromise appears to stem from a broader TeamPCP/Trivy CI supply-chain attack. Maintainers yanked affected versions and rotated keys. HN discussion centers on how fragile current dependency trust, CI, and developer environments really are, and how to harden them.

---

### Comment pulse
- Incident origin and scope → Maintainer says compromise came via Trivy in CI; proxy Docker images pinned to safe versions; 1.82.7/1.82.8 deleted and credentials rotated.  
- Sandboxing is now mandatory → Commenters argue we must treat any dependency as hostile, using VM-level isolation, tight egress controls, and rethought security models—counterpoint: containers alone haven’t yet been widely bypassed here.  
- Practical defenses → People share a litellm version-scanner, a macOS WebDAV/NFS “canary” fake-secrets filesystem, a detailed TeamPCP timeline, and a Python supply-chain hardening guide.

---

### LLM perspective
- View: Treat `pip install` as executing untrusted code; design workflows assuming at least one dependency will be actively malicious.  
- Impact: Organizations should segment build/dev infra, minimize long-lived tokens, and block outbound traffic by default for dev and CI workloads.  
- Watch next: Better package signing/verification, CI linters for .pth/auto-exec patterns, and incident response playbooks specifically for supply-chain compromises.
