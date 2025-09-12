# CocoaPods trunk read-only plan

- Score: 248 | [HN](https://news.ycombinator.com/item?id=45091493) | Link: https://blog.cocoapods.org/CocoaPods-Specs-Repo/

- TL;DR
  - CocoaPods will make its central Specs trunk read-only by Dec 2, 2026: no new pods or versions, but existing builds keep resolving via GitHub/CDN. A ban on new Podspecs using prepare_command began May 2025 after security abuse. Maintainers will email all contributors twice and run a Nov 1–7, 2026 test freeze. HN splits: gratitude and “time to move on” vs Swift Package Manager pain reports (missing commands, Xcode flakiness, large git clones). Many prefer SPM/Carthage/submodules over CocoaPods’ project “takeover.”

- Comment pulse
  - SPM is inadequate → lacks outdated command, fragile Xcode integration, heavy full‑repo clones inflate CI — counterpoint: others report stability and fewer headaches than CocoaPods.
  - CocoaPods “takes over” projects → required workspaces, Ruby spec files, CDN hiccups; teams preferred SPM or Carthage for simpler tags and Swift‑native workflows.
  - Deprecation is pragmatic → Apple tooling rewards staying on‑path; CocoaPods’ read‑only plan preserves existing builds and gives long notice to migrate.

- LLM perspective
  - View: Read‑only trunk formalizes CocoaPods as archival; ecosystem consolidates on SPM, private specs, or vendored dependencies.
  - Impact: Libraries must ship SwiftPM manifests; CI systems should cache Git checkouts; projects relying on prepare_command need alternative build steps.
  - Watch next: SPM roadmap: version‑outdated tooling, cache controls, compiler‑flag flexibility; CocoaPods publishes migration guides; monitor November 2026 freeze results for breakages.
