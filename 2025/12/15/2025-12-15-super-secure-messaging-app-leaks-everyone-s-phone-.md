# “Super secure” messaging app leaks everyone's phone number

- Score: 474 | [HN](https://news.ycombinator.com/item?id=46279123) | Link: https://ericdaigle.ca/posts/super-secure-maga-messaging-app-leaks-everyones-phone-number/

### TL;DR  
A rebranded “super secure” MAGA messaging app, Freedom Chat (from the failed Converso team), exposed users’ security PINs and phone numbers via basic API flaws. Channel membership responses returned each member’s plaintext login PIN, and a WhatsApp-style contact-discovery endpoint let anyone bulk-enumerate all registered phone numbers with no rate limiting. The researcher combined both leaks to map most users’ phone numbers to their PINs, defeating the app’s main security control. HN discussion focuses on sloppy backend practices, unsafe serialization, and poor contact-discovery design.

---

### Comment pulse

- Bulk-leaked PINs → result of opt‑out serializers or careless JS dicts that auto-include all fields; compounded by storing PINs in plaintext instead of using proper password hashing.  

- Contact discovery is hard → naive number→UID APIs keep repeating old WhatsApp/Telegram mistakes; commenters contrast Signal’s private lookup and propose pairwise-hash schemes—counterpoint: phone numbers themselves are a bad identifier.  

- Most “hacks” are boring → missing rate limiting, lack of basic security literacy, and no routine pentesting dominate; scanners help catch this—counterpoint: rate limiting alone is bypassable with distributed IPs.

---

### LLM perspective

- View: Secure-messaging claims are meaningless if trivial API and data-model mistakes leak identity and authentication secrets.  

- Impact: Small niche app, but the pattern—crypto veneer over insecure backends—is widespread in “privacy” startups.  

- Watch next: Frameworks should default to safe serialization, mandatory hashing, and rate limiting; app stores could require independent security reviews for “secure chat” apps.
