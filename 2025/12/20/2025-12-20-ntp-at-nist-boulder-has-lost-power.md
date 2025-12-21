# NTP at NIST Boulder Has Lost Power

- Score: 415 | [HN](https://news.ycombinator.com/item?id=46334299) | Link: https://lists.nanog.org/archives/list/nanog@lists.nanog.org/message/ACADD3NKOG2QRWZ56OSNNG7UIEKKTZXL/

## TL;DR
A prolonged, wind-driven power outage in Boulder, combined with preemptive shutdowns to prevent wildfires, has taken NIST Boulder’s atomic time ensemble offline. Backup generators partly failed, leaving NIST’s Boulder Internet Time Service servers powered but no longer accurately referenced, so staff plan to disable them to avoid serving bad time. Physical access to campus is restricted, complicating repairs and monitoring. HN comments discuss NTP’s history, resiliency planning, and alternative time sources like WWV and redundant networks.

## Comment pulse
- Extreme winds (up to 125 mph) led utilities to cut power to avoid fires; commenters note wildfire lawsuits and question NIST’s backup and site-access planning.  
- Thread highlights NTP’s inventor David Mills, his talks, and the idea of using NTP-observed frequency deviations as early warning for fires or HVAC failures.  
- Some suggest separate, low-bandwidth, low-power monitoring networks so status, environmental sensors, and control remain reachable when main cooling, networking, or generators fail.  

## LLM perspective
- View: Critical infrastructure can fail from non-obvious coupling: fire-risk policies, cooling systems, and generators together broke a national time reference.  
- Impact: Operators depending on Boulder NTP should verify stratum-1 diversity, prefer authenticated sources, and monitor for sudden offset or stratum changes.  
- Watch next: Expect more attention on resilient time-distribution: multi-site atomic ensembles, independent power feeds, and better out-of-band monitoring and communication channels.
