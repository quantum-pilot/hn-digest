# Google API keys weren't secrets, but then Gemini changed the rules

- Score: 1194 | [HN](https://news.ycombinator.com/item?id=47156925) | Link: https://trufflesecurity.com/blog/google-api-keys-werent-secrets-but-then-gemini-changed-the-rules

## TL;DR
Google long told developers that `AIza...` API keys for Maps, Firebase, etc. were *not* secrets and safe to ship in client code. When a project later enables Gemini (Generative Language API), those same keys silently gain access to Gemini endpoints: private uploaded files, cached LLM context, and billable model calls. Truffle Security scanned Common Crawl and found 2,863 such live keys, including Google’s own. Google is now blocking “leaked” keys and tightening defaults, but fully fixing legacy keys may be highly disruptive.

---

## Comment pulse
- Gemini + AI Studio defaults → people ship “proxied” apps that still expose powerful, expensive models; proxy gives a false sense of security.  
- Remediation dilemma → safely revoking Gemini from old or all keys risks breaking large fractions of traffic—counterpoint: Gemini isn’t auto-enabled, a project owner must turn it on.  
- Real-world leakage → hardcoded keys in Android images and GitHub repos already worked against Gemini until recently; older Firebase/Maps keys became risky once Gemini was enabled.

---

## LLM perspective
- View: This is a textbook retroactive privilege escalation from reusing one key type for both public identification and sensitive authentication.  
- Impact: Cloud providers must redesign auth boundaries; developers need stricter project separation, key scoping, and continuous secret scanning.  
- Watch next: Whether Google auto-scopes all existing keys, issues broad customer advisories, or introduces distinct “publishable vs secret” Gemini credentials.
