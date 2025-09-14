# Run a legal LTE network at home for $100

- Score: 166 | [HN](https://news.ycombinator.com/item?id=45082155) | Link: https://lantian.pub/en/article/modify-computer/legal-lte-network-at-home-for-100-bucks.lantian/

TL;DR
- A step‑by‑step guide shows how to run a legal home LTE cell in the US for about $100: buy a used Helium/FreedomFi CBRS indoor eNodeB (~$60), deploy Magma (core + AGW), authorize via Google SAS (CBSD‑A, ~$2.64/month), and program SIMs using the CBRS test IMSI block (MCC/MNC 315/010). TR‑069 DNS hijack redirects the radio to your core. An iPhone on Band 48 hit ~100/10 Mbps; Android support varied. HN flags eSIM alternatives, EU guard‑band options, and roaming limits for community builds.

Comment pulse
- Skip programmable SIMs → Simlessly’s RSP can issue a free single-device eSIM for your test network; no card writer required.
- EU option → Netherlands allows private 4G in 1.8 GHz guard band ≤200 mW indoors without license; requires radios supporting those frequencies, not CBRS-only units.
- Community LTE viability → Handover/roaming between cells remains brittle; Helium abandoned CBRS. — counterpoint: Single-cell campuses or events can work today.

LLM perspective
- View: Cheap CBRS eNodeBs plus SAS access make LTE tinkering practical; the complexity shifts to orchestration, DNS, and TR-069 configuration.
- Impact: Homelabbers, universities, and IoT pilots gain realistic RAN labs; consumer carriers and incumbents unaffected under GAA limits.
- Watch next: Track open-source mobility/handovers in Magma/Open5GS, eSIM provisioning tools, and any SAS pricing/policy shifts or CBSD supply drying up.
