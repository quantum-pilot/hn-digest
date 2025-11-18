# Azure hit by 15 Tbps DDoS attack using 500k IP addresses

- Score: 170 | [HN](https://news.ycombinator.com/item?id=45955900) | Link: https://www.bleepingcomputer.com/news/microsoft/microsoft-aisuru-botnet-used-500-000-ips-in-15-tbps-azure-ddos-attack/

- TL;DR
    - Microsoft says Azure absorbed a 15.72 Tbps, 3.64 Bpps UDP flood from the Aisuru botnet, sourced from 500k IPs against an Australian address. Aisuru—an IoT “Turbo Mirai” botnet—expanded after a TotoLink firmware server compromise; it also powered Cloudflare’s 22.2 Tbps record. Minimal spoofing aided traceback and provider blocking. HN debates why DDoS persists (gaming coercion, competition, market/gambling incentives) and highlights IoT firmware supply‑chain risks. Some dispute that DDoS often masks intrusions, arguing diversion rarely pays off.

- Comment pulse
    - DDoS-for-hire thrives in gaming → revenue from coercion, competition sabotage, revenge by banned players, market or event manipulation; some linked to gambling/“protection” rackets.
    - Supply-chain is the weak link → signed firmware and reproducible builds help, but compromised build/update servers can mass-infect devices; consumer routers often worse than OpenWRT.
    - DDoS as diversion is overstated → mitigation rarely loosens security; only advanced actors time pivots well — counterpoint: misconfigurations under pressure occasionally open doors.

- LLM perspective
    - View: Record-scale bpps matters more than Tbps; IoT UDP floods saturate CPU, state tables, and peering, not just bandwidth.
    - Impact: ISPs/router vendors must harden update servers, enforce signing, and ship auto-updates; clouds push traceback and upstream filtering with carriers.
    - Watch next: Expect takedowns, firmware advisories, and peering policy tweaks; track Aisuru bot counts, bpps peaks, and any arrests or booter-service seizures.
