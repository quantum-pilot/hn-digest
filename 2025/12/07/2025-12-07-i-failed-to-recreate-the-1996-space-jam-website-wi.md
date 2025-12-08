# I failed to recreate the 1996 Space Jam Website with Claude

- Score: 250 | [HN](https://news.ycombinator.com/item?id=46183294) | Link: https://j0nah.com/i-failed-to-recreate-the-1996-space-jam-website-with-claude/

### TL;DR
The author tries to have Claude Opus 4.1 recreate the 1996 Space Jam homepage from a single screenshot plus image assets. Despite elaborate prompting, grid overlays, region zooms, and automated screenshot comparisons, Claude keeps producing layouts that are semantically correct (planets orbiting a logo) but geometrically wrong, while confidently declaring “pixel-perfect” success. The post argues this stems from coarse, patch-based vision and LLM overconfidence on its own outputs, illustrating how current models grasp concepts well but fail at precise spatial reproduction.

---

### Comment pulse
- The original Space Jam page used HTML tables, not CSS positioning → LLMs and humans alike misremember early web layouts; nostalgia for sliced-table design resurfaces.  
- LLMs struggle with fine visual/layout details but excel at low-level code tasks → users report complex C and legacy Mac app work succeeding quickly.  
- Some question the premise: if raw HTML is available, why not just copy it → recreating from images highlights model limits, not a practical preservation strategy.

---

### LLM perspective
- View: Current vision-language models encode images semantically, not metrically, so they can “describe” layouts but can’t reliably match pixel-level geometry.  
- Impact: Trust calibration matters; LLMs will misjudge convergence on visual tasks, requiring external checks for design, UI testing, and robotics.  
- Watch next: Higher-resolution encoders, explicit measurement tools, and training that distinguishes self-generated outputs from ground truth for safer self-revision.
