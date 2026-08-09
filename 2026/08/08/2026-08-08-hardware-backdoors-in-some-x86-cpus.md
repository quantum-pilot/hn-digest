# Hardware backdoors in some x86 CPUs

- Score: 332 | [HN](https://news.ycombinator.com/item?id=49219508) | Link: https://github.com/xoreaxeaxeax/rosenbridge

### TL;DR
Rosenbridge documents a hidden auxiliary core in old VIA C3 x86 CPUs that can execute a “deeply embedded instruction set” and bypass all privilege and memory protections. Tools are provided to detect whether the feature is present or enabled-by-default and to disable it at boot, plus fuzzers and an assembler for the hidden ISA. HN points out this affects only ancient, niche CPUs and appears to be a documented debug feature, yet treats it as a useful case study in how opaque hardware subsystems create systemic security risk.

---

### Comment pulse
- Hidden hardware features matter → Increasing chip complexity, opaque vendors, and cheap on-die cores (sensors, WiFi, TPUs) create vast, under-scrutinized attack surface; reversing/fuzzing is replicable and valuable.

- “Only VIA C3, and it’s documented” → This targets decades-old CPUs and mirrors a documented Alternate Instruction Set; framing it as a secret backdoor is overstated — counterpoint: intent vs exploitability is secondary to resulting capabilities.

- Trust and mitigation debates → Some argue closed CPUs are inherently untrustworthy and push FPGAs, open cores, and local fabs; others note open-source and VMs can’t fully defeat a compromised host CPU.

---

### LLM perspective
- View: Treat “backdoor” claims as hypotheses: read datasheets, compare with public errata, and reproduce PoCs before concluding malice or novelty.

- Impact: Security work should prioritize opaque coprocessors and sensor/communication modules, which often have full-bus access but ship as uninspectable blobs.

- Watch next: Better automated ISA fuzzers, ME/PSP/open-firmware analysis, and standardized mechanisms to conclusively disable or attest low-level coprocessors.
