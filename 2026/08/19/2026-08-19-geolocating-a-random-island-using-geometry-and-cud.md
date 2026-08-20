# Geolocating a random island using geometry and CUDA programming

- Score: 469 | [HN](https://news.ycombinator.com/item?id=49360545) | Link: https://yassa9.github.io/osint/gralhix-004/

### TL;DR

Without EXIF or reverse-image search, the author converted three visible landmasses into a tolerant triangle fingerprint and searched an 882 MB OpenStreetMap coastline dataset. Heuristic tropical, density, clustering, shape, open-water, vegetation, and elevation filters generated 80.7 million island triples; an RTX 3050 tested them in 204.1 ms, ultimately leaving 26 candidates for visual inspection. The eighth match identified Oan resort in Micronesia at 7.363444° N, 151.755750° E, with a calculated camera bearing of 324.97°, northwest. The thresholds were intuition-driven, not a general proof.

### Comment pulse

- Readers praised the human-written style and suggested more geoguessing or earlier visual checking.
- Commenters connected the method to terrain-contour navigation in missiles and Mars 2020 landing.
- OpenStreetMap drew appreciation as a flexible OSINT dataset, especially where richer mapped features exist.

### LLM perspective

- View: It is a delightful reproducible search, though tuned heuristics and final visual inspection complete the solution.
- Impact: GPU geometry and open data can sharply narrow metadata-free image geolocation.
- Watch next: Blind tests, threshold sensitivity, perspective modeling, and automatic final-candidate ranking.
