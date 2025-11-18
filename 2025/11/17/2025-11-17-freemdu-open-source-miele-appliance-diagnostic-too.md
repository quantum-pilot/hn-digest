# FreeMDU: Open-source Miele appliance diagnostic tools

- Score: 226 | [HN](https://news.ycombinator.com/item?id=45953452) | Link: https://github.com/medusalix/FreeMDU

- TL;DR
  - FreeMDU is an open hardware/software suite that talks to Miele appliances’ hidden infrared diagnostic port, replacing Miele’s pricey, closed tools. It includes a Rust protocol library, a terminal UI, and MQTT firmware for Home Assistant, currently supporting devices via firmware software IDs. Intended for diagnostics and automation, it’s experimental and risky to use. HN applauds the reverse‑engineering, laments opaque fault codes across brands, shares cheap repair wins (sensors/boards), and debates paying for durable brands like Miele/Bosch/Speed Queen versus cost‑engineered appliances.

- Comment pulse
  - Diagnostics lock-in blocks DIY → Proprietary tools and hidden menus; FreeMDU exposes codes/control. — counterpoint: Some Electrolux models show codes and publish service docs.
  - Small fixes save devices → Replacing $12 hall sensors or cheap boards revives machines; “universal” controllers can substitute at ~20% of OEM prices.
  - Brand calculus → Miele/Bosch/Speed Queen praised for 20–40‑year lifespans; Samsung panned; downsides: proprietary detergent cartridges and HA features reserved for premium tiers.

- LLM perspective
  - View: Open IR adapters could normalize appliance diagnostics/automation, but safety and firmware quirks demand caution.
  - Impact: Empowers DIY repair and independent shops; pressures OEMs on right‑to‑repair and documentation access.
  - Watch next: Expand software‑ID coverage; publish adapter reference designs; firmware dumps and safety guidelines; official Home Assistant integrations.
