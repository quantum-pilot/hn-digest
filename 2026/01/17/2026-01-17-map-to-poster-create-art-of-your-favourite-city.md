# Map To Poster – Create Art of your favourite city

- Score: 212 | [HN](https://news.ycombinator.com/item?id=46656834) | Link: https://github.com/originalankur/maptoposter

### TL;DR

Map To Poster is a Python CLI that geocodes any city with Nominatim, downloads OpenStreetMap roads and features through OSMnx, then renders a themed PNG using matplotlib. Users choose city, country, one of 17 JSON-defined themes, and a radius; contributors can alter layers, road hierarchy, typography, and colors. HN liked the visuals but requested SVG/PDF output, coordinate-based centering, and batch rendering of all themes. Critics flagged questionable local-map projections and tuning friction, while others prioritized artistic effect; the author plans a format option.

### Comment pulse

- Vector output fits printable maps → users preferred SVG, and the author agreed to add a format flag despite slow large-city exports.
- Projection accuracy matters for local geometry → counterpoint: supporters viewed distortion and edge fading as acceptable artistic choices.
- Better targeting would reduce trial and error → coordinate input and one-command theme batches would improve exploration.

### LLM perspective

- View: The project’s appeal comes from a simple, hackable pipeline connecting open geodata to configurable visual design.
- Impact: Format and centering controls could move it from novelty generator toward practical print-production tooling.
- Watch next: SVG/PDF benchmarks, explicit projection handling, coordinate input, batch themes, and safeguards around Nominatim rate limits.
