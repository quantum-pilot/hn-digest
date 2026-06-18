# Lore – Open source version control system designed for scalability

- Score: 918 | [HN](https://news.ycombinator.com/item?id=48571081) | Link: https://lore.org/

## TL;DR
Lore is Epic Games’ open-source, MIT-licensed version control system built for massive, binary-heavy projects like Unreal games. It’s centralized and content-addressed, using Merkle trees and an immutable revision chain, with chunked storage, deduplication, and on-demand/sparse hydration so terabyte-scale depots remain usable. It supports file locking and server-side control, aiming squarely at Perforce rather than Git. HN game developers welcome a modern, Rust-based Perforce challenger—especially with deep Unreal integration—while noting Git still excels for smaller, code-only workflows.

---

## Comment pulse
- Target is Perforce-style gamedev → handles terabyte-scale binaries, file locks, granular permissions, partial syncs—counterpoint: Git still superior for small, text-only teams and dev tooling.
- Perforce is entrenched via Unreal support but feels dated, expensive, and painful to host; Lore plus first-class engine integration could finally offer a credible escape hatch.
- Git’s push output and concepts feel opaque to many; Lore’s messages seem clearer, though some say Git verbosity should just be hidden behind `-v` and training.

---

## LLM perspective
- View: Centralized, content-addressed VCS optimized for large binaries fills a long-standing gap that Git/LFS never solved cleanly.
- Impact: Game, VFX, and CAD studios gain an open Perforce alternative; Unreal teams may standardize around Lore if tooling matures.
- Watch next: Independent benchmarks, migration tools from Perforce, UE editor integration quality, and how Lore behaves at multi-site, multi-petabyte scales.
