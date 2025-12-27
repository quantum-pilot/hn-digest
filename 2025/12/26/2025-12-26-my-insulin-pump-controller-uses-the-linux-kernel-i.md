# My insulin pump controller uses the Linux kernel. It also violates the GPL

- Score: 438 | [HN](https://news.ycombinator.com/item?id=46395184) | Link: https://old.reddit.com/r/linux/comments/1puojsr/the_device_that_controls_my_insulin_pump_uses_the/

- TL;DR  
An insulin pump controller was found running the Linux kernel; the manufacturer apparently ships binaries without offering corresponding GPLv2 source. Commenters dive into GPL section‑3 details: when users are actually entitled to source, whether failure is contract breach or copyright violation, and how jurisdiction matters. Others describe how outsourced hardware, poor archival, and risk‑averse lawyers make compliance rare. Several note that if the device only uses an unmodified kernel, the released code may be minimal but still obligatory.  
*Content unavailable; summarizing from title/comments.*

- Comment pulse  
  - GPL enforcement is murky: obligations hinge on written source offers; some say non-delivery is contract breach, others see GPL breach—counterpoint: Germany lets end-users sue.  
  - Companies often outsource firmware, lose build artifacts, and sideline support; legal teams may ignore low-risk GPL requests, so contacting corporate counsel via lawyer is advised.  
  - If only a vanilla Linux kernel is used, users may get little beyond kernel source, since GPL doesn’t extend to separate userspace apps or drivers.

- LLM perspective  
  - View: GPL compliance around embedded Linux remains fragile; medical devices heighten stakes because patients depend on secure, verifiable software.  
  - Impact: Clearer global precedent on who can enforce GPL would incentivize firms to maintain reproducible builds and documented source-release processes.  
  - Watch next: Track Conservancy v. Vizio and similar cases; also, industry guidelines or tooling that automate GPL obligations for embedded vendors.
