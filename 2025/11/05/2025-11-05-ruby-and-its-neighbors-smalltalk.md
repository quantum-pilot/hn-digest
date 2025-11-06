# Ruby and Its Neighbors: Smalltalk

- Score: 161 | [HN](https://news.ycombinator.com/item?id=45823831) | Link: https://noelrappin.com/blog/2025/11/ruby-and-its-neighbors-smalltalk/

- TL;DR
  - HN compares Ruby to its Smalltalk lineage through the lens of Smalltalk’s image-based environment. Proponents love images for live, persistent systems and reflective tooling; critics argue images complicated reproducibility and distribution, and licensing costs hurt adoption while free Java surged. Practitioners describe native-looking deployments via trimmed images that reset state. Newspeak appears as a modern, capability-secure Smalltalk-like path. Many say Ruby kept the pure object model but lost the image/IDE strengths, while scripting and conventional tooling shaped its success.
  - _Content unavailable; summarizing from title/comments._

- Comment pulse
  - Smalltalk images enable live evolution and persistence → debugging and distribution of state; but reproducibility/versioning suffered and high licensing hurt adoption — counterpoint: modern forks improved tooling.
  - Deployment wasn’t a kiosk OS → images booted into native Windows UIs; vendors used tree-shaking and executable headers; many apps reset state on startup.
  - Ruby echoes Smalltalk’s object model → lacks image-based IDE, live tooling; community and Rails favored text editors, source control, and scripting; some want Smalltalk-like editors.

- LLM perspective
  - View: Image-like workflows could return via containerized snapshots with deterministic builds, versioned state, and better provenance than 90s Smalltalk images.
  - Impact: Dynamic-language IDEs can regain live-editing strengths without sacrificing reproducibility; Ruby could host experiment IDEs leveraging its reflection and debuggers.
  - Watch next: WASM Smalltalk/Newspeak VMs, standardized image manifests, incremental checkpointers, and benchmarks on startup/memory to evaluate deployability beyond nostalgic demos.
