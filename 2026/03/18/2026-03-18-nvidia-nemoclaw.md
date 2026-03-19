# Nvidia NemoClaw

- Score: 220 | [HN](https://news.ycombinator.com/item?id=47427027) | Link: https://github.com/NVIDIA/NemoClaw

## TL;DR
NemoClaw is NVIDIA’s open-source plugin and installer that sets up OpenClaw agents inside an OpenShell Linux sandbox, routing all model calls through NVIDIA’s cloud Nemotron models and enforcing declarative policies on network, filesystem, and processes. It targets “always-on” agents with hardened defaults, CI-friendly installers, and alpha-stage tooling. Hacker News discussion focuses on whether sandboxing meaningfully reduces the inherent risk of giving agents access to accounts and data, and on NVIDIA’s motive to capture inference spend and data. Network egress is default-deny and adjusted via policies and human approvals.

## Comment pulse
- Sandboxing OpenClaw agents can't fix risk: useful agents need broad access; attack surface is email, calendars, banking—counterpoint: proxy accounts help but limit utility.  
- Many see NemoClaw as Nvidia’s shovel-selling play → secure default OpenClaw installer that locks users into NVIDIA cloud inference for revenue/data, without solving autonomy dangers.  
- Runtime sandboxing praised, but SKILL.md prompt rules flagged → unprioritized, negative instructions cause silent noncompliance; instruction linting becomes as important as network and filesystem hardening.  

## LLM perspective
- View: NemoClaw is an early reference design for policy-governed autonomous agents, showing what “defense in depth” can realistically provide.  
- Impact: Most valuable for infra/security teams experimenting with always-on agents; far less relevant for average users wanting calendar/email helpers.  
- Watch next: Real-world red-team results, policy templates for common SaaS scopes, and support for non-NVIDIA models to avoid single-vendor lock-in.
