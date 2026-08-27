# NoLongerEvil-Thermostat – Nest Generation 1 and 2 Firmware

- Score: 346 | [HN](https://news.ycombinator.com/item?id=45813343) | Link: https://github.com/codykociemba/NoLongerEvil-Thermostat

### TL;DR

NoLongerEvil provides experimental tools for flashing first- and second-generation Nest thermostats through OMAP DFU. Modified bootloader and kernel components redirect the device from Google to a reverse-engineered NoLongerEvil API, restoring operation after the original cloud dependency. The project warns that flashing can brick devices or cause unexpected behavior and should not control critical heating or cooling. Although it promises to open-source firmware images and backend code for self-hosting, commenters emphasized that the current release still substitutes one proprietary service for another.

### Comment pulse

- Supporters praised the reverse engineering and right-to-repair potential despite the project’s unfinished state.
- Critics wanted auditable backend code, configurable endpoints, self-hosting, and a privacy policy before accepting claims of complete control.

### LLM perspective

- View: Hardware revival is meaningful, but independence arrives only when every required service is replaceable.
- Impact: Owners gain an experimental recovery path while assuming firmware and climate-control risk.
- Watch next: Backend release, reproducible builds, endpoint configuration, security review, and safe rollback.
