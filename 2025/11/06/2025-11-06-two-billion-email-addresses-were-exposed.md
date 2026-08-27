# Two billion email addresses were exposed

- Score: 281 | [HN](https://news.ycombinator.com/item?id=45839901) | Link: https://www.troyhunt.com/2-billion-email-addresses-were-exposed-and-we-indexed-them-all-in-have-i-been-pwned/

### TL;DR

Have I Been Pwned indexed Synthient’s aggregated credential-stuffing corpus containing 1.96 billion unique email addresses and 1.3 billion unique passwords, including 625 million passwords new to Pwned Passwords. This is not a single Gmail breach: roughly 394 million addresses were Gmail accounts, and sampled pairs included old or mismatched credentials as well as some still-valid ones. HIBP keeps email and password lookup separate, supports anonymous password checks, and is notifying affected subscribers gradually after a resource-intensive import.

### Comment pulse

- Commenters stressed unique passwords, password managers, multifactor authentication, and passkeys rather than trying to identify one originating breach.
- Privacy concerns about password lookup eased after discussion clarified the service’s hashed range-query design and separation from email addresses.

### LLM perspective

- View: The scale measures accumulated credential reuse and aggregation, not one fresh compromise of two billion accounts.
- Impact: Users and services receive another signal to retire reused credentials and strengthen authentication.
- Watch next: Notification completion, credential rotations, corpus provenance, false associations, and Pwned Passwords API payload growth.
