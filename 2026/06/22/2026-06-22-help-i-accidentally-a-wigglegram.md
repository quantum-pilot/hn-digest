# Help I accidentally a wigglegram

- Score: 473 | [HN](https://news.ycombinator.com/item?id=48605561) | Link: https://lmao.center/blog/wiggle-accidents/

### TL;DR
The author realizes their habit of taking many near-duplicate photos from slightly different angles has unintentionally filled their iCloud library with potential wigglegrams (looping stereo GIFs). They use perceptual hashing to scan all photos, compute Hamming distances, and automatically find “runs” of visually similar images, then stitch these into animated wigglegrams. The results range from true depth illusions to tiny kinetic moments. HN expands on wigglegram techniques, alignment tricks, data‑viz uses, de‑duplication, and appreciation for “hand-written” code.

---

### Comment pulse
- Wigglegrams can come from multi-lens cameras or depth-map synthesis; phones’ Live Photos and LiDAR make both easy—counterpoint: the aesthetic is currently niche and unfashionable.  
- Careful post-alignment around a stable subject strongly improves depth; choosing the lock point (e.g., a face) controls the perceptual “anchor” and viewer comfort.  
- Perceptual hashes are great for near-duplicate detection if combined across algorithms; readers also praise the script’s readable, non-AI-generated style as “artisanal” code.

---

### LLM perspective
- View: Accidental multi-angle shots are a rich, underused source for playful 3D and motion effects surfaced via simple perceptual tooling.  
- Impact: Hobby photographers, archivists, and data-viz folks gain low-friction ways to mine huge photo backlogs for compelling micro-animations.  
- Watch next: Tools that bundle hashing, auto-alignment, and depth-based interpolation; potential integration into photo apps as an ambient “memories in 3D” feature.
