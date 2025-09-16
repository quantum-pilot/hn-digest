# Tesla said it didn't have key data in a fatal crash, then a hacker found it

- Score: 671 | [HN](https://news.ycombinator.com/item?id=45062614) | Link: https://www.washingtonpost.com/technology/2025/08/29/tesla-autopilot-crashes-evidence-testimony-wrongful-death/

- TL;DR
  - Washington Post: In a 2019 Key Largo fatal crash, Tesla told plaintiffs it lacked critical Autopilot data; a hacker later unearthed it, helping a jury find Tesla partially liable. Court records say crash “snapshots” auto-upload to Tesla, then the car marks its local copy for deletion. HN debates: pervasive infotainment tracking, whether log deletion is design vs. malice, Autopilot’s filtering/object permanence failures shown in annotated footage, and discovery fights where judges threaten sanctions to force telemetry disclosure.

- Comment pulse
  - Automakers control nonstandard logs → owners sue for access; Tesla publicizes telemetry to defend itself — counterpoint: limiting access can protect privacy and investigation integrity.
  - Tesla uploads crash snapshots, then marks local logs for deletion; a server copy may have been deleted, swaying jurors toward liability.
  - Autopilot detected obstacles but planned a path through them → critiques of fixed-object filtering and poor object permanence; overtrust amplifies risk.

- LLM perspective
  - View: The core issue is data governance: retention, access, and auditability for safety-critical logs, not just Autopilot performance.
  - Impact: Expect tighter legal discovery orders, spoliation sanctions, and state laws granting owners and investigators standardized telemetry access.
  - Watch next: NHTSA/NTSB guidance on event data recorders for ADAS, industry logging standards, and manufacturer transparency reports on crash-data retention.
