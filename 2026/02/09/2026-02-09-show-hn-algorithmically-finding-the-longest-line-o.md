# Show HN: Algorithmically finding the longest line of sight on Earth

- Score: 360 | [HN](https://news.ycombinator.com/item?id=46943568) | Link: https://alltheviews.world

TL;DR  
- A custom algorithm exhaustively scanned global elevation data, computing billions of terrain-based sightlines to find Earth’s longest unobstructed view: about 530 km between peaks in western China and Tajikistan. An interactive map exposes 4.5 billion precomputed views for exploring extreme and local maximum sightlines. Hacker News discussion corrects the mountain naming, asks for 3D or Google Earth-style visualizations as the real payoff, debates atmospheric feasibility versus ~483 km photographic records, and uses the tool to probe regional candidates.

Comment pulse  
- Naming accuracy matters → commenters note the “Hindu Kush” start peak is actually in the Kunlun/Hindu Tagh range, urging correct geographic labeling.  
- Need richer visuals → many want Google Earth-style or panorama 3D views to feel the terrain; author links a helper repo and welcomes PRs.  
- Theoretical vs visibility → some doubt 500 km is seeable through atmosphere — counterpoint: others cite a 483 km photo record and long NZ/America lines.

LLM perspective  
- View: Treat this as a global computational geometry dataset; beyond records, it maps local visibility basins for planning, tourism, education.  
- Impact: Combining it with real-time aerosols and weather could turn theoretical sightlines into probabilistic “when can I see X?” forecasts.  
- Watch next: Benchmark algorithmic coverage, publish open DEM+code pipeline, and maybe crowdsource verified photos to constrain refraction and visibility models.
