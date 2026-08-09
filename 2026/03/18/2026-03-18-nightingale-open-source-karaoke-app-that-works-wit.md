# Nightingale – open-source karaoke app that works with any song on your computer

- Score: 480 | [HN](https://news.ycombinator.com/item?id=47422942) | Link: https://nightingale.cafe/

### TL;DR

Nightingale is a GPL desktop karaoke system that locally separates vocals with UVR Karaoke or Demucs, retrieves or transcribes word-aligned lyrics through LRCLIB and WhisperX, scores microphone pitch, and supports profiles, videos, gamepads, and dynamic backgrounds across Linux, macOS, and Windows. Its single launcher bootstraps FFmpeg, Python, PyTorch, and models on first run, with GPU acceleration or CPU fallback. HN welcomed private, subscription-free karaoke for obscure songs but reported a Python path bug, unexpected dependency and Docker setup, Japanese alignment failure, lyric drift, and missing editing controls.

### Comment pulse

- Managed dependencies simplify cross-platform support → embedded runtimes avoid incompatible system Python installations — counterpoint: silent executable downloads create trust and supply-chain concerns.
- Multilingual alignment remains fragile → Japanese lyrics yielded hundreds of aligned words but zero preserved display lines.
- Early playback tooling needs refinement → testers requested seeking, punctuation, editable analysis, note previews, and broader GPU support.

### LLM perspective

- **View:** Local inference solves catalog and privacy constraints, but packaging quality now determines whether nontechnical singers can benefit.
- **Impact:** Karaoke fans can process niche libraries without uploads, accounts, telemetry, subscriptions, or preexisting community tracks.
- **Watch next:** Dependency bundling, signature verification, alignment fixes, editable lyrics, pitch visualization, accelerator coverage, and comparisons with UltraSinger.
