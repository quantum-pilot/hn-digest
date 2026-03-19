# More than 135 open hardware devices flashable with your own firmware

- Score: 316 | [HN](https://news.ycombinator.com/item?id=47369883) | Link: https://openhardware.directory

### TL;DR

A new “Open Hardware Directory” catalogues ~450+ boards and devices that can be flashed with custom firmware, from ESP32 and RP2040 dev boards to consumer smart-home gear, SBCs, and wearables. Each entry lists specs, price, and typical use-cases, with filters (CPU, brand, firmware, use-case) and an AI-powered search; pages are also exposed as Markdown and llms.txt for tooling. HN likes the goal but notes coverage gaps vs existing firmware projects, UX friction from AI-centric search, and some confusingly non-flashable entries.

---

### Comment pulse

- Directory is useful but far smaller than Tasmota, OpenBeken, Tuya-cloudcutter, ESPHome ecosystems → years of community curation to match coverage.  
- UX criticized: AI-only-ish search feels slow and opaque; users want simple browsing and wildcard filters — counterpoint: maintainer says pagination + filters already list everything.  
- Scope confusion: some listed products are just peripherals, not flashable targets → undermines the “flash with your own firmware” positioning.

---

### LLM perspective

- View: Federate with existing Tasmota/ESPHome/OpenBeken databases instead of rebuilding device metadata from scratch.  
- Impact: Makers, refurbishers, and self-hosters gain a single, canonical lookup point for “can I de-cloud this thing?”.  
- Watch next: Better non-AI browse UI, API export, and community tagging for “flashability,” bootloader access, and open-firmware maturity.
