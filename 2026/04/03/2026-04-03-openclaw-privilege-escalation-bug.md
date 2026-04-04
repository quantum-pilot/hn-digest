# OpenClaw privilege-escalation bug

- Score: 218 | [HN](https://news.ycombinator.com/item?id=47628608) | Link: https://nvd.nist.gov/vuln/detail/CVE-2026-33579

## TL;DR
OpenClaw versions before 2026.3.28 have a privilege-escalation bug in the `/pair approve` command path. The core approval logic assumes a set of caller scopes, but the plugin command handler sometimes calls it without them; the check then fails open. An already-authorized client with pairing/write-level access can approve a pending device request that asks for broader scopes, including `operator.admin`, effectively bypassing the intended permission ceiling. HN discussion focuses on how exposed misconfigured instances are, and on hardening and sandboxing AI agents in general.

---

## Comment pulse
- Author: this is a scope-ceiling bypass for already-authorized command senders, not “any random Telegram/Discord message gets admin” — counterpoint: public, unauthenticated instances still make initial pairing trivial.  
- Stats debate: claim of 135k public instances, 63% without auth is questioned; some see the title as alarmist but effective for driving patching.  
- Practice: several admins run AI agents under restricted OS users or VMs, leveraging classic multi-user isolation instead of trusting application-level auth alone.

---

## LLM perspective
- View: This is a classic “check fails open when optional context is missing” bug in a security-critical path.  
- Impact: Operators of exposed or multi-user OpenClaw instances must patch and audit pairing/auth configs; single-user setups are less at risk.  
- Watch next: Better threat models, mandatory scope propagation, defense-in-depth configs, and automated scans for misconfigured AI agent gateways.
