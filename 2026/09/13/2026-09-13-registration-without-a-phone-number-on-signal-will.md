# Registration without a phone number on Signal will use zero-knowledge proofs

- Score: 258 | [HN](https://news.ycombinator.com/item?id=49689048) | Link: https://community.signalusers.org/t/registration-without-a-phone-number/2222?page=10

### TL;DR

Signal forum participants point to Android commits adding basic registration and login for numberless accounts, username setup, password-manager support, and a new zero-knowledge credential. Signal staff explain that zero-knowledge proofs can validate properties such as username length and character set without revealing the username. The supplied discussion does not establish a release date, final payment flow, or whether existing phone-number accounts can unlink. Commenters welcome numberless registration but question Google Play billing, backend transparency, centralized infrastructure, and what privacy guarantees the design actually provides.

### Comment pulse

- Zero-knowledge proofs can validate hidden attributes → Signal staff cite username constraints alongside existing private group and payment-related uses.
- Spam resistance may require payment → commenters infer Google Play billing from commits but want options independent of Google accounts.
- Implementation details remain incomplete → users ask when registration ships, whether existing accounts can unlink, and what trust assumptions remain.

### LLM perspective

- View: The commits indicate active development, not a finalized privacy model or generally available numberless registration feature.
- Impact: Removing phone-number enrollment could improve pseudonymity while shifting abuse prevention and account recovery toward credentials and payments.
- Watch next: Seek official protocol documentation, release status, non-Google payment paths, migration rules, recovery design, and independent cryptographic review.
