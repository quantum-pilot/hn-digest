# Swiss e-voting pilot can't count 2,048 ballots after decryption failure

- Score: 142 | [HN](https://news.ycombinator.com/item?id=47334982) | Link: https://www.theregister.com/2026/03/11/swiss_evote_usb_snafu/

### TL;DR

Basel-Stadt suspended its e-voting pilot after officials could not decrypt 2,048 ballots from Switzerland’s March 8 referendums: three USB keys with the correct codes all failed, despite expert help. The affected votes were under 4% of the canton’s total and could not change outcomes, but certification was delayed, criminal proceedings began, and an external investigation was commissioned. Other cantons using Swiss Post’s system were unaffected. Commenters favor voter-verifiable paper because manual processes preserve recountability, distributed observation, and a fraud scale constrained by human effort.

### Comment pulse

- Availability is part of election integrity → perfectly encrypted ballots still disenfranchise voters if operational key handling makes them unreadable.
- Paper separates eligibility from secrecy → officials authenticate a voter, then anonymous ballots enter an observable count.
- Cryptography can support private verification → counterpoint: remote authentication, endpoint compromise, and public trust remain difficult beyond mathematical proofs.

### LLM perspective

- **View:** A voting system needs a tested recovery path that cannot silently alter ballots or depend on one vendor.
- **Impact:** Overseas and disabled voters lose convenience while Basel-Stadt pauses the pilot through December.
- **Watch next:** Root cause, key-ceremony logs, ballot recoverability, independent findings, and revised fallback procedures.
