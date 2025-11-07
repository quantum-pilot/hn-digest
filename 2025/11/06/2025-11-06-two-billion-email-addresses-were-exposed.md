# Two billion email addresses were exposed

- Score: 281 | [HN](https://news.ycombinator.com/item?id=45839901) | Link: https://www.troyhunt.com/2-billion-email-addresses-were-exposed-and-we-indexed-them-all-in-have-i-been-pwned/

- TL;DR
    HIBP indexed 1.96B unique emails and 1.3B passwords (625M new) from Synthient’s credential‑stuffing lists—an aggregation from many breaches, not a Gmail leak. Verification with subscribers showed mostly old but some still‑active passwords; HIBP stores passwords separately and lets you check them anonymously via k‑anonymity. Processing required heavy Azure SQL scaling; Pwned Passwords hash‑range responses grew ~50%. Practical guidance: use a password manager, unique strong passwords or passkeys, and MFA. HN discusses ubiquity of exposure, credit freezes, opacity about which password, and a likely unreported Spotify incident.

- Comment pulse
    - Security hygiene focus → Use password managers, unique passwords, MFA; freeze credit to limit financial abuse — counterpoint: some primary emails remain clean after years.
    - Frustration about opacity → HIBP won’t reveal which password; rely on manager breach checks; admins avoid blanket resets for aggregate, years-old lists.
    - Suspicious gap → Unique Spotify-only email hit suggests unreported 2020 incident; credential stuffing vs partner leak remains unclear.

- LLM perspective
    - View: Credential stuffing data at this scale shows password reuse is still the dominant account-takeover vector.
    - Impact: Expect higher API payloads; more services should block known-breached passwords and accelerate passkey rollout.
    - Watch next: Company disclosures (e.g., Spotify), regulators’ responses, and measurable drops in stuffing success after password rotations.
