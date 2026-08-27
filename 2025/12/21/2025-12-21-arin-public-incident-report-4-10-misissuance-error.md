# ARIN Public Incident Report – 4.10 Misissuance Error

- Score: 130 | [HN](https://news.ycombinator.com/item?id=46345444) | Link: https://www.arin.net/announcements/20251212/

### TL;DR

ARIN accidentally removed IPv4 block 23.150.164.0/24 from its rightful holder and issued it to another customer during a manual 4.10 allocation workflow. The error deleted associated registry services, including ROAs, and enabled an incorrect route announcement for roughly seven days until the original customer reported it. ARIN restored the block, assigned a replacement to the other customer, and coordinated route withdrawal. Planned safeguards include dual review, stricter deletion controls, better allocation and ROA warnings, and migration from spreadsheets to integrated inventory automation.

### Comment pulse

- The affected customer said routing alerts exposed the problem, while deleting the allocation also removed the ROA that might otherwise protect it.
- Readers praised ARIN’s frank report but found production IP allocation through an offline spreadsheet alarming.

### LLM perspective

- View: This was a control-plane failure where authoritative registry error defeated downstream routing safeguards by erasing their source data.
- Impact: Resource holders need alerts for missing allocations and ROAs, not only invalid routes or expiring records.
- Watch next: Whether ARIN’s integrated inventory enforces hard allocation invariants rather than merely presenting stronger warnings.
