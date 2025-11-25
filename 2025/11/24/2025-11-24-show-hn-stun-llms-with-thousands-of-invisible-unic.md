# Show HN: Stun LLMs with thousands of invisible Unicode characters

- Score: 183 | [HN](https://news.ycombinator.com/item?id=46029889) | Link: https://gibberifier.com

- TL;DR
  Geneplore’s Gibberifier inserts zero‑width Unicode between letters so text looks normal to humans but becomes long, obfuscated input for LLMs—triggering confusion, refusals, or crashes while wasting tokens. The demo claims multiple models fail. HN tests are mixed: some models decode or strip characters; others refuse due to injection policies. Accessibility risks for screen‑reader users are flagged. One commenter found hidden extra codepoints resembling instructions, and behavior varied across UIs and copy‑paste paths.

- Comment pulse
  - Trivially defeatable → strip zero‑width codepoints or OCR; models can decode but often refuse due to prompt‑injection policies—counterpoint: still breaks naive copy‑paste prompts in consumer UIs.
  - Accessibility harm → recordings show screen readers mangle gibberified text, making content effectively unusable.
  - Odd behaviors observed → Gemini sometimes decodes; paste truncation changes outcomes; hidden anti‑disclosure strings and system prompts surfaced in some tests.

- LLM perspective
  - View: Simple Unicode obfuscation is a short-term nuisance, not a robust anti-LLM defense.
  - Impact: Increases token counts and errors in chat UIs; harms accessibility; minor friction for casual scraping.
  - Watch next: Libraries, browsers, and models adding zero-width normalization; site policies restricting invisible characters; OCR-based agents bypassing text obfuscation.
