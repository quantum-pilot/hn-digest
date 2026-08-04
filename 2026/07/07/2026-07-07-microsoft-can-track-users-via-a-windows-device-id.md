# Microsoft Can Track Users via a Windows Device ID

- Score: 323 | [HN](https://news.ycombinator.com/item?id=48815196) | Link: https://www.pcmag.com/news/a-hackers-arrest-reveals-microsoft-can-track-users-via-a-windows-device

### TL;DR

A criminal complaint against alleged Scattered Spider member Peter Stokes shows Microsoft records linking a persistent Windows Global Device Identifier to specific ngrok pages and hosting infrastructure used during a 2025 jewelry-retailer intrusion. The identifier persists across Windows updates but changes after reinstallation; one user may accumulate several distinct IDs. Investigators used those records despite the suspect’s VPN. The evidence demonstrates cross-service correlation, but the article does not establish which software transmitted the browsing data, what traffic Microsoft logs generally, or whether the mechanism applies beyond Microsoft or third-party services.

### Comment pulse

- Identifier existence was not the core concern → machine IDs are common; remote correlation with browsing activity changes the privacy boundary.
- Attribution mechanism remained contested → guesses ranged from Edge SmartScreen and Defender telemetry to ngrok or analytics — counterpoint: the complaint does not resolve it.
- Platform switching offered no simple escape → Linux also exposes machine identifiers, though collection and correlation policies differ.

### LLM perspective

- **View:** The confirmed issue is retained, subpoena-accessible correlation data; claims of universal Windows traffic surveillance remain unproven here.
- **Impact:** VPN anonymity can fail when endpoint telemetry links activity to a stable installation or logged-in account.
- **Watch next:** Microsoft’s explanation, data schema and retention, components, opt-outs, browser scope, and whether identifiers survive account or hardware changes.
