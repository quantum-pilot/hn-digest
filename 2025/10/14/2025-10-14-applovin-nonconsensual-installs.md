# AppLovin nonconsensual installs

- Score: 113 | [HN](https://news.ycombinator.com/item?id=45584226) | Link: https://www.benedelman.org/applovin-nonconsensual-installs/

- TL;DR
    - Ben Edelman presents decompiled AppLovin SDK/JS and partner helper code, plus 208 matching complaints, showing ads can trigger Android app installs without explicit consent—via auto-install, countdowns, or “InstallOnClose” after tapping tiny Xs. He argues OEM/carrier install helpers (Samsung, T‑Mobile) granted OOBE-time rights that were used broadly, with no time checks. This conflicts with AppLovin’s “explicit user choice” claims and raises legal/security risks. HN discusses platform blame (Android/carriers), mitigations (iOS, Device Protection, MDM), and the financial incentives behind AppLovin’s high margins.

- Comment pulse
    - Carrier/OEM helpers enable ad-triggered installs → OOBE permissions lack time limits; elevated rights allow OTA “direct download.” — counterpoint: iOS blocks; Android Device Protection/MDM help.
    - Single-tap or mis-tap risk → tiny close targets and forced flows undermine consent; broad install surface threatens many Android users.
    - Incentives sustain behavior → AppLovin’s 45–65% margins make paid carrier deals plausible; investors question long-term legality and reputational risk.

- LLM perspective
    - View: Evidence triangulation is strong; the weak link is OEM/carrier intent versus AppLovin’s usage beyond OOBE.
    - Impact: Expect Android policy and Play Protect updates; OEM/carrier audits; advertisers and developers reassess SDKs to avoid liability.
    - Watch next: Technical repros, CVEs, and regulator inquiries; Samsung/T-Mobile statements; AppLovin SDK/version diffs and deprecations.
