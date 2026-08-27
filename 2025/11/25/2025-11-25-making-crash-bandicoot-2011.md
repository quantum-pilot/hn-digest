# Making Crash Bandicoot (2011)

- Score: 190 | [HN](https://news.ycombinator.com/item?id=46045039) | Link: https://all-things-andy-gavin.com/video-games/making-crash/

### TL;DR

Andy Gavin’s retrospective index sketches how Naughty Dog built Crash Bandicoot around PlayStation constraints: a mascot opportunity, sparse enemies, detailed cartoon worlds, and repeatedly refined controls. Its linked excerpts also cover the GOOL Lisp-derived scripting system, localization, and a single-codebase pipeline. In discussion, Gavin confirms that linear levels enabled build-time polygon ordering and delta-encoded visibility lists, reducing runtime work and fitting the console’s 2 MB memory and slow CD access.

### Comment pulse

- Precomputed geometry was structural, not cosmetic → linear paths made polygon sorting and sequential disc layout practical.
- Hardware limits rewarded whole-pipeline design → level layout, visibility data, memory use, and loading strategy reinforced one another.

### LLM perspective

- View: Crash’s signature corridor design doubled as a rendering and storage architecture.
- Impact: Tight constraints made artists, engine programmers, and level designers solve one shared optimization problem.
- Watch next: Compare the linked technical retrospectives with surviving engine artifacts and contemporary PlayStation pipelines.
