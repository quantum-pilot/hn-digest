# Euro cops take down cybercrime network with 49M fake accounts

- Score: 142 | [HN](https://news.ycombinator.com/item?id=45701825) | Link: https://www.itnews.com.au/news/euro-cops-take-down-cybercrime-network-with-49-million-fake-accounts-621174

- TL;DR
    - Europol and Shadowserver dismantled SIMCARTEL in Latvia, arresting seven and seizing 1,200 SIM boxes with 40,000 active SIMs, five servers, and the sites gogetsms.com and apisim.com. The service sold temporary numbers in 80+ countries to bypass 2FA and generate 49M fake accounts used for fraud, extortion, smuggling, and CSAM, with reported losses of €4.5M (Austria) and €420k (Latvia). HN discussed telco detection versus incentives around SIM farms, per-service phone-number aliases to trace leaks, and the cheeky “Euro cops” framing.

- Comment pulse
    - Per-service phone numbers would expose data sellers → like email aliases, they’d pinpoint leak sources; skeptics say spam rarely traced and aliases add overhead.
    - 40k SIMs from one site should be obvious → rotation, event-like density, coarse location, and inbound-SMS revenue reduce detectability and incentives—counterpoint: clusters should trigger audits.
    - “Euro cops” headline resonated → lighthearted, pan-European framing felt less divisive than national politics; sparked jokes about continental stereotypes.

- LLM perspective
    - View: Striking SMS-as-a-service infrastructure disrupts 2FA-bypass supply chains; platform integrity relies on telecom hygiene as much as app security.
    - Impact: Telcos, KYC providers, and marketplaces face pressure to detect SIM farms; risk teams recalibrate trust in SMS for onboarding/recovery.
    - Watch next: Benchmarks on SIM-box detection rates; moves to email- or app-based 2FA; prosecutions of telco insiders or resellers enabling SIM access.
