# Baochip-1x: What it is, why I'm doing it now and how it came about

- Score: 262 | [HN](https://news.ycombinator.com/item?id=47339219) | Link: https://www.crowdsupply.com/baochip/dabao/updates/what-it-is-why-im-doing-it-now-and-how-it-came-about

- TL;DR  
  Baochip‑1x is bunnie Huang’s RISC‑V microcontroller that brings a full MMU and mostly open RTL into microcontroller‑class SoCs, enabling desktop‑style memory isolation in tiny devices. He argues classic page‑based virtual memory remains the most practical base for high‑assurance embedded systems, and that shipping partially open silicon now beats waiting a decade for fully open fabs. By “hitchhiking” on Crossbar’s 22 nm security chip, he added an open VexRiscv core cheaply, then built the Dabao eval board to seed an open ecosystem.

- Comment pulse  
  - Spare die space reuse is praised → Crossbar let bunnie add VexRiscv, but only after strict guarantees on risk, validation, area, and power.  
  - Users dislike Crowd Supply’s VPN blocking → they see it as hostile to privacy — counterpoint: others argue export‑control compliance outweighs benefit of consumer VPNs.  
  - Discussion clarifies openness → Baochip uses the MIT‑licensed VexRiscv core; commenters thank bunnie for decades of approachable hardware hacking work.

- LLM perspective  
  - View: Baochip shows a middle path: open for trust, pragmatic about analog and PHY IP that’s hard to replace.  
  - Impact: If successful, it could seed an ecosystem of MMU‑equipped microcontrollers, enabling richer embedded OSes beyond today’s flat‑memory Cortex‑M world.  
  - Watch next: Watch Xous/Linux adoption on Baochip‑1x, community audits of the RTL, and whether other vendors permit similar hitchhiker cores.
