# Linux Kernel Explorer

- Score: 519 | [HN](https://news.ycombinator.com/item?id=46066280) | Link: https://reverser.dev/linux-kernel-explorer

### TL;DR

The interactive explorer combines the Linux 6.1 source tree with a nine-chapter guided map of kernel concepts, curated files, and documentation. Its opening lesson explains that ordinary syscall work executes in the calling process's context at higher privilege rather than in a separate kernel process, then links that model to boot, tasks, memory, scheduling, and I/O entry points. HN readers liked the lowered entry barrier but treated the implementation and differentiation as unfinished.

### Comment pulse

- Contextual layers aid orientation → readers compared side annotations to commentary traditions that make dense, non-linear texts navigable.
- Differentiation remains unclear → existing browsers already offer source and search, prompting requests for dependency graphs or guided explanations.
- Naive API access harms availability → shared rate limits blocked visitors, and the developer acknowledged caching or authentication needs.

### LLM perspective

- View: Curated reading paths solve conceptual navigation, a different problem from locating symbols.
- Impact: Kernel newcomers can reach representative code before understanding the repository's full topology.
- Watch next: Caching, directory handling, source search, cross-reference graphs, version support, and explanation provenance.
