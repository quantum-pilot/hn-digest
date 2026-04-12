# Apple Silicon and Virtual Machines: Beating the 2 VM Limit (2023)

- Score: 107 | [HN](https://news.ycombinator.com/item?id=47733971) | Link: https://khronokernel.com/macos/2023/08/08/AS-VM.html

- TL;DR  
  The article reverse‑engineers Apple’s two‑macOS‑VM limit on Apple Silicon and finds it’s enforced in the kernel via `hv_apple_isa_vm_quota`. By building and booting a development kernel collection from Apple’s Kernel Debug Kit, disabling SIP, and setting special boot args, the author overrides the quota and runs nine macOS VMs on an M2 Pro. This breaks the SLA and complicates OS updates, but shows Apple ships an internal, tunable knob. HN debates the limit’s motives and Apple’s seriousness as a dev platform.

- Comment pulse  
  Apple’s 2‑VM cap is arbitrary → hardware already constrains usage; some want limits scaled by chip tier—counterpoint: any artificial cap on paid hardware is offensive.  
  Limit is business‑driven → discourages Mac VPS providers and large identity farms, aligning with Apple’s hardware‑funded software model.  
  Technical side is impressive → custom dev kernels still boot full GUI; newer M3 nested virtualization might offer alternative ways around the restriction.

- LLM perspective  
  View: Apple quietly supports power‑user toggles while keeping them undocumented and gated behind AppleInternal/SIP, preserving the consumer‑appliance narrative.  
  Impact: Power users, Mac admins, and CI farms gain dense macOS testbeds if they accept more fragile, hands‑on system management.  
  Watch next: Track macOS releases for kernel‑arg changes, nested virtualization behavior, and any official virtualization licensing or quota adjustments.
