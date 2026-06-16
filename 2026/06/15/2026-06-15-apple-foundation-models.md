# Apple Foundation Models

- Score: 461 | [HN](https://news.ycombinator.com/item?id=48536776) | Link: https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models

## TL;DR
Anthropic released a Swift package, ClaudeForFoundationModels, that plugs Claude’s cloud models into Apple’s new Foundation Models framework on iOS/macOS 27. Developers can call Claude through the same LanguageModelSession API as Apple’s on‑device model, with support for streaming, tools (client/server), structured output, images, and mapped errors. Auth is via API key or backend proxy, and apps decide per-call whether to use local or cloud. HN discussion centers on Apple commoditizing LLMs behind an OS abstraction, privacy vs lock‑in, and limits around on‑device models.

## Comment pulse
- Apple turns cloud LLMs into replaceable backends while owning device, UX, and payments—some liken providers to 1990s telcos — counterpoint: commoditization remains distant.  
- Many wanted Claude on‑device; instead it’s cloud-only, raising questions about local models, downloads across apps, and whether Apple should share or standardize storage.  
- Framework abstraction lets apps swap Apple, Claude, Gemini via one API; commenters split between praising privacy safeguards and warning about ecosystem lock‑in and data leverage.  

## LLM perspective
- View: Apple’s framework makes “LLM provider” a pluggable backend role; differentiation shifts toward integration, tooling, and vertical products.  
- Impact: Native devs get one Swift API for local, Apple-hosted, third-party models, slashing integration work but tightening dependence on Apple platforms.  
- Watch next: Watch how Apple handles pricing, quotas, and fees for third-party models via Foundation Models once its own frontier models arrive.
