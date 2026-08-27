# The Asus gaming laptop ACPI firmware bug

- Score: 432 | [HN](https://news.ycombinator.com/item?id=45271484) | Link: https://github.com/Zephkek/Asus-ROG-Aml-Deep-Dive

### TL;DR

A technical investigation attributes periodic stutter, audio crackling, input lag, and occasional crashes on several ASUS ROG laptops to flawed ACPI firmware. Its traces associate `_GPE._L02` with millisecond-scale bursts, while decompiled AML contains sleeps, self-rearming event logic, and GPU power notifications that allegedly omit a MUX-mode check. The author says this serializes ACPI work and can target the only active GPU. HN praised the reverse engineering but emphasized that the repository proposes causes and fixes; ASUS still must validate and ship firmware.

### Comment pulse

- The investigation demonstrates unusually deep end-user diagnosis → commenters praised reproducible traces and decompiled firmware evidence.
- Persistent reports raise process questions → commenters asked how support, QA, firmware review, and vendor escalation missed a visible problem.

### LLM perspective

- View: The evidence forms a credible root-cause hypothesis, but vendor confirmation remains distinct from community reproduction.
- Impact: Affected owners need firmware remediation; driver reinstalls cannot reliably repair BIOS-level control logic.
- Watch next: ASUS’s technical response, corrected BIOS releases, cross-model reproductions, and before-and-after latency traces.
