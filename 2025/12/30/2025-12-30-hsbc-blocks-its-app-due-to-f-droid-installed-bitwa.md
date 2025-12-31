# HSBC blocks its app due to F-Droid-installed Bitwarden

- Score: 231 | [HN](https://news.ycombinator.com/item?id=46431453) | Link: https://mastodon.neilzone.co.uk/@neil/115807834298031971

### TL;DR
HSBC’s Android banking app is reportedly refusing to run if Bitwarden installed via F-Droid is present, likely using Google’s Play Integrity/SafetyNet plus app-enumeration permissions. This shows how banking apps now depend on Google’s device-attestation and blacklist mechanisms, which can quietly punish alternative app stores and rooted/custom ROM users. Hacker News discussion widens to de-banking and sanctions, user workarounds (separate “clean” phones, friendlier banks), and the underused potential of PWAs as a way around app-store and attestation lock-in.  
*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Mobile banking tied to Google integrity checks → financial access can be indirectly gated by Google’s blacklist and US-centric sanctions pressure, eroding user freedom—counterpoint: laws, banks, and governments also choose this setup.
- Users adapt rather than fight → some keep a locked-down iPhone or stock Android solely for banking while using GrapheneOS/rooted devices for everything else; others switch to banks like Monzo that warn but still allow rooted devices.
- Technical enforcement is broad and opaque → banks can request QUERY_ALL_PACKAGES to inspect installed apps “for security,” mis-detect benign features (e.g., second screens, password managers), and block devices; PWAs could sidestep this but lack mainstream adoption and UX polish.

---

### LLM perspective
- View: Banking apps using Play Integrity plus full app visibility effectively outsource risk policy to Google, with minimal transparency or appeal.
- Impact: Privacy-focused users, alternative app store users, and people on non-standard devices face exclusion from essential financial services.
- Watch next: Regulatory pushes for web access to core banking, scrutiny of app blacklists, and technical standards for auditable attestation behavior.
