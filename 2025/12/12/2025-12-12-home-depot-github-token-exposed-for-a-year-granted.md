# Home Depot GitHub token exposed for a year, granted access to internal systems

- Score: 260 | [HN](https://news.ycombinator.com/item?id=46247000) | Link: https://techcrunch.com/2025/12/12/home-depot-exposed-access-to-internal-systems-for-a-year-says-researcher/

### TL;DR
Home Depot left a GitHub access token publicly exposed for roughly a year, apparently via an employee’s mistake. The token gave read/write access to hundreds of private repos plus cloud infrastructure tied to order fulfillment, inventory, and CI/CD pipelines—essentially a software supply-chain foothold. Researcher Ben Zimmermann responsibly reported it but was ignored until he went to TechCrunch, after which the token was revoked. Home Depot has no formal vulnerability disclosure channel and hasn’t said whether logs show any malicious use.

---

### Comment pulse
- Corporate silence → Once media gets involved, everything routes through legal, producing non-answers; seen as rational risk management — counterpoint: public postmortems can reduce long-term legal and trust damage.  
- Key hygiene worry → Personal anecdotes show mixed vendor responses to leaked API keys; “vibe coding” and LLM tools increase accidental leaks and confusion about where secrets live.  
- How to handle secrets → For self-hosting, suggestions include env files plus IP restrictions, SOPS with age, cloud-native secret stores, or 1Password with API integration.

---

### LLM perspective
- View: This incident is a basic token-leak failure compounded by missing VDP processes and unresponsive corporate security culture.  
- Impact: Increases pressure on large enterprises to offer clear security reporting paths and automated token scanning/revocation across developer tooling.  
- Watch next: Regulatory moves on mandatory disclosure programs and logging, and broader adoption of secret-scanning in IDEs, CI, and code-hosting platforms.
