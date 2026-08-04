# FBI director's Based Apparel site has been spotted hosting a 'ClickFix' attack

- Score: 185 | [HN](https://news.ycombinator.com/item?id=48243293) | Link: https://www.pcmag.com/news/kash-patels-apparel-site-is-trying-to-trick-visitors-into-installing-malware

### TL;DR

BasedApparel.com, a merchandise site co-created by FBI director Kash Patel before his appointment, appears to have been compromised with a macOS ClickFix campaign. A fake Cloudflare verification page copied an obfuscated AppleScript command while displaying harmless text, then instructed visitors to paste it into Terminal. The payload, flagged by 27 antivirus engines, allegedly stole Chromium credentials and cryptocurrency-wallet data for exfiltration. HN commenters clarified that the site was a victim rather than the attacker, while raising conflict-of-interest concerns and debating whether other operating systems were likely targeted through user-agent-specific instructions.

### Comment pulse

- Readers argued public officials should divest businesses because politically driven traffic makes personal commercial sites attractive targets and possible security liabilities.
- Some warned that terminal-copy attacks may vary by user agent — counterpoint: the documented sample and payload were macOS-specific.
- Chromium targeting prompted speculation that Safari’s Keychain integration complicates theft, though the supplied discussion offered no confirmed explanation.

### LLM perspective

- View: ClickFix bypasses software exploits by turning clipboard deception and user obedience into the execution chain.
- Impact: Brand trust and fake security interfaces can convert ordinary browsing into credential and wallet compromise.
- Watch next: Site remediation, compromise vector, campaign scope, Windows variants, stolen-data destinations, and disclosure from Based Apparel.
