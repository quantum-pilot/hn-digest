# Email obfuscation: What works in 2026?

- Score: 334 | [HN](https://news.ycombinator.com/item?id=47609694) | Link: https://spencermortensen.com/articles/email-obfuscation/

### TL;DR
Mortensen runs a honeypot page where each obfuscation technique protects a unique email, and spam to those addresses reveals which methods fail. With data from ~400 spammers, plain text and unprotected `mailto:` links offer 0% protection, but even very simple tricks (HTML entities, comments, URL-encoding, CSS `display:none`, SVG via `<object>`, JS-based conversions/AES, or user-interaction reveals) block 95–100% of harvesters. Classic “AT/DOT”, images, bidi/CSS content, etc. are rejected as they harm usability or accessibility.

---

### Comment pulse
- Plain email sometimes ‘fine’ → Many report few spam issues due to good provider filters or low-profile sites; others see thousands/month on public corporate addresses.  
- Scrapers stay dumb → Commenters suspect many bots just scan raw HTML for '@', not parse entities/JS, explaining why basic encodings still defeat ~95%.  
- Alternative defenses → Suggestions include per-recipient aliases on own domain or strict whitelists; obfuscation seen as complementary, especially after visible spam spike from new sites.

---

### LLM perspective
- View: For personal sites, combining one simple HTML/CSS trick with provider spam filtering likely yields excellent cost-benefit.  
- Impact: JS-dependent schemes may erode as more scrapers use headless browsers; CSS `display:none` and SVG `<object>` are more durable.  
- Watch next: Measure if LLM-assisted spam bypasses filters faster than harvesters improve, making on-page address protection more important again.
