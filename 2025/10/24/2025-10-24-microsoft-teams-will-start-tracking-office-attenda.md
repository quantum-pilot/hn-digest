# Microsoft Teams will start tracking office attendance

- Score: 76 | [HN](https://news.ycombinator.com/item?id=45698930) | Link: https://www.tomsguide.com/computing/office-software/microsoft-teams-will-start-snitching-to-your-boss-when-youre-not-in-the-office-and-this-update-is-coming-in-december

TL;DR
Microsoft Teams will auto-mark employees as “in office” when devices connect to corporate Wi‑Fi, updating work location on Windows/macOS starting December 2025. It’s off by default, but tenant admins can enable it and require opt‑in. Detection likely uses IP/BSSID rather than spoofable SSIDs. HN debates its purpose: RTO enforcement and firing ammo vs. benign coordination. Skeptics cite Teams bloat and accuracy gaps (wired, VMs, VPNs) and note badges/backgrounds already indicate presence; others foresee broader surveillance creep.

Comment pulse
- It's about enforcement, not collaboration → creates a paper trail to justify RTO compliance and terminations. — counterpoint: Some see value for coworkers to find you onsite.
- Teams bloat/accuracy concerns → unnecessary network probing; unclear for wired devices, VMs; history of buggy features and confusing shortcuts.
- Easy to infer presence already → badges, backgrounds, and VPN use suffice; this feature suits smaller orgs lacking IT controls.

LLM perspective
- View: Auto-location can be useful; value hinges on purpose limitation, transparency, and opt-in verified by audit logs, not silent rollout.
- Impact: HR/Legal get another RTO metric; IT must map BSSIDs to buildings; expect conflicts with unions and EU privacy laws.
- Watch next: Admin controls granularity, spoofing resistance details, integration with badge systems, and whether reports feed Microsoft Viva/HRIS dashboards.
