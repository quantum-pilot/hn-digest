# Self-hosting email like it's 1984

- Score: 155 | [HN](https://news.ycombinator.com/item?id=45473730) | Link: https://maxadamski.com/blog/2025/10/email.html

TL;DR
Guide to a lean self-hosted mail server: Postfix + OpenDKIM, no IMAP/POP or webmail, STARTTLS with a cert on the MX host, and DNS for SPF/DKIM/DMARC. PTR is advised; the author still delivers to Gmail/GMX/Outlook and uses SSH + mailx to operate. Biggest caveat: deliverability risk. HN debate: longtime admins report low maintenance and independence; others cite backups/DR, always-on expectations, and greylisting slowing signups. Starter stacks (Mail-in-a-Box, Stalwart) ease setup; big providers’ filtering remains inconsistent.

Comment pulse
- Self-hosting as hobby → low maintenance, control, logs help; multi‑decade stability reported — counterpoint: backups/DR/security burdens can outweigh savings for critical mail.
- Uptime and retries → some report big senders bouncing quickly; others cite greylisting working fine and 99% deliverability with correct SPF/DKIM and reliable hosts.
- Getting started tools → Mail‑in‑a‑Box and Stalwart simplify setup; caveat: MIAB greylisting delays signup/2FA emails and lacks easy per‑user overrides.

LLM perspective
- View: SMTP‑only self‑hosting suits solo apps; complexity concentrates in client access (IMAP/webmail), spam defenses, PTR/IP reputation, and certificate automation.
- Impact: Lower costs and more autonomy; but you assume backups, monitoring, patching, and incident response obligations previously handled by providers.
- Watch next: MTA‑STS/TLS‑RPT and ARC uptake, Gmail/Outlook rule shifts, clean‑IP options, turnkey stack releases, and retry policies from major providers.
