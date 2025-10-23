# Ovi: Twin backbone cross-modal fusion for audio-video generation

- Score: 224 | [HN](https://news.ycombinator.com/item?id=45674166) | Link: https://github.com/character-ai/Ovi

- TL;DR
    - Character AI’s Ovi co-generates synchronized video and audio from text or text+image, built on Wan2.2 (video) plus a new 5B audio branch. It outputs 5‑second, 24‑FPS clips trained at 720×720 yet upscales cleanly; open weights, Gradio/ComfyUI, and fp8/qint8 help with heavy VRAM (≈24–32GB). HN welcomes open alternatives to VEO/Runway/Google, flags uncanny artifacts and short durations, and debates whether fully AI‑generated shorts or feature films arrive first.

- Comment pulse
    - Open movement accelerating → Ovi extends Wan2.2; activity around Wan suggests community pace challenging proprietary labs — counterpoint: clips are short, artifacts persist.
    - Quality debate → Impressive sync, but uncanny valleys appear (e.g., extra limbs); some say even theatrical CGI feels similar.
    - What arrives first → Some expect fully AI-generated shorts soon; others argue feature-length films will land first; plus confusion from domain-squatting around new model names.

- LLM perspective
    - View: Co-generating AV avoids post-hoc alignment; twin backbones can share timing cues for lip-sync, foley, and scene coherence.
    - Impact: 24–32GB VRAM keeps it pro-only; expect cloud-first workflows for indies, with local runs on rented GPUs.
    - Watch next: Durations beyond 5s, benchmarked AV-sync and lip accuracy, artifact rates, 11B checkpoint/training scripts, and stable multi-GPU inference.
