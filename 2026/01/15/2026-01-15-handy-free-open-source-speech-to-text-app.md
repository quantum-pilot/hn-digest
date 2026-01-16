# Handy – Free open source speech-to-text app

- Score: 201 | [HN](https://news.ycombinator.com/item?id=46628397) | Link: https://github.com/cjpais/Handy

### TL;DR
Handy is a free, MIT‑licensed, cross‑platform desktop app for speech‑to‑text that runs entirely offline using Whisper and NVIDIA’s Parakeet V3. You hit a global hotkey, speak, and Handy pastes the transcript into any text field, with optional debug UI and post‑processing. It focuses on being simple, privacy‑preserving, and hackable (Tauri: Rust backend + React/TS frontend). HN discussion highlights accessibility use (e.g., for users who can’t type), rapid Parakeet‑based workflows, and ideas for integrating STT with LLM agents and custom vocabularies.

---

### Comment pulse
- Local STT is “good enough” with Parakeet V3 → near‑instant, slightly less accurate than top Whisper, but fine when an LLM can interpret/clean the text.  
- Accessibility users want “voice to computer use” → not just dictation, but context‑aware coding/editing by voice powered by STT + LLMs + system context — counterpoint: GUIs make this harder than CLIs.  
- Ecosystem comparison: Superwhisper, Hex, Fluid Voice, VoiceInk, Wispr Flow → each trades off price, UX, live preview, clipboard behavior, and extras like custom words and built‑in LLM routing.

---

### LLM perspective
- View: Handy is an ideal STT front‑end for local/remote agents; it abstracts audio, you wire the text into workflows.  
- Impact: Power users, disabled developers, and privacy‑sensitive teams can build voice‑driven coding and automation without cloud dependence.  
- Watch next: Native “send transcript to LLM” actions, programmable macros, uncertainty‑aware custom dictionaries, and better real‑time streaming vs final‑pass accuracy.
