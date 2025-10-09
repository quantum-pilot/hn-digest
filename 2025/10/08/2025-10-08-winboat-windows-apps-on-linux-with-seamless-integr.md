# WinBoat: Windows apps on Linux with seamless integration

- Score: 203 | [HN](https://news.ycombinator.com/item?id=45518813) | Link: https://www.winboat.app/

- TL;DR
  - WinBoat wraps a Windows VM (KVM, dockur/windows) with automation and RDP “rootless” windows to make Windows apps feel native on Linux. It mounts your home directory, supports experimental USB passthrough, and promises Office/Adobe-type compatibility; no GPU passthrough yet, anti‑cheat games won’t work. HN likes the polished UX but notes it’s not novel—just orchestration over existing pieces—and “Windows in Docker” is misleading. Early users report freezes and flaky integration; others debate native-only vs Wine/Proton/VM pragmatism.

- Comment pulse
  - VM orchestration, not a new approach → KVM + dockur/windows + FreeRDP rootless; daemon reports installed apps; “in Docker” wording misleads.
  - Beta quality shows → users saw Edge freeze, stuck desktop, lingering window outlines; reverted to Windows. — counterpoint: UX is promising if stability improves.
  - Pragmatism vs purism → many need Wine/Proton/VMs for niche tools; “Run Any App” ignores anti‑cheat blocks, no GPU passthrough, non‑USB device gaps.

- LLM perspective
  - View: Polished wrapper around KVM+RDP; value is automation, per-app launchers, and sane defaults, not technical novelty.
  - Impact: Eases life for designers, office users, and USB‑dependent peripherals; insufficient for gamers, 3D workloads, or low-latency creative suites.
  - Watch next: GPU acceleration path (virtio‑gpu, Looking Glass), Flatpak/Podman support, app discovery reliability, and benchmarks versus Wine, WinApps, and native Windows.
