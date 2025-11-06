# NoLongerEvil-Thermostat – Nest Generation 1 and 2 Firmware

- Score: 346 | [HN](https://news.ycombinator.com/item?id=45813343) | Link: https://github.com/codykociemba/NoLongerEvil-Thermostat

- TL;DR
    - An experimental firmware uses the OMAP DFU bootloader to flash Nest Gen 1/2 with custom x-load, U-Boot, and a Linux kernel that redirects traffic from Google to the NoLongerEvil backend. The device stops talking to Google and registers to a new dashboard. HN likes the right-to-repair angle and reviving “bricked” units, but flags that today it’s a closed blob tied to a proprietary service with no clear privacy policy; open-source backend and self-hosting are promised “soon.” Alternatives via OpenTherm/Home Assistant also surface.

- Comment pulse
    - Swap one lock-in for another → Endpoint is fixed, no self-host today; privacy policy unclear — counterpoint: reverse-engineering and DFU path are a big step forward.
    - Right-to-repair win → DFU exploit + custom boot chain can revive idle Nests; community bounties suggest momentum.
    - Prefer open standards → OpenTherm/EMS-ESP with Home Assistant yields finer control, energy savings, and avoids cloud reliance.

- LLM perspective
    - View: Promising jailbreak, but true user control requires configurable endpoints and an open, self-hostable backend.
    - Impact: Extends Nest Gen1/2 lifespan; raises expectations for local control and vendor repair policies.
    - Watch next: Publish server code, add local-first mode, document self-hosting; third-party audits; reports on forced-air compatibility.
