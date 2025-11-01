# AI scrapers request commented scripts

- Score: 175 | [HN](https://news.ycombinator.com/item?id=45773347) | Link: https://cryptography.dog/blog/AI-scrapers-request-commented-scripts/

- TL;DR
  - An admin traced waves of 404s to bots requesting a JavaScript file referenced only inside an HTML comment—evidence of scrapers regexing URLs and spoofing browser user‑agents while ignoring robots.txt. He frames this as a fingerprint to detect AI/data scrapers and outlines countermeasures: fail2ban IP blocks, hidden bait links, cautious decompression bombs, and serving poisoned data to taint LLM training (recent work suggests ~250 poisons can suffice). HN debates consent vs norms, costs bordering on DDoS, and how scrapers evade zip‑bombs and throttles.

- Comment pulse
  - Scraper operator view → Zip bombs seldom work; use Content-Length, byte caps, timeouts; avoid spoonfeeding; custom crawlers bypass throttles — counterpoint: serve huge files anyway.
  - Open server ≠ consent to mass scraping → robots.txt is etiquette; UA spoofing to bypass defenses breaks implied consent; others insist GET needs no permission.
  - Plaintext URL extraction > DOM parsing → vastly cheaper, explaining comment harvesting; some suggest baiting hidden links to auto-ban or poison models.

- LLM perspective
  - View: Comment-only URL requests are a strong heuristic; combine with other signals to avoid false positives.
  - Impact: Admins can automate bans and targeted poisoning; scraper operators will adapt UAs and parsers.
  - Watch next: Replicate 250-poison result; measure bait efficacy; push for bot identity attestation and enforcement beyond robots.txt.
