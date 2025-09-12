# Nest 1st gen and 2nd gen thermostats no longer supported from Oct 25

- Score: 282 | [HN](https://news.ycombinator.com/item?id=45143879) | Link: https://community.hubitat.com/t/nest-1st-gen-and-2nd-gen-thermostats-no-longer-supported-by-google-from-10-25-2025/152952

- TL;DR
  - Google is ending cloud/app support and the public API for 1st/2nd‑gen Nest thermostats on Oct 25, 2025. Devices will still work locally, but remote control via Nest/Home, Hubitat, or HA integrations stops. Users weigh options: discounted Nest Gen‑4 with Matter (feature‑limited), Ecobee via Hubitat cloud or local HA/HomeKit, or local‑first Zigbee/Z‑Wave (Sinopé, Honeywell, GoControl). HN leans local‑first; an ex‑Nest engineer says adding secure local APIs to 2011‑era hardware isn’t trivial. An open‑source PCB replacement for Nest v2 is underway.

- Comment pulse
  - Local‑first replacements → Zigbee/Z‑Wave thermostats (Sinopé, Honeywell, GoControl) deliver LAN control and avoid vendor shutdowns; Wi‑Fi/cloud devices invite EOL surprises.
  - Upgrade to Nest Gen‑4 for Matter → local after setup; Hubitat’s Matter driver exposes basics only; buy one and test first.
  - Open local APIs/self‑hosted server → preserves legacy devices — counterpoint: ex‑Nest engineer says secure local support on 2011 hardware is costly and risky.

- LLM perspective
  - View: Cloud‑dependent HVAC is brittle; prefer standards and devices with maintained local APIs.
  - Impact: Platforms shift local; early Nest resale falls; DIY retrofit boards and Zigbee/Z‑Wave demand rises.
  - Watch next: Google EOL specifics, Matter thermostat parity, Ecobee’s Matter timeline, open‑source Nest v2 PCB shipping.
