# Go hard on agents, not on your filesystem

- Score: 573 | [HN](https://news.ycombinator.com/item?id=47550282) | Link: https://jai.scs.stanford.edu/

### TL;DR

`jai` is a Linux wrapper that reduces damage from AI agents and untrusted commands without requiring container images. It keeps the working directory writable, makes temporary directories private, mounts other files read-only, and overlays or hides the user’s home. Its casual, strict, and bare modes trade convenience, confidentiality, UID separation, and NFS compatibility; the project explicitly disclaims VM-grade isolation. HN users welcomed independent defense-in-depth but compared it with native sandboxes, separate Unix accounts, containers, and dedicated hardware. It cannot stop cloud providers seeing files agents read.

### Comment pulse

- Claude’s new sandbox offers similar controls — counterpoint: users reported enforcement failures and advised testing denied reads before trusting status output.
- Plain Unix accounts constrain subprocesses; dedicated laptops simplify mental models but still require careful handling of external-service credentials.
- Critics flagged installation trust — counterpoint: supporters said reviewing a short package build script beats piping a remote script to Bash.

### LLM perspective

- **View:** `jai` solves an adoption problem: a modest boundary people use beats ideal isolation they routinely skip.
- **Impact:** It chiefly protects host integrity; confidentiality, credential theft, kernel exploits, and malicious remote context require additional controls.
- **Watch next:** Security audits, escape testing, distro packaging, non-Linux support, and explicit secret-proxy patterns.
