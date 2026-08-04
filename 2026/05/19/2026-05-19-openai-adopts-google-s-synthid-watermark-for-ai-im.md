# OpenAI Adopts Google's SynthID Watermark for AI Images with Verification Tool

- Score: 200 | [HN](https://news.ycombinator.com/item?id=48198291) | Link: https://openai.com/index/advancing-content-provenance/

### TL;DR

OpenAI is adding Google DeepMind’s invisible SynthID watermark to images made by ChatGPT, Codex, and its API, alongside signed C2PA metadata. A public preview verifier checks both signals: C2PA supplies origin and edit context, while SynthID may survive metadata stripping, resizing, format changes, and screenshots. Absence of either will not prove an image is human-made, and verification initially covers only OpenAI output. HN debated whether attackers can erase the watermark, whether it enables user fingerprinting, and whether imperfect detection still helps expose cheap mass deception.

### Comment pulse

- Watermark removal looks tractable → one commenter reconstructed alternating pixels with an off-the-shelf model — counterpoint: the visible pattern may be a decoy.
- Provenance still has evidentiary value → supporters cited falsified posts exposed via SynthID, arguing imperfect defenses can raise deception costs.
- Mandatory tagging divides creators → critics likened it to unwanted DRM on game assets — counterpoint: generative AI enables vastly greater deception scale.

### LLM perspective

- **View:** Interoperability matters more than any detector’s perfection; shared standards let platforms preserve evidence while adversaries force continuous robustness testing.
- **Impact:** Creators inherit invisible tagging, while journalists and platforms gain a low-cost first-pass check that still requires contextual investigation.
- **Watch next:** Publish payload specifications, privacy controls, false-positive rates, transformation benchmarks, and third-party verifier compatibility beyond OpenAI content.
