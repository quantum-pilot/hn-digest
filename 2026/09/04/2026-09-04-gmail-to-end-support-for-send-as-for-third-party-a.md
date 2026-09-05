# Gmail to end support for "Send as" for third-party addresses, such as @yahoo.com

- Score: 186 | [HN](https://news.ycombinator.com/item?id=49565693) | Link: https://support.google.com/mail/answer/22370?hl=en

### TL;DR

Google says Gmail will stop supporting “Send as” for third-party addresses beginning January 2027, while Google Workspace aliases and other owned Gmail addresses remain unaffected. The documentation still describes today’s SMTP-based setup, leaving commenters divided over whether externally hosted custom domains are included; several cited separate guidance suggesting they are. Users who forward domain mail into personal Gmail may therefore need a new outbound-mail workflow or provider. Discussion favored owning a domain because changing providers then primarily requires updating DNS rather than changing addresses everywhere.

### Comment pulse

- Affected users described Gmail as their client for externally hosted domains and anticipated migrating their “home base.”
- Commenters disputed the scope because “third-party addresses” and the stated Workspace exceptions do not clearly settle externally hosted custom domains.
- Fastmail and other providers were popular suggestions—counterpoint: storage, price, and migration effort remain practical trade-offs.

### LLM perspective

- View: The deadline is clear, but Google’s wording leaves the most technically consequential custom-domain case insufficiently explicit.
- Impact: Users combining forwarding with Gmail’s outbound SMTP face workflow changes; Workspace aliases appear protected.
- Watch next: Google should publish a matrix covering personal Gmail, Workspace, external domains, mobile clients, forwarding, and SMTP relay.
