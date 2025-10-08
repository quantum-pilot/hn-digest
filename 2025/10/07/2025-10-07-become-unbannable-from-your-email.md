# Become unbannable from your email

- Score: 181 | [HN](https://news.ycombinator.com/item?id=45509243) | Link: https://karboosx.net/post/PJOveGVa/become-unbannable-from-your-emailgmail

- TL;DR
    - The post argues email is your real digital address: lose it and you lose access everywhere. Solution: own a domain, host mail with a reputable provider offering catch‑all, and continuously forward copies to a local server/NAS so you can repoint MX and keep reading mail even if the provider bans you. HN adds caveats: registrars can fail—use ICANN‑regulated ones and separate registrar/host; forwarding relays spam—do periodic IMAP backups; catch‑all/plus help but some sites block them; plan migrations and 2FA (multiple keys).

- Comment pulse
    - Own your domain, but registrars add a failure point → pick ICANN-regulated registrar, separate registrar/host, keep local backups; ICANN disputes can rescue .com/.net.
    - Infinite addresses via catch-all/plus are great for filtering → some companies block brand names or balk at unusual emails; consider Spamgourmet or Gmail plus addressing.
    - Forwarding-as-backup can relay spam and break under bans → prefer periodic IMAP backups integrated with your backup system — counterpoint: MX repointing restores future mail.

- LLM perspective
    - View: Aim for email portability and continuity; combine domain ownership with provider redundancy and routine restore tests.
    - Impact: Individuals avoid lockouts; teams gain leverage over vendors and smoother incident recovery.
    - Watch next: Trial MX failover, schedule IMAP backups, enforce SPF/DKIM/DMARC alignment, register two FIDO2 keys, and document recovery contacts.
