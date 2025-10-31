# GenAI Image Editing Showdown

- Score: 199 | [HN](https://news.ycombinator.com/item?id=45708795) | Link: https://genai-showdown.specr.net/

TL;DR
- Head-to-head benchmark of 14 image generators on prompt adherence with no inpainting/remixing and limited retries. Results: OpenAI 4o 9/12; Gemini 2.5 Flash 8/12; Imagen 4, Seedream 4 at 7/12; FLUX.1 dev 4/12; Midjourney v7 2/12. Hard cases exposed: everyone failed a coral‑snake color sequence and a D20 with primes; 4o handled a maze and complex text well; aspect ratio changed outcomes in cube‑stacking; safety policies blocked some satirical/violent prompts.

Comment pulse
- Safety gating hurts usefulness → 4o refused satirical “violence”; users decry corporate morality — counterpoint: enterprises won’t buy permissive tools; market demands strict filters.
- Undated/old content confused readers → “image editing” vs “generation” mislabeled; correct tab/link later clarified the scope.
- Pipelines likely rewrite prompts/multi-pass → hosted models optimize style/adherence; counter: local single-pass proves capability; attempt counts were shown.

LLM perspective
- View: Adherence-first tests expose brittle sequencing/text reasoning and policy friction, complementing aesthetics-focused comparisons.
- Impact: Expect “precision/strict” modes, stronger text rendering, and clearer safety messaging; local/open stacks favored for controllable workflows.
- Watch next: Public prompts/seeds/outputs, updated 2025 model reruns, and separate editing-mode baselines to isolate capabilities.
