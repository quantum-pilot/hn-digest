# Handy – Free open source speech-to-text app

- Score: 201 | [HN](https://news.ycombinator.com/item?id=46628397) | Link: https://github.com/cjpais/Handy

### TL;DR

Handy is a free, MIT-licensed desktop dictation app that records through a global shortcut, transcribes locally with Whisper or Parakeet V3, and pastes text into the active application. Its Tauri-based Windows, macOS, and Linux client emphasizes privacy, simplicity, and forkability, with configurable models, voice detection, CLI controls, and optional post-processing. HN users praised its speed and accessibility value, especially when typing is difficult, while asking for programming-aware dictation, richer screen context, custom vocabulary, confidence review, and more reliable input across Wayland, VDI, and Citrix.

### Comment pulse

- Parakeet V3 is fast enough for conversational agent prompting → small recognition errors matter less when an LLM can reconstruct intent.
- Speech access can restore productivity during motor impairment → contextual expansion could turn dictation into hands-free coding and computer control.
- Production usability depends on edge cases → specialist vocabulary, uncertainty visibility, and non-clipboard text injection remain important.

### LLM perspective

- View: Handy’s defensible advantage is a modifiable local workflow, not winning a raw transcription benchmark.
- Impact: Forks can target specialized workflows without routing sensitive audio through a vendor-controlled service.
- Watch next: Dictionary improvements, contextual-agent experiments, and fixes for platform-specific recording and insertion failures.
