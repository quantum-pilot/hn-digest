# Self-updating screenshots

- Score: 457 | [HN](https://news.ycombinator.com/item?id=47908051) | Link: https://interblah.net/self-updating-screenshots

## TL;DR
The author wired their Rails-based help center so screenshots are generated automatically from the live app during a build step. Markdown contains special HTML comments describing which page, element, and UI actions (clicks, waits, cropping, hiding elements, torn edges) to use; a Rake task drives headless Chrome via Capybara/Cuprite to capture images. Running one command regenerates all screenshots, keeping docs visually up to date and encouraging frequent documentation changes, though text still must be maintained manually.

---

## Comment pulse
- Auto-screenshots are spreading → Others use Nix, Android emulators, or Fastlane to script screenshots across platforms, including multiple locales and app-store requirements.  
- Multi-variant docs → Scripted pipelines can emit light/dark theme pairs and swap via `<picture>` plus prefers-color-scheme—counterpoint: setup overhead is non-trivial but pays off long-term.  
- Risk: screenshots fresher than text → UI labels may diverge from prose; proposed fix is tests that scan screenshots for expected words and flag mismatched docs.

---

## LLM perspective
- View: Treat documentation screenshots as build artifacts driven by declarative specs alongside prose, not as manual assets.  
- Impact: Teams with UI-heavy products, multi-theme UIs, or many locales can drastically cut doc rot and release friction.  
- Watch next: Libraries integrating screenshot specs into static-site generators and CI, plus combining with visual-regression testing to catch unintended UI changes.
