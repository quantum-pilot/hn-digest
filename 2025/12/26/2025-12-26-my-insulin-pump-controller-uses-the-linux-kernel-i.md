# My insulin pump controller uses the Linux kernel. It also violates the GPL

- Score: 495 | [HN](https://news.ycombinator.com/item?id=46395184) | Link: https://old.reddit.com/r/linux/comments/1puojsr/the_device_that_controls_my_insulin_pump_uses_the/

### TL;DR
An insulin pump user discovered their medical device’s controller runs the Linux kernel and believes the manufacturer is violating the GPL by withholding source. HN lawyers-and-nerds debate what the GPL actually obliges: written offers vs direct source delivery, who can sue, and whether using the kernel obliges releasing any custom code. Others focus on corporate reality: outsourced hardware, lost tarballs, risk-averse support staff, and why effective enforcement likely needs copyright holders or groups like the Conservancy.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- GPL obligations are nuanced: distributors can ship source, include a three‑year written offer, or other options; without a written offer, only copyright holders—not users—can sue.  
- Embedded vendors often outsource and lose track of GPL tarballs; support ignores requests unless legal intervenes—counterpoint: some engineers implement processes and education to satisfy requests.  
- Using Linux kernel alone doesn't require releasing userspace or proprietary modules; likely only kernel source is owed, if binaries are unmodified and shipped correctly.  

---

### LLM perspective
- View: GPL compliance in medical devices is ethical and legal; patients’ safety devices depending on opaque binaries raises trust concerns.  
- Impact: Better handling of source requests, archives, and SPDX-style tracking would reduce risk for vendors and improve transparency for patients.  
- Watch next: Outcomes of Conservancy v. Vizio and similar cases will clarify whether end users can directly enforce copyleft licenses.
