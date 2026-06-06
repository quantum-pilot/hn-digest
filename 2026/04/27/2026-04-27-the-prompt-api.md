# The Prompt API

- Score: 253 | [HN](https://news.ycombinator.com/item?id=47917026) | Link: https://developer.chrome.com/docs/ai/prompt-api

### TL;DR
The Prompt API lets Chrome web pages and extensions call the built-in Gemini Nano model for on-device prompting, including text, image, and audio. Developers create stateful sessions, specify expected input/output modalities and languages, stream responses, enforce JSON‑schema‑constrained output, and manage context windows, cloning, and destruction. It’s desktop-only, with large one-time model downloads and notable RAM/VRAM requirements, but inference runs locally and doesn’t send data to Google. HN discussion highlights civility filters, model quality tradeoffs, UX pain, and hopes for OS-level model APIs.

### Comment pulse
- De-snark the internet → Extensions rewrite hostile, clickbaity posts into dry facts to reduce flamewars and doomscrolling — counterpoint: filtered views may fragment shared conversations.  
- Local inference win, UX loss → On-device Nano gives free, private “poor man’s Ollama”, but huge initial model download and modest speed frustrate many users.  
- Towards standard model APIs → Commenters compare Gemini Nano to Gemma4/Phi, reference Apple’s Foundation Models, and argue for cross-platform, OS-level model management beyond chat-style interfaces.  

### LLM perspective
- View: Browser-native LLM APIs make AI a first-class web primitive, similar to canvas or WebGL, enabling richer, privacy-preserving client features.  
- Impact: Web apps and extensions gain cheap summarization, search, and moderation tools, especially valuable for enterprises avoiding server-side data sharing.  
- Watch next: Adoption by Firefox/Safari, mobile support, OS-shipped shared models, and standardized knobs for safety, latency, and structured outputs.
