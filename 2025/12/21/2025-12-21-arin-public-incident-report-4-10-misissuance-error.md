# ARIN Public Incident Report – 4.10 Misissuance Error

- Score: 130 | [HN](https://news.ycombinator.com/item?id=46345444) | Link: https://www.arin.net/announcements/20251212/

## TL;DR
ARIN mistakenly deleted a customer’s IPv4 /24 (23.150.164.0/24) and reassigned it to another org due to a legacy, Excel-driven “4.10” allocation workflow that bypassed robust automated checks. The error lasted about a week and only surfaced when the original holder saw a BGP alert, by which time the new holder was announcing the route and the ROA had been auto-removed. ARIN reversed the change, issued a replacement /24, and is accelerating full online automation and dual-review controls.  

## Comment pulse
- Affected holder used BGPAlerter, saw their /24 “hijacked,” then found it missing in ARIN; plans to monitor for disappearing ROAs too.  
- Some see rising ARIN fees as unjustified by service quality; others note ARIN is now cheaper than RIPE for smaller orgs.  
- Many praise ARIN’s blunt, blame-owning report and generally solid RIR track record—counterpoint: automation itself often introduces new, different failure modes.  

## LLM perspective
- View: Critical registries should design for “RIR can be wrong” scenarios; external alerts on registry/RPKI changes are now table-stakes.  
- Impact: Network operators need monitoring for missing ROAs and unexpected WHOIS changes, not just route origin anomalies.  
- Watch next: Whether ARIN delivers unified inventory, role-based controls, and auditable automation—and if other RIRs publish similar incident postmortems.
