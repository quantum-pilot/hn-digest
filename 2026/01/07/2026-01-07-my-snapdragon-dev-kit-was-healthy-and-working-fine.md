# My Snapdragon Dev Kit was healthy and working fine until a Windows update failed

- Score: 201 | [HN](https://news.ycombinator.com/item?id=46521860) | Link: https://jasoneckert.github.io/myblog/how-microsoft-killed-my-snapdragon-devkit/

### TL;DR

After more than a year of reliable use, a discontinued Snapdragon X Elite dev kit became unstable following repeated failure and rollback of Windows update KB5068861. Windows profile damage progressed into random reboots, shutdowns, frozen firmware menus, and an unusable installer; reseating components and testing the SSD elsewhere found no answer. The author cannot distinguish corrupted firmware, Secure Boot or TPM state, power-management trouble, or coincidental hardware failure. With no supported recovery path, a potentially repairable fault became terminal. This historical input excludes later post-publication updates.

### Comment pulse

- Many readers read random boot-stage failures as RAM, controller, or power hardware faults rather than software-chain corruption.
- Others cited Windows-delivered firmware patches and fleet experience with failed update rollbacks as plausible routes to a hard brick.
- Discussion broadened into Qualcomm’s sparse recovery documentation and whether unsupported dev kits deserve trust without Linux support.

### LLM perspective

- View: The causal evidence is ambiguous, but missing recovery tooling is the clearest product failure.
- Impact: Unsupported developer hardware can turn routine update risk into irrecoverable downtime and lost confidence.
- Watch next: Reproducible failures across devices or a documented reflashing path would distinguish systemic firmware damage from coincidence.
