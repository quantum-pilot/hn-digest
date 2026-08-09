# 3.4M Solar Panels

- Score: 281 | [HN](https://news.ycombinator.com/item?id=47862386) | Link: https://tech.marksblogg.com/american-solar-farms-v2.html

### TL;DR

Version 2 of the GM‑SEUS geospatial dataset expands its US ground-mounted inventory from 2.9 million to 3,429,157 panel records, covering 18,980 arrays, and adds 5,822 rooftop-array records. The author converts GeoPackages to Zstd-compressed, spatially ordered Parquet with GDAL and DuckDB, then maps source coverage and attributes through QGIS and H3. The inspection exposes uneven provenance and major omissions: rooftop coverage is sparse, array and panel detections do not always align, and Ivanpah mirrors appear as panels. Readers therefore cautioned against treating map gaps as actual absence.

### Comment pulse

- Apparent state-level gaps sparked policy debate, but replies noted Florida ranks highly in solar production despite sparse mapped detections.
- Off-grid owners valued resilience during outages and described learning connectors, cable sizing, grounding, breakers, batteries, and monitoring incrementally.
- Readers requested azimuth and tilt distributions; roof area can favor denser east–west or flat layouts over individually optimal orientation.

### LLM perspective

- Publish completeness estimates by state, source, and installation class before using counts for policy comparisons.
- Add geometry validation and facility-type labels to separate photovoltaic rows from concentrated-solar mirrors.
- Track future versions with stable IDs, change sets, and precision-recall audits against sampled imagery.
