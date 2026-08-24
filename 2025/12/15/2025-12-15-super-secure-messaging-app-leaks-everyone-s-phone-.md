# “Super secure” messaging app leaks everyone's phone number

- Score: 474 | [HN](https://news.ycombinator.com/item?id=46279123) | Link: https://ericdaigle.ca/posts/super-secure-maga-messaging-app-leaks-everyones-phone-number/

### TL;DR

Security testing of Freedom Chat found that its default channel returned plaintext six-digit account PINs for all 1,519 members, while an unthrottled contact-discovery API accepted 40,000 numbers per request. In roughly 27 hours, the researcher enumerated registered North American phone numbers, linked their user IDs to exposed PINs, and defeated the login safeguard for users who remained in that channel. Messages appeared properly encrypted through Seald. The company said PINs cannot restore message history, reported patches after disclosure, and promised additional audits.

### Comment pulse

- Commenters blamed default serialization or raw dictionaries for leaking fields; they also noted that storing PINs unhashed compounded the mistake.
- Signal’s protected discovery drew praise — counterpoint: several argued truly private messengers should avoid mandatory phone-number identities altogether.
- Engineers called missing rate limits elementary, while others warned distributed querying can evade simple throttles and secure development fails at many small edges.

### LLM perspective

- View: Encryption did not fail; surrounding identity, serialization, and abuse-control design nullified an otherwise encrypted messaging path.
- Impact: Exposed users faced account takeover risk, while the relaunch inherited its predecessor’s credibility problem.
- Watch next: Patch verification, forced PIN resets, hashed credential storage, enumeration defenses, independent audits, and limits on channel-member data.
