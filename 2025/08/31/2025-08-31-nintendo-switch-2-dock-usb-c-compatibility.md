# Nintendo Switch 2 Dock USB-C Compatibility

- Score: 298 | [HN](https://news.ycombinator.com/item?id=45087971) | Link: https://www.lttlabs.com/blog/2025/08/30/nintendo-switch-2-dock

### TL;DR

LTT Labs captured USB-C Power Delivery traffic across Nintendo and third-party Switch 2 charging and docking setups. In its tests, the console drew about 15 watts regardless of charger or dock, reached roughly 90% in two hours and 100% in three, and sometimes charged through third-party equipment without video output. The Nintendo dock requested 20 volts at 3 amps immediately, while an Antank dock scaled its request later. The authors could not determine whether widespread dock incompatibility is deliberate or merely an incomplete USB-C implementation.

### Comment pulse

- Commenters disputed the interpretation of vendor-defined messages and whether a proprietary exchange proves intentional exclusion of third-party docks.
- Several shared anecdotal Switch 1 charging failures, while others said Switch 2 appears more standards-compatible.

### LLM perspective

- View: Measured power behavior is solid evidence; motives inferred from protocol traces remain unsettled.
- Impact: Charging compatibility does not imply display compatibility, making the USB-C connector’s apparent universality misleading.
- Watch next: Reproducible decoding of the proprietary message and broader dock testing could separate safety checks from lock-in.
