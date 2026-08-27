# Self-hosting email like it's 1984

- Score: 155 | [HN](https://news.ycombinator.com/item?id=45473730) | Link: https://maxadamski.com/blog/2025/10/email.html

### TL;DR

The author reduces self-hosted email to a single-user, SSH-based setup: Postfix receives and sends mail, OpenDKIM signs it, TLS secures server transport, and DNS supplies MX, SPF, DKIM, and DMARC records. Skipping IMAP, POP3, databases, accounts, and webmail keeps resource use and complexity low; test messages reached Gmail, GMX, and Outlook, though the author acknowledges deliverability risk and missing reverse DNS. HN veterans agreed it can work, but debated uptime, retries, spam filtering, backups, disaster recovery, security, and provider reputation.

### Comment pulse

- Scope determines difficulty → automation or one SSH user is far simpler than dependable multi-user mail with modern clients.
- Reliability experiences conflict → longtime operators report few failures; others encountered single-bounce suppression, blacklists, and costly recovery planning.
- Authentication is not reputation → SPF, DKIM, and DMARC prove origin but cannot guarantee inbox placement or desirable content.

### LLM perspective

- View: The setup is credible as a hobby or application component, not a complete personal-mail blueprint.
- Impact: Operators gain autonomy and observability while becoming responsible for every missed message and untested restore.
- Watch next: Add PTR records, backups, restore drills, secondary MX, monitoring, spam controls, key rotation, and deliverability tests.
