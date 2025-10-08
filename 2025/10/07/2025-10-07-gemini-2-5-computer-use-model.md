# Gemini 2.5 Computer Use model

- Score: 417 | [HN](https://news.ycombinator.com/item?id=45507936) | Link: https://blog.google/technology/google-deepmind/gemini-computer-use-model/

TL;DR
- Google’s Gemini 2.5 Computer Use model, now in API preview, lets agents operate UIs in a loop using screenshots and action calls (click, type, scroll). It targets browsers first, shows strong results on web/mobile control benchmarks with lower latency, and ships per-step safety checks and confirmation gates. HN testers found the demo striking—handling logins and navigation—but noted limits (e.g., trouble interpreting Wordle colors). A viral “CAPTCHA solve” was Browserbase’s solver, not Gemini. Discussion contrasted general UI-control models with tool-specific automations.

Comment pulse
- General UI-control model → aims to work across arbitrary UIs, unlike Chrome DevTools MCP scripts — counterpoint: skeptics see just predefined tool orchestration.
- Model solved CAPTCHA → later clarified Browserbase’s environment handled the solve; Gemini only attempted it.
- Autonomous browsing feels eerie → logs in, scrolls, replies; lacks real-time steering and struggles with color feedback tasks like Wordle.

LLM perspective
- View: UI-control agents are finally usable; reliability hinges on action-review loops, DOM robustness, and injection-resistant prompting.
- Impact: Short-term winners: QA teams, RPA vendors, and customer-support automation; losers: brittle bespoke scripts and manual test suites.
- Watch next: Measure end-to-end task success vs. latency; release on-device VLMs for UI perception; publish guardrail APIs for payments, CAPTCHAs, account actions.
