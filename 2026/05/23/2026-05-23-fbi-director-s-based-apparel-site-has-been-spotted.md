# FBI director's Based Apparel site has been spotted hosting a 'ClickFix' attack

- Score: 185 | [HN](https://news.ycombinator.com/item?id=48243293) | Link: https://www.pcmag.com/news/kash-patels-apparel-site-is-trying-to-trick-visitors-into-installing-malware

- TL;DR  
An apparel website tied to FBI director Kash Patel, BasedApparel.com, was briefly serving a sophisticated “ClickFix” malware scam targeting macOS users. Visitors sometimes saw a fake Cloudflare “verify you are human” page instructing them to copy‑paste a short “verification” string into Terminal. The button actually copied an obfuscated AppleScript command that steals browser credentials and cryptocurrency wallet data, then exfiltrates it. Researchers say this likely stems from a compromise of the site’s WordPress stack; Apple’s newest macOS now warns against such pasted commands.

- LLM perspective  
  - View: This illustrates how modest, politically-linked WordPress sites become high‑value distribution vectors for credential‑stealing malware via UI deception.  
  - Impact: Mac users face growing social‑engineering attacks that bypass Gatekeeper by convincing them to self‑execute opaque commands in trusted tools.  
  - Watch next: Wider deployment and bypasses of macOS paste‑protection, and whether browsers or Cloudflare add explicit warnings around Terminal instructions.
