# The unlikely story of Teardown Multiplayer

- Score: 214 | [HN](https://news.ycombinator.com/item?id=47366435) | Link: https://blog.voxagon.se/2026/03/13/teardown-multiplayer.html

- TL;DR  
  Teardown’s long-awaited multiplayer seemed impossible: fully destructible voxel worlds, mods, and chaotic physics are notoriously hard to sync over networks. Dennis Gustafsson describes evolving from a bandwidth‑hungry prototype to a hybrid model: deterministic, command-based destruction plus unreliable state sync for motion within a 1 Mbit budget. They kept scripting and modding via shared server/client scripts, streamed UI as delta-encoded draw commands, enabled limited join-in-progress by replaying command logs, and spent a year merging divergent branches while preserving backward compatibility.

- Comment pulse  
  Floating-point determinism is tricky → Within one ISA you can mostly succeed; cross-CPU requires restricted ops, stable FPU modes, and avoiding aggressive compiler optimizations.  
  Business choice praised → Shipping multiplayer as a free update, not a sequel, feels consumer‑friendly; Coffee Stain’s handling of Satisfactory/Valheim suggests solid long‑term support.  
  Voxel-space physics curiosity → Fully discrete, grid-aligned physics looks wrong; converting voxel chunks to meshes stays pragmatic — counterpoint: some enjoy weird, intentionally discrete worlds.

- LLM perspective  
  View: Mixing deterministic command streams with lossy state sync is a strong template for networking highly dynamic, partially deterministic simulations.  
  Impact: Shows small teams can retrofit demanding multiplayer into shipped single-player sandboxes, guiding other indies with destructible or systemic worlds.  
  Watch next: Benchmarks or talks on their new engine’s simplified multiplayer, and whether they pursue cross-platform determinism beyond Steam networking.
