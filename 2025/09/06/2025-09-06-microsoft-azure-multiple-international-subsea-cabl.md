# Microsoft Azure: "Multiple international subsea cables were cut in the Red Sea"

- Score: 186 | [HN](https://news.ycombinator.com/item?id=45152773) | Link: https://azure.status.microsoft/en-gb/status

- TL;DR
    - Microsoft Azure issued a Service Health advisory that multiple subsea cables in the Red Sea were cut, forcing reroutes and raising latency for traffic between Asia, the Middle East, and Europe. Engineers are rebalancing across diverse paths and seeking extra capacity; undersea repairs can take weeks. HN discussion focuses on uncertain causes (frequent anchor damage vs potential sabotage), how splicing and slack management works on repair ships, and respect for backbone operators keeping services running—even when the public status page shows no “active events.”

- Comment pulse
    - Cause is unknown: anchor strikes are common in the Red Sea; others doubt 'accidental' drops on busy routes — counterpoint: too early for attribution.
    - Repairs: ships cut and raise both ends, splice a new section onboard, test, then lay a seabed loop to manage slack and protection.
    - Impact management: operators reroute traffic over alternate cables and transit, trading capacity and path diversity for higher latency rather than outages.

- LLM perspective
    - View: Red Sea chokepoint risk is systemic; multi-provider transit and terrestrial bypasses should be preplanned, not improvised.
    - Impact: Cloud and SaaS see latency/jitter spikes, longer replication times, and costlier egress as providers lease emergency capacity.
    - Watch next: Repair ETAs from cable consortia, new transit announcements, and routing convergence data from RIPE/ThousandEyes to quantify recovery.
