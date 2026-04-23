# 3.4M Solar Panels

- Score: 281 | [HN](https://news.ycombinator.com/item?id=47862386) | Link: https://tech.marksblogg.com/american-solar-farms-v2.html

- TL;DR  
  Mark Litwintschik reviews version 2 of the GM-SEUS dataset, a detailed geospatial catalog of US solar infrastructure. It now includes ~3.43M panel polygons, ~19k ground-mounted arrays, and a new but small (~5.8k) rooftop-solar footprint layer. He documents how to turn GeoPackage data into analysis-ready Parquet using GDAL, DuckDB, and spatial/H3 extensions, then explores coverage, source composition, nulls, and capacity trends over time. Visuals reveal uneven rooftop coverage and striking desert utility-scale patterns, including Ivanpah’s heliostat field.

- LLM perspective  
  - View: This is an excellent reproducible workflow for turning messy national-scale GIS into tidy, queryable Parquet.  
  - Impact: Useful baseline for energy modelers, grid planners, and open-data projects needing real-world solar siting and capacity.  
  - Watch next: Automated rooftop detection, better source harmonization, and validation against utility interconnection and production datasets.
