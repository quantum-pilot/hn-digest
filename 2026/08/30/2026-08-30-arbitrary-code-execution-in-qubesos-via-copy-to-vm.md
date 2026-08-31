# Arbitrary code execution in QubesOS via copy-to-VM error reporting backchannel

- Score: 244 | [HN](https://news.ycombinator.com/item?id=49496918) | Link: https://www.qubes-os.org/news/2026/08/29/qsb-118/

### TL;DR

Qubes Security Bulletin 118 describes a dom0 command-injection flaw affecting all Qubes releases. When a user copies a file from dom0 into a malicious or compromised qube, that qube can return a crafted filename through qfile error reporting. Dom0’s GUI error path insufficiently sanitizes the filename before passing a constructed command to `system()`, enabling arbitrary code execution. VM-to-VM copying is unaffected because its path uses `execlp()`. Qubes 4.3 users can remediate through normal updates to `qubes-core-dom0-linux` 4.3.22.

### Comment pulse

- Readers stressed that copying from dom0 is discouraged, but isolation should still withstand mistakes by less-technical users.
- Several identified `system()` and shell-string construction—not virtualization—as the central engineering failure.

### LLM perspective

- View: A narrow workflow still becomes critical when its failure crosses directly into dom0.
- Impact: The patch closes a complete-system takeover path without requiring special remediation beyond updates.
- Watch next: Track stable-repository availability and audit other privileged error paths for shell interpolation.
