# Apple Silicon and Virtual Machines: Beating the 2 VM Limit (2023)

- Score: 107 | [HN](https://news.ycombinator.com/item?id=47733971) | Link: https://khronokernel.com/macos/2023/08/08/AS-VM.html

### TL;DR

Apple Silicon macOS normally permits only two concurrent macOS guests, reflecting Apple’s license rather than hardware capacity. Mykola Grymalyuk traced enforcement to the closed XNU hypervisor stack and found a hidden `hv_apple_isa_vm_quota` boot argument. By building a hardware-matched development kernel collection, disabling System Integrity Protection and boot-argument restrictions in recoveryOS, and setting the quota, an M2 Pro ran nine usable guests. The unsupported setup complicates operating-system updates and requires restoring the stock boot policy first. Commenters called the cap arbitrary and likely commercial, since non-macOS guests remain effectively unlimited.

### Comment pulse

- Developers called a uniform two-guest ceiling absurd because machine resources already provide a natural limit for serious testing.
- Apple’s hardware-funded software model may discourage cheap Mac hosting — counterpoint: identity-farm prevention was another suggested rationale.
- Readers were impressed that an Apple Silicon Mac can boot a custom development kernel while retaining the full graphical system.

### LLM perspective

- **View:** A kernel-enforced licensing quota creates technical friction without reflecting the host’s real virtualization capacity.
- **Impact:** Test labs gain density at the cost of weakened security posture, fragile updates, and unsupported configuration maintenance.
- **Watch next:** Behavior on current macOS, M3-era nested virtualization, automated kernel builds, policy changes, and safer override mechanisms.
