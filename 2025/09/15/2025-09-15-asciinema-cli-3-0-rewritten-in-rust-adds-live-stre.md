# Asciinema CLI 3.0 rewritten in Rust, adds live streaming, upgrades file format

- Score: 319 | [HN](https://news.ycombinator.com/item?id=45251375) | Link: https://blog.asciinema.org/post/three-point-o/

- TL;DR
  - Asciinema CLI 3.0 is a Rust rewrite with a static binary, faster startup, live terminal streaming (local and remote), and a revamped asciicast v3 format using delta timings, exit events, and comments. The player adds adaptive buffering; the server can relay/record streams. The CLI goes local-first: filenames required; uploads are explicit; a server URL prompt eases self-hosting and reduces accidental leaks. HN welcomes streaming and v3, praises AGG/GIF workflows but debates GIF downsides, and notes BEAM-backed scaling under launch-day load.

- Comment pulse
  - GIFs for docs → AGG makes high-quality demos from asciicast; simpler than raw output for heavy stdout effects. — counterpoint: wasteful, unseekable; prefer web player.
  - Live stream stressed asciinema.org → BEAM/Phoenix handled many connections on tiny 2 GB VMs; quick scaling restored stability; tune btop refresh to cut CPU.
  - Frequent rewrites questioned → some call Rust/Go/Python churn trend-chasing; others say language choice is incidental here and developer motivation matters more.

- LLM perspective
  - View: Delta-timed v3 plus comments make casts editable and reviewable in VCS; better for PRs and tooling pipelines.
  - Impact: Static binaries and AVT integration simplify CI/testing of terminal UIs; ops can broadcast incidents without screen-sharing.
  - Watch next: Packaging timelines, stream-recording policies on public servers, migration tools from v2, and standardizing cast metadata for search.
