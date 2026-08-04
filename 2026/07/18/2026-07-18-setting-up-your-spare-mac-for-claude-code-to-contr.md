# Setting up your spare Mac for Claude Code to control, a step-by-step guide

- Score: 167 | [HN](https://news.ycombinator.com/item?id=48959392) | Link: https://ykdojo.github.io/claude-controls-mac/

### TL;DR

The guide turns a wiped spare Mac into an always-on, high-permission Claude Code workstation reachable by SSH, phone remote control, Screen Sharing, or Tailscale. It recommends a fresh local admin without personal data or Apple ID, SSH keys, passwordless sudo, disabled sleep, a separate GitHub account, and Claude’s permission-bypass mode. Computer use runs through a LaunchAgent-managed tmux session granted Screen Recording and Accessibility, often Full Disk Access. HN saw value for Mac-native GUI and long-running work but warned that hardware separation does not isolate the local network.

### Comment pulse

- Hardware is optional → VMs and VPSs reset faster — counterpoint: Mac-native apps, graphics, browser fingerprinting, and GUI permissions may favor a spare Mac.
- Machine isolation is not network isolation → use VLAN or deny-all firewall rules because an autonomous root agent can still probe other devices.
- Useful workloads are asynchronous or GUI-bound → examples included incident triage, fuzzing, long analyses, local-model compute, browser tasks, and Figma automation.

### LLM perspective

- **View:** The spare Mac limits local-data exposure but is not a sandbox; it deliberately grants the agent extraordinary machine control.
- **Impact:** Persistent access converts idle hardware into an agent appliance while creating a durable, credentialed endpoint needing server-grade security.
- **Watch next:** Add segmentation, outbound controls, scoped credentials, logging, backups, reimaging, updates, and recurring audits of macOS privacy grants.
