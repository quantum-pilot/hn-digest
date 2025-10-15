# ADS-B Exposed

- Score: 277 | [HN](https://news.ycombinator.com/item?id=45578383) | Link: https://adsb.exposed/

- TL;DR
    - ADS‑B Exposed is a ClickHouse‑powered demo that aggregates and renders massive ADS‑B flight data into interactive, SQL‑tunable map tiles. It supports real‑time cloud or self‑hosted snapshots, drill‑downs from tens of billions of rows, and example layers like Boeing‑vs‑Airbus or combined altitude/velocity. HN praises the scale and speed, asks for legends/contrast and clearer dataset sources (“Birds,” “You”), spots no‑fly “holes” near Popocatépetl/Area 51/Havana, and notes a separate 3D visualizer as an alternative.

- Comment pulse
    - Usability: Needs legend/contrast; Boeing-vs-Airbus uses RGB for manufacturer counts, opacity for totals — counterpoint: interactive exploration suffices for orientation.
    - Data curiosities: Flight “holes” align with Popocatépetl exclusion zone, Area 51 and Havana; spotted patterns around Vance/Sheppard training bases raise interpretation questions.
    - Features/alternatives: Rectangular selection makes local reports; new datasets (Birds, Photos, “You”) prompt source questions.

- LLM perspective
    - View: A strong demo of high‑volume geospatial analytics: SQL-parameterized rasterizing in ClickHouse yields responsive, map‑tiled heatmaps from billions of rows.
    - Impact: Lowers barrier to exploring ADS‑B, encourages community analysis, and spotlights privacy, airspace restrictions, and training patterns.
    - Watch next: Document provenance and legends; add accessibility modes; expose APIs; benchmark zoom-level latency; prototype 3D/VR client.
