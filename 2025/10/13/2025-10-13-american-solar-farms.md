# American solar farms

- Score: 194 | [HN](https://news.ycombinator.com/item?id=45566638) | Link: https://tech.marksblogg.com/american-solar-farms.html

- TL;DR
  - A new GM-SEUS dataset maps 15k ground-mounted US solar arrays and 2.9M panel rows. The author shows how to convert the GPKG release to compact, queryable Parquet with DuckDB/QGIS, explores capacity, mounting types, sources over time, and highlights gaps: only 5,358 arrays include panel rows today, so counts are underestimates pending v2. HN readers pivot to dual‑use siting (parking-lot canopies), the sheer scale of Texas renewables, and a debated ‘cancellation’ of a Nevada project later clarified as a review-process change.

- Comment pulse
  - Dual-use solar canopies are attractive → shade/snow benefits; examples at MSU, libraries; fish-farm pairing in China — counterpoint: structures add cost and collision risks.
  - Texas renewables feel vast → drivers report lake-sized solar fields and synchronized red lights on wind turbines at night.
  - Policy signal is noisy → Esmeralda 7 was reported “canceled,” but BLM clarified a shift from programmatic to individual reviews; environmental impact debates persist.

- LLM perspective
  - View: Treat GM-SEUS v1 as a spatial index for US solar; join with EIA, interconnection, and land-cover for richer analyses.
  - Impact: Helps siting, permitting, risk underwriting, and grid planning by quantifying layout choices and footprint.
  - Watch next: v2 detection metrics, ArcGIS Pro Parquet support, and open benchmarks comparing inferred capacity vs. metered generation.
