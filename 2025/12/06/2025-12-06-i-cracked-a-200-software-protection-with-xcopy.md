# I cracked a $200 software protection with xcopy

- Score: 78 | [HN](https://news.ycombinator.com/item?id=46170060) | Link: https://www.ud2.rip/blog/enigma-protector/

### TL;DR

A researcher examining an Enigma Protector-wrapped audio-plugin installer initially analyzes packing, local license verification, hardware binding, and apparent RSA-signed keys. The decisive finding is simpler: protection covers only the installer, while the installed VST and sound data contain no runtime license check and work when copied elsewhere. The author presents this as a threat-modeling failure rather than broken cryptography. Commenters challenge the “cracked protection” framing, noting Enigma itself functioned, the plugin creator may lack development expertise, and avoiding runtime DRM can reduce live-performance failures.

### Comment pulse

- Runtime checks would protect the payload—counterpoint: they can add support risk and instability for legitimate performers.
- Critics say the target was a solo musician’s inexpensive plugin, making the mocking tone and product identification disproportionate.
- Aggressive DRM can discourage purchases and motivate reversing, even when simple deterrence was the creator’s actual goal.

### LLM perspective

- View: The failure sits at the integration boundary, where strong controls guard the wrong asset.
- Impact: Developers can pay for sophisticated DRM yet receive only a one-time installation gate.
- Watch next: Payload-side validation, offline-failure behavior, performance costs, and documentation that distinguishes configuration from guarantees.
