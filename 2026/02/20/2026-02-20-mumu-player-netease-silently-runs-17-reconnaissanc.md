# MuMu Player (NetEase) silently runs 17 reconnaissance commands every 30 minutes

- Score: 308 | [HN](https://news.ycombinator.com/item?id=47082496) | Link: https://gist.github.com/interpiduser5/547d8a7baec436f24b7cce89dd4ae1ea

### TL;DR

A researcher reports that MuMu Player Pro 1.8.5 on macOS executes 17 reconnaissance-like commands about every 30 minutes, recording network configuration, processes, installed applications, launch services, mounts, and other system details. The logs reportedly include potentially sensitive command-line data and are retained locally in rotating files. Separate SensorsData analytics include the Mac serial identifier and a queued payload. The evidence demonstrates recurring local collection, but it does not establish that the detailed reconnaissance logs are uploaded.

### Comment pulse

- Many commenters recommend isolating emulators in VMs or restricted networks; counterpoint: others argue broad surveillance practices span vendors and countries.
- The unresolved question is network transmission: local collection is documented, while exfiltration of the command-output logs remains unproven.

### LLM perspective

- **View:** Diagnostic data becomes surveillance-grade when recurring collection spans network topology, processes, software, and a durable device identifier.
- **Impact:** Isolation limits collection scope, while packet capture is needed to distinguish retained diagnostics from transmitted telemetry.
- **Watch next:** Destinations, payload contents, retention behavior, privacy-policy changes, Apple review, and whether later releases remove collection.
