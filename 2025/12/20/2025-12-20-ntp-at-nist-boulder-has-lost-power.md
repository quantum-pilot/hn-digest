# NTP at NIST Boulder Has Lost Power

- Score: 415 | [HN](https://news.ycombinator.com/item?id=46334299) | Link: https://lists.nanog.org/archives/list/nanog@lists.nanog.org/message/ACADD3NKOG2QRWZ56OSNNG7UIEKKTZXL/

### TL;DR

NIST Boulder’s atomic ensemble time scale failed after a prolonged utility outage caused by extreme winds, damaged lines, and wildfire-prevention shutdowns. A crucial standby generator apparently failed, leaving six Boulder NTP services without an accurate reference even though their servers remained reachable on another generator; NIST planned to disable them rather than distribute wrong time. Cooling and internal networks were also shut down, reducing monitoring while the campus remained inaccessible. Staff prioritized alternate power to keep hydrogen masers alive on battery backup, with no repair estimate available.

### Comment pulse

- Readers noted gusts up to 125 mph and recent wildfire liability, explaining the utility’s unusually aggressive preventive shutdown.
- Some proposed an independent low-power monitoring network because cooling shutdown removed visibility exactly when operators needed it most.

### LLM perspective

- View: Reachability without a trustworthy reference makes a time server actively hazardous, so withdrawal is the safe failure mode.
- Impact: Operators relying on named NIST endpoints need diverse time sources across independent sites and power domains.
- Watch next: Clock survival, time-scale realignment, generator failure analysis, and resilient out-of-band telemetry upgrades.
