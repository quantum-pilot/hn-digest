# Lennart Poettering, Christian Brauner founded a new company

- Score: 201 | [HN](https://news.ycombinator.com/item?id=46784572) | Link: https://amutable.com/about

### TL;DR

Amutable is a new Linux security company founded by VFS maintainer Christian Brauner, systemd creator Lennart Poettering, and former Kinvolk CEO Chris Kühl. It says it will make Linux workloads cryptographically verifiable across build, boot, and runtime, so systems begin in a verified state and remain trusted. The announcement offers little implementation detail, prompting discussion of reproducible builds, transparency logs, TPMs, and attestation. A founding engineer said planned attestation models would leave users controlling their keys, while critics warned the same mechanisms could enable DRM-like service exclusion.

### Comment pulse

- Critics feared remote attestation could gate banking or online services — counterpoint: a founding engineer described user-controlled keys and rejected that direction.
- Supporters want verification beyond today’s kernel-focused Secure Boot, which often leaves initrds and userspace outside the trust chain.
- Readers asked whether reproducible builds and transparency logs underpin the design; the company says technical details will follow.

### LLM perspective

- View: Attestation’s value depends less on cryptography than on who controls keys and who may demand proof.
- Impact: Enterprises could verify Linux fleets continuously, while users risk losing services when running modified systems.
- Watch next: Threat model, key ownership, reproducibility, transparency infrastructure, offline recovery, and safeguards against third-party attestation mandates.
