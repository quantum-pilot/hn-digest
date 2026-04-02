# Claude wrote a full FreeBSD remote kernel RCE with root shell

- Score: 243 | [HN](https://news.ycombinator.com/item?id=47597119) | Link: https://github.com/califio/publications/blob/main/MADBugs/CVE-2026-4747/write-up.md

### TL;DR
A stack buffer overflow in FreeBSD’s `kgssapi.ko` (CVE-2026-4747) lets an authenticated NFS client achieve remote kernel code execution. The bug: `svc_rpc_gss_validate()` copies up to 400 bytes of RPCSEC_GSS credentials into a 96-byte stack region with no bounds check, overwriting saved registers and the return address. The exploit uses 15 GSS-authenticated NFS requests to stream a 432-byte kernel-mode shellcode into BSS, mark it executable, spawn a kernel process, and exec a root reverse shell. Claude (the LLM) helped both find the bug and author the full working exploit from the advisory, sparking discussion about LLM-driven vulnerability discovery, its benefits for defense, and its offensive potential.

### Comment pulse
- LLM-driven vuln discovery will flood us with CVEs → cheaper, broad scanning lets defenders fix issues once reserved for well-funded attackers—counterpoint: short-term, it also empowers offense.  
- LLMs pair well with fuzzing and agents → they can propose harnesses, guide where to fuzz, and iteratively turn “should-never-pass” tests into exploits.  
- FreeBSD hardening is debated → confusion over KASLR status and skepticism that ASLR-style mitigations give meaningful protection versus deeper architectural defenses.

### LLM perspective
- View: LLMs can already execute complex exploit engineering when steered; autonomous vuln research loops are the next obvious step.  
- Impact: Kernel and infrastructure maintainers must plan for attacker-grade automated audit, tightening review, mitigation, and rollout cycles.  
- Watch next: Comparative studies of LLMs vs fuzzers, automated patch generation pipelines, and policy on exploit-capable capabilities in general-purpose models.
