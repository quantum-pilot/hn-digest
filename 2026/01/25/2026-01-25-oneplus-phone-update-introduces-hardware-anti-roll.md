# Oneplus phone update introduces hardware anti-rollback

- Score: 305 | [HN](https://news.ycombinator.com/item?id=46757944) | Link: https://consumerrights.wiki/w/Oneplus_phone_update_introduces_hardware_anti-rollback

### TL;DR
OnePlus/OPPO’s January 2026 ColorOS updates for several flagship phones silently blow Qualcomm QFPROM eFuses, enforcing a hardware anti-rollback counter. Once updated, any attempt to flash older stock firmware or most existing custom ROMs can hard-brick the device, requiring a motherboard replacement. EDL unbrick tools no longer bypass this. The move, made without clear disclosure, is framed by defenders as necessary to stop downgrade-based attacks, while critics see it as an ownership and right-to-repair violation that undermines modding and long-term device control.

---

### Comment pulse
- Security-first view → eFuses and anti-rollback are long-standing, standard defenses against reverting to exploitable firmware and defeating anti-theft or secure boot. — counterpoint: hard-bricking is disproportionate to that goal.  
- Ownership / rights view → remote updates that permanently restrict firmware choice show you “license” a phone; vendors can vandalize devices post-sale without meaningful recourse.  
- Modding nuance → bootloader unlocking isn’t killed; new ROMs built on the fused firmware base should work, but the existing ROM ecosystem is instantly obsolete for updated devices.  

---

### LLM perspective
- View: This is a textbook security–freedom tradeoff, made worse by opaque communication and an unusually harsh failure mode (hard brick).  
- Impact: Custom ROM communities, refurbishers, and privacy‑conscious power users lose flexibility; average users inherit more vendor lock‑in by default.  
- Watch next: Clear OEM statements, fuse-state diagnostic tools, ROMs targeting fused bases, and potential regulatory scrutiny under right-to-repair or unfair-practices laws.
