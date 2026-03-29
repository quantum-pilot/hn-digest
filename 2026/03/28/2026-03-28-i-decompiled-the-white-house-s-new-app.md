# I decompiled the White House's new app

- Score: 338 | [HN](https://news.ycombinator.com/item?id=47555556) | Link: https://thereallo.dev/blog/decompiling-the-white-house-app

- TL;DR  
    - The decompiler-based review of the new White House Android app finds a typical React Native/Expo marketing portal backed by WordPress, but with worrying choices for a government app: a WebView script that strips cookie banners, GDPR dialogs, and some paywalls from any external site; deeply integrated OneSignal analytics with ready-to-enable frequent GPS tracking and detailed user profiling; and unsandboxed third-party JavaScript loaded from GitHub Pages, Elfsight, and other vendors, all without certificate pinning or clean production hardening.

- Comment pulse  
    - Location-tracking concerns → Commenters note the app doesn’t request location permissions on their devices, suggesting dead SDK code, rollout differences, or that behavior changed in a just-released update.  
    - Boilerplate consultancy app → Many see this as generic agencyware using standard OneSignal-heavy templates; R8 often leaves unused RN/Expo code in place — counterpoint: for a White House app, “just boilerplate” isn’t a defense.  
    - Cert pinning debate → Some argue lack of pinning is overblown; others stress CA compromise, corporate MDM roots, or hostile networks make pinning more valuable for sensitive apps.

- LLM perspective  
    - View: This app exemplifies how plug-and-play SDK stacks quietly import aggressive tracking and brittle supply chains into high-profile apps.  
    - Impact: Government users, staffers, and journalists may unknowingly expose behavior, location, and metadata to multiple private vendors.  
    - Watch next: Independent audits diffing app versions, checking actual runtime permission prompts, and cataloging third-party endpoints would clarify real-world risk.
