# Iran-backed hackers claim wiper attack on medtech firm Stryker

- Score: 235 | [HN](https://news.ycombinator.com/item?id=47346091) | Link: https://krebsonsecurity.com/2026/03/iran-backed-hackers-claim-wiper-attack-on-medtech-firm-stryker/

## TL;DR
Iran-linked hacktivist group Handala claims it used Stryker’s own Microsoft Intune device-management setup to remotely wipe more than 200k systems and phones across 79 countries. Stryker, a $25B medtech giant embedded in surgical suites and ICUs worldwide, has sent thousands of workers home and is suffering broad IT outages. The attack, framed as retaliation for a US missile strike in Iran, is already disrupting ordering and online clinical services, highlighting how geopolitical cyber operations can quickly become healthcare supply‑chain crises.

---

## Comment pulse
- BYOD + MDM = wipe risk → Employees are often misled that Intune profiles only affect apps; in reality, full-device control and wipes are common.  
- Centralized SaaS consoles are single points of failure → One compromised Intune admin can “self‑destruct” an entire fleet—counterpoint: on‑prem tools can cause similar blast radii without better processes.  
- Platforms lack safety rails → People ask why Intune doesn’t rate-limit wipes (e.g., “>1% devices in minutes = halt”), given how predictable this failure mode is.

---

## LLM perspective
- View: This is a textbook “weaponized IT hygiene” incident: standard management tools turned into strategic wipers by a state-aligned actor.  
- Impact: Hospitals, medtech vendors, and regulators must treat device-management and identity platforms as national critical infrastructure, not mere IT conveniences.  
- Watch next: Concrete mitigations: Intune safety features, mandated guardrails for mass actions, sector-wide tabletop exercises on supply-chain cyber failure in healthcare.
