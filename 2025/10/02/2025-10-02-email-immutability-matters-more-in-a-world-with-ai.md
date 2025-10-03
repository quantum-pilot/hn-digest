# Email immutability matters more in a world with AI

- Score: 142 | [HN](https://news.ycombinator.com/item?id=45453135) | Link: https://www.fastmail.com/blog/not-written-with-ai/

- TL;DR
    - AI makes editing online history cheap, so email’s per-recipient copies look safer. HN debates how immutable email really is: remote content and Gmail’s dynamic messages can change post-delivery. Some propose provider-side mitigations; others think the threat is overblown. Security-minded commenters advocate cryptographic integrity and authentication, while another thread widens to provenance for photos/video, highlighting bypasses and likely platform lock-in. A side note flags Fastmail’s own AI use, framed with standard privacy and human-in-the-loop assurances.
    - Content unavailable; summarizing from title/comments.

- Comment pulse
    - Email isn’t immutable → remote assets and AMP emails can change later; providers could snapshot at open — counterpoint: clients block remotes; senders embed.
    - Use cryptographic protection → PGP/S/MIME signatures ensure body integrity; DKIM/SPF/DMARC indicators help detect tampering and spoofing.
    - Provider hypocrisy concern → Fastmail also uses AI; policies promise privacy, human review, bias checks, and appeals, seen by some as marketing boilerplate.

- LLM perspective
    - View: Treat message bodies and dependencies separately; freeze or strip externals, verify bodies with signatures.
    - Impact: Email providers add snapshotting, disable AMP by default; enterprises standardize S/MIME or PGP for official notices.
    - Watch next: Gmail AMP trajectory, IETF integrity extensions, C2PA provenance adoption across cameras and social platforms.
