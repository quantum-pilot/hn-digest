# Key IOCs for Pegasus and Predator Spyware Removed with iOS 26 Update

- Score: 213 | [HN](https://news.ycombinator.com/item?id=45700946) | Link: https://iverify.io/blog/key-iocs-for-pegasus-and-predator-spyware-cleaned-with-ios-26-update

### TL;DR

iVerify reports that iOS 26 overwrites `shutdown.log` at every reboot instead of preserving successive snapshots, erasing historical artifacts used to investigate Pegasus and Predator infections. Older Pegasus versions left direct traces; later versions’ attempts to clear the log made absence itself a useful heuristic when correlated with boot records. On pre-iOS-26 devices, a particular WebKit Networking staging path could indicate a 2022 infection. iVerify advises saving a sysdiagnose before upgrading. It does not establish whether Apple’s behavior is intentional, a hygiene tradeoff or a bug.

### Comment pulse

- Readers stress that a routinely cleared log can no longer distinguish ordinary reboot behavior from spyware cleanup.
- Motives are contested: some suspect weakened transparency, while others consider a late-introduced bug more plausible.

### LLM perspective

- View: Forensic retention is a security feature even when the underlying log was never designed as a detector.
- Impact: Reboots can now destroy retrospective evidence, narrowing investigative options for targeted users.
- Watch next: Apple’s explanation, restoration of history and purpose-built tamper-resistant telemetry matter more than inferred motives.
