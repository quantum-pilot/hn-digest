# Nano Banana can be prompt engineered for nuanced AI image generation

- Score: 390 | [HN](https://news.ycombinator.com/item?id=45917875) | Link: https://minimaxir.com/2025/11/nano-banana-prompts/

TL;DR
- Nano Banana (Gemini 2.5 Flash Image) is an autoregressive image model with standout prompt adherence, likely powered by a strong text encoder and 32k context. Max Woolf shows precise multi-edit control, subject consistency without LoRAs, and success with structured prompts (Markdown/JSON/HTML) that influence composition and even code-like text. He observes system-prompt hints and composition gains via “NYT cover” cues. Weaknesses: style transfer, some rendering quirks, and lenient IP/NSFW moderation. He ships a gemimg API wrapper; ~$0.04/MP, no watermark via API.

Comment pulse
- Layered prompting enables consistent storyboards and img2vid pipelines → control improves with practice — counterpoint: once outputs drift, recovery is difficult.
- Ecosystem/tools: gemimg gets a CLI; interest in open-source editors (e.g., QwenEdit) for masking/LoRAs rivaling Nano Banana’s robustness.
- Tactics/limits: style transfer better with paired reference images; left/right ambiguity surfaced; claims of watermark removal via devtools.

LLM perspective
- View: LLM-grade encoders in AR image models unlock rule-heavy, structured prompting and reliable multi-edit workflows.
- Impact: Cheaper storyboarding/product shots; fewer per-subject LoRAs; higher compliance risk around IP/moderation.
- Watch next: Edit fidelity and style-transfer benchmarks; stronger watermarking/guardrails; open-weight AR models with large context.
