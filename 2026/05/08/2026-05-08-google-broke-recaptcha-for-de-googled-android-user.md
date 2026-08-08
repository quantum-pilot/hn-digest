# Google broke reCAPTCHA for de-googled Android users

- Score: 471 | [HN](https://news.ycombinator.com/item?id=48067119) | Link: https://reclaimthenet.org/google-broke-recaptcha-for-de-googled-android-users

### TL;DR

Google’s newer reCAPTCHA flow can require challenged Android users to scan a QR code using Google Play Services 25.41.30 or later. Phones running GrapheneOS or other de-Googled systems without that proprietary framework then fail verification, potentially blocking access to sites that adopt the system. iOS 16.4+ completes the flow without an extra Google app. The article portrays this as ecosystem control disguised as fraud prevention; commenters worry it resembles remote attestation that could enable device correlation, while site operators immediately sought less invasive anti-spam alternatives.

### Comment pulse

- Critics reject hardware-backed humanity checks even on certified phones, fearing internet access will become conditional on a vendor-controlled identity signal.
- GrapheneOS users report banks and services already refusing them; some switch providers or self-host rather than restore Google dependencies.
- Operators need bot defenses — counterpoint: proprietary mobile software as a web prerequisite excludes unsupported phones and alternative Android systems.

### LLM perspective

- The key unknown is whether this uses hardware attestation, account signals, behavioral telemetry, or some combination.
- Measure abuse reduction against challenge failures, privacy exposure, accessibility, and vendor lock-in before enabling it.
- Watch documentation changes, independent traffic analysis, regulator scrutiny, and deployment by large edge providers.
