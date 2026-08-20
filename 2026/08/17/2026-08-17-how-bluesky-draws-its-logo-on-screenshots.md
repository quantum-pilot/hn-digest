# How Bluesky draws its logo on screenshots

- Score: 707 | [HN](https://news.ycombinator.com/item?id=49338459) | Link: https://timmarinin.net/2026/bluesky-screenshots/

### TL;DR

Bluesky’s iOS app places its logo beneath the Follow button, then renders that button inside a secure UITextField. During screenshots, iOS blanks the secure field to protect sensitive text, exposing the logo underneath; app-switcher snapshots behave differently because they capture an inert frame. The implementation lives in GrowthHack.tsx and uses expo-privacy-sensitive. The author finds the attribution cute, while commenters split between seeing a low-impact replacement for permanent branding and calling it misuse of a privacy API that violates users’ expectation of exact screenshots.

### Comment pulse

- Screenshot-only attribution preserves content → supporters prefer a source logo over an irrelevant Follow button or permanent watermark.
- Secure-field masking protects secrets → counterpoint: banking apps and branding uses make an unoverridable safety feature patronizing and hostile.
- User control is missing → commenters wanted OS permission to override masking and prevent apps from learning about captures.

### LLM perspective

- View: The trick is technically elegant but exposes a governance gap between privacy intent, branding use, and user ownership.
- Impact: App developers gain contextual attribution while platforms inherit pressure to distinguish protection from manipulation.
- Watch next: Apple review rules, screenshot override controls, and broader use of secure-layer compositing will determine whether the technique persists.
