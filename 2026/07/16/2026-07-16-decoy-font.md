# Decoy Font

- Score: 359 | [HN](https://news.ycombinator.com/item?id=48936584) | Link: https://www.mixfont.com/experiments/decoy-font

- TL;DR  
Decoy Font is a downloadable TTF that uses the “hybrid image” optical illusion to show two different texts at once: sharp outlines form a visible decoy, while blurred low-frequency shading encodes a second message legible when squinting or viewing from afar. Because most vision models and OCR read pixels at full resolution, they tend to report only the decoy text, making screenshots partially resistant to scraping. HN debates how robust this is, noting simple pre-processing or better prompts can reveal the hidden text.

- Comment pulse  
  - Novelty / art toy → People like the optical trick and hybrid-image typography, but many argue it’s more playful than practically useful.  
  - Security value debated → Some note it can confuse today’s VLMs or surveillance cameras; others say resizing, filtering, or fine-tuned models will decode messages.  
  - Prompting matters → When told a hidden message exists, newer GPT/Sol models can identify “HAPPY HUMAN,” showing this is an obfuscation arms race, not protection.

- LLM perspective  
  - View: Clever demonstration of frequency-based steganography in fonts; treats AI as a new “viewer” with exploitable perceptual biases.  
  - Impact: Short-term niche uses for anti-scraping screenshots or CAPTCHAs; long-term value as a benchmark for multimodal model robustness.  
  - Watch next: Vision models trained on hybrid images; standardized tests for adversarial typography; legal norms around anti-ML obfuscation in content.
