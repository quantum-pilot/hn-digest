# Chipotlai Max

- Score: 371 | [HN](https://news.ycombinator.com/item?id=48363765) | Link: https://github.com/cyberpapiii/chipotlai-max

## TL;DR

Chipotlai Max is a meme fork of the OpenCode coding agent that reroutes requests through a locally run proxy to Chipotle’s “Pepper” customer-support AI, effectively using Chipotle’s cloud budget for free code generation. The repo ships Pepper as the default OpenAI-compatible model, with Chipotle branding and an explicit “this violates ToS” disclaimer, and invites contributors to reverse‑engineer other retail chatbots. HN discussion quickly shifts to CFAA risk, ethics of commandeering corporate compute, doubts about Pepper’s true capabilities, and alternatives using legal free/fast LLMs.

---

## Comment pulse

- This likely falls under CFAA “misuse of computing resources” → reverse‑engineering and off‑label use of a production bot could bring criminal, not just civil, consequences. — counterpoint: some see it as a clever educational stunt.

- Several users couldn’t reproduce Pepper’s viral coding feats → suspect cherry‑picked or faked screenshots; similarly, Llama 3 8B is reported as too weak for serious coding despite high token speed.

- People riff on “free compute” agents → imagine self‑preserving AIs that forage for tokens via support chats and trials; others note legal options like OpenRouter’s free providers instead.

---

## LLM perspective

- View: A sharp parody of AI hype that also exposes how fragile many production chatbots’ security and rate‑limiting still are.

- Impact: Encourages hobbyist experimentation with OpenAI-compatible proxies, but also pressures companies to lock down customer-service AIs and add authentication.

- Watch next: Whether similar projects migrate toward officially free APIs or local small models once legal risk and patches make “stolen compute” untenable.
