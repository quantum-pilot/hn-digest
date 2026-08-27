# Linux Capabilities Revisited

- Score: 162 | [HN](https://news.ycombinator.com/item?id=45669142) | Link: https://dfir.ch/posts/linux_capabilities/

### TL;DR

Linux capabilities split root authority into narrower privileges, but dangerous assignments can create inconspicuous escalation paths. The article demonstrates that granting Python `CAP_SETUID` lets an ordinary user spawn a root-UID shell without modifying the executable or setting its SUID bit. Because ordinary `ls` output hides file capabilities, defenders should inventory them with `getcap`, inspect process capability sets through `/proc` or `getpcaps`, and monitor `setcap`. Commenters stressed that these flags remain coarse ambient privileges, unlike object-capability systems that explicitly pass constrained references between processes.

### Comment pulse

- Defensive gap → SUID audits alone miss privilege embedded in inode extended attributes.
- Model criticism → broad flags such as privileged-port access are weaker than passing a specific bound file descriptor.
- Granularity tradeoff → finer controls reduce authority but enlarge the configuration and escalation surface auditors must understand.

### LLM perspective

- View: Capabilities reduce root exposure only when assignments are visible, minimal, and continuously reviewed.
- Impact: Security teams need capability inventories alongside conventional permission, package, and process monitoring.
- Watch next: Unexpected `setcap` activity, package-file drift, ambient service capabilities, and unexplained executable attributes.
