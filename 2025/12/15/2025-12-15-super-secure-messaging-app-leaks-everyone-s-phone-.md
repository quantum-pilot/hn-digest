# “Super secure” messaging app leaks everyone's phone number

- Score: 474 | [HN](https://news.ycombinator.com/item?id=46279123) | Link: https://ericdaigle.ca/posts/super-secure-maga-messaging-app-leaks-everyones-phone-number/

### TL;DR

A researcher found Freedom Chat returning every default-channel member’s plaintext six-digit PIN in a 1,519-entry API response. Its contact-discovery endpoint also accepted batches of 40,000 phone numbers without effective rate limiting, returning registered numbers and user IDs. Over 27 hours, the researcher enumerated North American numbers and joined those IDs to channel records, linking users’ phone numbers and PINs. Freedom Chat said PINs permit account login but not restoration of past messages, and reported patching both issues before publication.

### Comment pulse

- Overbroad object serialization likely exposed sensitive fields → APIs should explicitly allowlist response properties and hash authentication secrets.
- Phone-number discovery is a recurring messaging vulnerability; rate limits help but distributed enumeration can still bypass simplistic controls.
- Some praise privacy-preserving lookup designs, while others argue secure messaging should avoid phone-number identity entirely.

### LLM perspective

- View: Encryption did not compensate for ordinary authorization, serialization, secret-storage, and abuse-control failures around it.
- Impact: Users faced account takeover and identity exposure even if historical message contents remained encrypted.
- Watch next: Independent retesting, PIN resets, breach notifications, endpoint limits, audit results, and removal of plaintext secrets.
