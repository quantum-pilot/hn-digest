# Google's Liquid Cooling

- Score: 400 | [HN](https://news.ycombinator.com/item?id=45016720) | Link: https://chipsandcheese.com/p/googles-liquid-cooling-at-hot-chips

- TL;DR
    - Google detailed a datacenter-scale, direct-to-chip liquid cooling system for TPUs: rack-mounted coolant distribution units (N+1), water-to-water heat exchange to facility supply, split-flow cold plates, and bare‑die TPUv4 to handle 1.6× power. Loops run chips in series and size flow for the warmest leg. Pumps use <5% of the fan power of air-cooled servers; maintenance relies on quick disconnects, filtration, and alerting. HN debates novelty—mainframes/HPC did water for decades—but agrees hyperscale, facility-integrated DLC is now standard amid the AI power boom.

- Comment pulse
    - Old idea → mainframes/HPC did water; novelty is hyperscale, facility-to-rack direct-to-chip loops with external chillers/CDUs. — counterpoint: fits Google’s commodity-first evolution.
    - Cooling is the business → operators prioritize industrial heat removal; DLC bypasses human-comfort air limits and can enable higher-temperature loops and heat reuse.
    - Series vs parallel → energy balance identical; series demands higher flow to keep last chip cool, overcools upstream; engineers size flow to thermal impedance.

- LLM perspective
    - View: Direct-to-chip water with N+1 CDUs signals hyperscalers shifting from server cooling to facility-integrated thermal utility operations.
    - Impact: Server/OEM designs, colos, and municipalities adapt for warm-water loops, quick-disconnect standards, leak detection, and potential district heat reuse.
    - Watch next: DLC manifold standards, published PUE/WUE vs coolant temps, chillerless free-cooling days, and real-world leak/maintenance incident rates.
