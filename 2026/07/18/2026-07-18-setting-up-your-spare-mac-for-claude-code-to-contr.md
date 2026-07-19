# Setting up your spare Mac for Claude Code to control, a step-by-step guide

- Score: 167 | [HN](https://news.ycombinator.com/item?id=48959392) | Link: https://ykdojo.github.io/claude-controls-mac/

## TL;DR
The article is a detailed, copy‑pasteable guide for turning a spare Mac into a dedicated “Claude Code box” that the AI can fully control with computer-use (screen, mouse, keyboard). It walks through hardening and isolation (fresh user, no Apple ID, passwordless SSH/sudo), quality-of-life tools (clipboard sync, Tailscale, Screen Sharing), and deeper integrations (tmux-based desktop control, Chrome extension, phone remote-control). HN discussion focuses on whether real hardware is necessary versus containers/VMs, and on concrete 24/7-agent use cases.

---

## Comment pulse
- Real Mac vs VM/container → Some prefer libvirt VMs or cheap VPSs for fast rollback and isolation; hardware mainly matters for macOS-only or GPU/graphics workflows.—counterpoint: old Macs are abundant and enable native apps like iMessage.
- Use cases → Examples include alert triage, long-running data science jobs, GUI tools (Chrome, Figma), intensive local models, and even automated web shopping for specific clothing.
- Security and VM alternatives → Suggestions include VLANs/deny-all firewalls, macOS VMs via UTM; but lack of graphics acceleration and CAPTCHA issues make browser use in UTM frustrating.

---

## LLM perspective
- View: Treating an AI agent like a “teammate with its own workstation” is becoming a practical pattern, not a gimmick.
- Impact: Encourages offloading long, noisy, or risky tasks to a disposable environment, reshaping dev, ops, and data workflows.
- Watch next: Standardized “agent boxes,” hardened images, and first-party tools for secure computer-use and network-scoped permissions.
