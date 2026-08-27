# Geolocation and Starlink

- Score: 142 | [HN](https://news.ycombinator.com/item?id=45422514) | Link: https://www.potaroo.net/ispcol/2025-09/starlinkgeo.html

### TL;DR

APNIC Labs found that mapping Starlink IP addresses to countries badly distorted its ISP market-share estimates. Its method implied roughly six million Starlink users in Yemen and over 10% shares across 21 territories, figures likely inflated by ships, aircraft, roaming terminals, cross-border resellers, gateway placement, and inconsistent territorial codes. Mobile satellite access breaks the assumption that an IP address has one stable national location. APNIC therefore marked Starlink data for 20 affected countries as unclassified, sacrificing completeness to prevent misleading national statistics.

### Comment pulse

- Physical and legal location diverge → commenters debated whether terminals abroad represent useful censorship resistance or violations that weaken regulatory authority.
- Precision is conditional → IP geolocation can be granular for fixed assignments, but roaming, VPNs, satellites, and carrier routing create major exceptions.
- Incentives matter → some suspected Starlink tolerates cross-border use to grow, while countries lacking commercial leverage can mainly pursue users.

### LLM perspective

- View: Satellite mobility exposes country labels as policy choices rather than inherent properties of IP addresses.
- Impact: Researchers, rights holders, security systems, and regulators can misclassify users when treating geolocation databases as ground truth.
- Watch next: Maritime and aviation codes, dynamic geofeeds, Starlink methodology, roaming enforcement, and uncertainty-aware market estimates.
