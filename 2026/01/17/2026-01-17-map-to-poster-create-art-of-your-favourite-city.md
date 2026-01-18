# Map To Poster – Create Art of your favourite city

- Score: 212 | [HN](https://news.ycombinator.com/item?id=46656834) | Link: https://github.com/originalankur/maptoposter

### TL;DR
MapToPoster is a small Python tool that turns any city into a minimalist map poster using OpenStreetMap data, OSMnx, and themed color palettes. You run a CLI command with city, country, theme, and radius; it fetches roads/parks/water, renders via matplotlib, and saves high‑res PNGs. The repo includes 17 themes, distance presets, and a “hacker’s guide” for extending layers (e.g., railways) or styles. HN discussion covers alternatives, projections, SVG output, printing options, and city-name ambiguity.

---

### Comment pulse
- Similar projects exist → anvaka’s city-roads is praised for SVG output and an in-browser interface; author has other respected visualization tools.  
- Projection nitpicks → some see non-local projections as a flaw; others stress it’s decorative art, not cartography—counterpoint: projection still affects aesthetics.  
- Practicalities → SVG/PDF export via matplotlib is easy but slow for large cities; users trade tips on print services and how Nominatim handles duplicate city names.

---

### LLM perspective
- View: Nice example of “generative art from open data,” with clear architecture that invites hacking and theming.  
- Impact: Lowers the bar for personalized, data-driven wall art for coders, designers, and gift-givers.  
- Watch next: Optimized vector export, explicit projection choices, and a simple web front-end would broaden adoption beyond Python users.
