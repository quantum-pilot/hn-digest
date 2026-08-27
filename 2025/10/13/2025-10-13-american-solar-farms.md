# American solar farms

- Score: 194 | [HN](https://news.ycombinator.com/item?id=45566638) | Link: https://tech.marksblogg.com/american-solar-farms.html

### TL;DR

The post explores GM-SEUS, a new geospatial dataset cataloguing 15,017 ground-mounted solar arrays and about 2.9 million panel rows across the contiguous United States and Washington, DC. Using DuckDB, GDAL, H3, and QGIS, the author converts source files into analysis-ready Parquet, examines fields such as mounting type, capacity, azimuth, spacing, and geometry, and maps notable installations. Only 5,358 array records link to panel records, illustrating both the dataset’s analytical reach and its incomplete coverage across merged source inventories.

### Comment pulse

- Readers discussed pairing panels with parking lots, trails, benches, farms, and fish ponds to combine generation with useful shade.
- Others emphasized the striking physical scale of large Texas and western solar installations.

### LLM perspective

- View: The post’s real contribution is making a rich but messy public dataset reproducibly explorable with commodity tools.
- Impact: Linked array and panel geometry can support land-use research, deployment audits, and infrastructure planning.
- Watch next: Coverage validation, source reconciliation, and clearer explanations for arrays lacking matched panels.
