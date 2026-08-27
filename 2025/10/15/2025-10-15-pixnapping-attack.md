# Pixnapping Attack

- Score: 289 | [HN](https://news.ycombinator.com/item?id=45588594) | Link: https://www.pixnapping.com/

### TL;DR

Researchers describe Pixnapping, an Android pixel-stealing attack combining intents, graphical operations, timing measurements, and the GPU.zip side channel. Their demonstrations on five Google and Samsung phones running Android 13–16 recovered visible information, including Authenticator codes in under 30 seconds, from an app declaring no permissions. They say Google's first patch was bypassed and another was planned. Commenters debated missing network controls, practical targeting constraints, disclosure timing, and possible app-level defenses that would degrade usability.

### Comment pulse

- Android's implicit capabilities drew criticism → commenters proposed tighter background and network controls, though intents complicate that model.
- Practical exploitation has constraints → rapidly changing codes require known fonts, positions, and carefully selected pixels.
- App mitigations remain speculative → hiding, moving, or visually varying secrets could raise attack cost but harm usability.

### LLM perspective

- View: Permissionless cross-app pixel leakage exposes a boundary Android's user-facing permission model does not represent.
- Impact: Visible secrets become vulnerable even when applications correctly prevent ordinary screenshots or direct data access.
- Watch next: Verify December's patch, vendor coverage, bypass resistance, and effective mitigations for authentication applications.
