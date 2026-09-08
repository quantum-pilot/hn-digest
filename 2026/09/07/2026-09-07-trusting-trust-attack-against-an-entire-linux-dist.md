# Trusting-Trust Attack against an Entire Linux Distribution

- Score: 196 | [HN](https://news.ycombinator.com/item?id=49575515) | Link: https://arxiv.org/abs/2607.24888

### TL;DR

Researchers report extending Ken Thompson’s trusting-trust attack beyond compilers by tampering with GNU `strip`. In their demonstrated NixOS bootstrap, a malicious seed `strip` altered finished ELF binaries, propagated into later `strip` generations, survived after the seed left the dependency closure, and backdoored nearly every binary in a graphical installer. Commenters dispute the breadth and novelty, noting the attack depends on a tainted binary participating, newer x86 Nix bootstrap seeds are only 181 bytes, and diverse double compilation or full-source bootstraps may detect or avoid it.

### Comment pulse

- Finished-binary manipulation broadens the threat model → an ordinary post-processing utility can perpetuate compromise without parsing source.
- Bootstrap applicability is contested → current minimal x86 seeds may exclude the assumed tampered utility, unlike some other platforms.
- Diverse rebuilding may expose infection → commenters argue varying host, hardware, compiler, and stripping environment should produce a mismatch.

### LLM perspective

- View: The paper demonstrates one potent supply-chain path, not inevitable compromise of every Linux distribution.
- Impact: Reproducible-build systems must audit all seed tools and binary transformations, not only compilers.
- Watch next: Test current architectures, formalize mitigation assumptions, and reproduce detection using diverse double compilation.
