# TS-2026-009: Insecure argument handling in Tailscale SSH permitted root access

- Score: 210 | [HN](https://news.ycombinator.com/item?id=48915004) | Link: https://tailscale.com/security-bulletins

### TL;DR

Tailscale says its Linux SSH implementation accepted usernames beginning with `-` and passed them to `getent` as arguments. Connecting as `-i` made `getent` interpret the name as a flag, print account entries beginning with root, and caused Tailscale to open a root session. Exploitation required existing Tailscale SSH access, but bypassed `autogroup:nonroot` ACL restrictions. Version 1.98.9 rejects leading dashes. HN called this a classic argument-injection failure, urged native account-lookup APIs instead of subprocesses, and debated whether Tailscale SSH’s convenience justifies expanding a VPN’s privileged attack surface.

### Comment pulse

- Exploit scope mattered → an attacker already needed tailnet SSH permission — counterpoint: the flaw converted explicitly non-root access into full root control.
- Minimal deployment limits blast radius → users isolate Tailscale on bastions and retain OpenSSH certificates — counterpoint: integrated SSH simplifies revocation and intermittent fleet management.
- Subprocess choice drew criticism → native user-lookup APIs avoid option parsing; merely rejecting dashed names treats the immediate input, not the hazardous boundary.

### LLM perspective

- **View:** Trusted root code delegated identity parsing to a CLI, letting option grammar change an untrusted username’s meaning.
- **Impact:** Non-root policy failed at the privileged host boundary, undermining least-privilege assumptions on affected Linux nodes.
- **Watch next:** Upgrade coverage, argument-fuzzing tests, native account lookup, independent audits, privileged-feature isolation, and disclosure of any observed exploitation.
