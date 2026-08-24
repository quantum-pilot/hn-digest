# Nvidia-smi hangs indefinitely after ~66 days

- Score: 196 | [HN](https://news.ycombinator.com/item?id=46750425) | Link: https://github.com/NVIDIA/open-gpu-kernel-modules/issues/971

### TL;DR

Operators report that B200 systems using NVIDIA’s open kernel modules lose cross-NVLink functionality after roughly 66 to 67 days of uptime. Monitoring commands then hang, load averages climb, and multi-GPU jobs fail until reboot. Reports span 570 and 580 drivers, Ubuntu and openEuler, and one 256-GPU cluster. NVIDIA confirmed the 580 series is affected, opened internal bugs, and said a fix was in progress without a timeline. A proposed jiffies-wrap explanation remains uncertain because one affected Ubuntu host used a different timer frequency.

### Comment pulse

- A fixed failure interval signals counter overflow → wrap-safe time comparisons exist specifically to avoid long-uptime bugs.
- Monitoring amplifies the outage → repeated hanging probes accumulate load while providing no health signal.

### LLM perspective

- View: Reproducibility across drivers and clusters turns a sparse report into a credible systemic defect.
- Impact: Long-lived accelerator fleets face synchronized failures that can disrupt entire training or inference clusters.
- Watch next: Released driver fix, root-cause disclosure, accelerated wrap tests, and single-GPU behavior after onset.
