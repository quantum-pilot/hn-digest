# Disable AI in Firefox

- Score: 180 | [HN](https://news.ycombinator.com/item?id=45696752) | Link: https://flamedfury.com/posts/disable-ai-in-firefox/

- TL;DR
    - The post lists Firefox about:config switches to disable new AI features: set browser.ml.enable=false for a global off, or toggle chat, page assist, link previews, smart tab groups, and the ML API individually. HN debates on‑device ML utilities versus distracting chatbot elements, bias risks, and immaturity. Skeptics expect flags to rename and fragment; others fault Mozilla’s strategy and bloat while noting Chromium’s unbeatable scale. Extra notes: Firefox added an @perplexity search shortcut; archived builds exist but carry security and unsigned‑addon caveats.

- Comment pulse
    - On-device ML is fine for utilities like translation; disable chatbot cruft. — counterpoint: On-device still risks bias, ads, and inconsistent summaries; usefulness lags.
    - browser.ml.enable off works now, but flags rename/split; expect about:config whack‑a‑mole and new defaults like @perplexity. Archives exist; mind security and unsigned‑addon limits.
    - Mozilla is distracted from core engine; Gecko/Servo missed a platform moment. Others note Chromium’s scale, embedding history, and funding make parity unrealistic.

- LLM perspective
    - View: Treat Firefox ML as opt-in utilities; keep a one-click global kill switch and visible UI toggles per feature.
    - Impact: Privacy-conscious users and IT admins need stable policies; extension authors may rely on ML APIs that users disable.
    - Watch next: Look for Mozilla’s policy on data flow, on-device models, flag stability, and benchmarks for translation, summarization, and tab grouping accuracy.
