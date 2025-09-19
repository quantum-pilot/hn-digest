# Show HN: The text disappears when you screenshot it

- Score: 528 | [HN](https://news.ycombinator.com/item?id=45284311) | Link: https://unscreenshottable.vercel.app/?text=Hello

TL;DR
A small demo hides text using animated noise: while the scene moves, motion cues reveal the letters; any single paused frame looks like random static, defeating naive screenshots. Commenters quickly break it by compositing two or more screenshots with blend modes or by recording video and averaging frames. The effect matches motion-based camouflage and random-dot kinematograms; similar shaders exist. It’s friction, not security. Fun twist: GPT‑5 with code tools reconstructed the text; Gemini guessed; Claude refused on safety grounds.

Comment pulse
- Two screenshots + Difference/Screen blend reveal text; even flipping between two tabs rapidly lets your visual system integrate it.
- It’s motion camouflage: animated noise over static noise. Related to random-dot kinematograms; artifacts or zooming out disrupt the illusion.
- Not security: video or frame averaging recovers content; another device works too — counterpoint: opposing motion patterns might raise the work factor.

LLM perspective
- View: Motion-based obfuscation deters single-frame capture; multi-frame or temporal methods defeat it.
- Impact: Best for puzzles, demos, or light obfuscation; unsuitable for protecting sensitive data.
- Watch next: Release reproducible shader, test against OCR/LLMs with multi-frame inputs, quantify break rates vs frame count and noise parameters.
