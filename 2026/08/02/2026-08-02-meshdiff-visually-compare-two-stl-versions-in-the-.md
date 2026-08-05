# Meshdiff – visually compare two STL versions in the browser, client-side

- Score: 171 | [HN](https://news.ycombinator.com/item?id=49143479) | Link: https://meshdiff.com/

### TL;DR

MeshDiff compares two STL, 3MF, or OBJ models entirely in the browser unless a share link is explicitly created. It voxelizes both meshes into one grid, marks additions green and removals red, supports 0–5 mm tolerance, reports volume change, and offers a beta surface-deviation heatmap. Current outputs include JSON reports and reproducible shared diffs; auto-alignment, cross-sections, workers, workspaces, comments, history, approvals, and PDFs are roadmap items. HN liked the local-first design but expected synchronized rotation across all three viewports.

### Comment pulse

- Locked views were the near-unanimous first request because independent rotation makes corresponding geometry harder to inspect.
- Users also wanted transform-aware comparison that isolates actual dimensional change after translation, rotation, scaling, or axis-specific resizing.
- Embedding diffs in pull requests could make 3D-file revisions reviewable alongside code and enable branch previews.

### LLM perspective

- View: Geometry review becomes useful when spatial correspondence is effortless; visualization quality matters as much as numerical difference metrics.
- Impact: CAD and print teams can inspect models locally, reducing upload risk while creating a path toward auditable design reviews.
- Watch next: Benchmark auto-alignment accuracy, voxel resolution cost, false differences near tolerance boundaries, synchronized navigation, and large-model browser performance.
