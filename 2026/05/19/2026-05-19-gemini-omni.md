# Gemini Omni

- Score: 268 | [HN](https://news.ycombinator.com/item?id=48196609) | Link: https://deepmind.google/models/gemini-omni/

### TL;DR

Google’s Gemini Omni is a multimodal creation model centered on conversational video editing. It can iteratively transform action, style, objects, characters, camera angles, audio, and text while combining image, text, video, or audio references and attempting scene consistency and real-world knowledge. Outputs in Gemini, Flow, and YouTube carry SynthID and C2PA provenance. HN found the demos visually striking but exposed morphing geometry and implausible rigid-body motion, questioned whether video training yields structured spatial understanding, reported confusing usage limits, and found competing Seedance models stronger in early tests.

### Comment pulse

- Visual plausibility masks physical errors → Jenga blocks disappeared, morphed, or moved unrealistically even after repeated prompts for rigid-body accuracy.

- Video-native learning may lack explicit geometry → critics saw no persistent scene structure — counterpoint: transformers can learn dynamics when supplied better representations and pipelines.

- Early comparisons challenge the launch framing → experienced users preferred Seedance 2, while one unrelated SQL test found Omni slower, costlier, and less accurate.

### LLM perspective

- **View:** Coherent video editing needs persistent objects, geometry, and causality; photorealistic frames alone can conceal failures until motion exposes them.

- **Impact:** Creators gain rapid ideation and style transfer, but physics-critical, architectural, and continuity-sensitive work still requires inspection or conventional tools.

- **Watch next:** Benchmark multi-turn identity, occlusion recovery, rigid-body contacts, camera-path geometry, text timing, quotas, and competitor quality on shared inputs.
