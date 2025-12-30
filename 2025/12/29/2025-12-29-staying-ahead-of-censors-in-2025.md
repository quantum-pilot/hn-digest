# Staying ahead of censors in 2025

- Score: 228 | [HN](https://news.ycombinator.com/item?id=46417844) | Link: https://forum.torproject.org/t/staying-ahead-of-censors-in-2025-what-weve-learned-from-fighting-censorship-in-iran-and-russia/20898

### TL;DR
Tor’s anti-censorship team spent 2025 hardening access from heavily filtered networks in Iran and Russia. They deployed in-country monitoring to track blocking in real time, strengthened Snowflake (better NAT handling, metrics, and staging), and prepared Conjure, which hides bridges in ISP address space using realistic DNS/AMP bootstrap methods. In Russia, WebTunnel’s HTTPS-mimic transport plus dynamic bridge distribution (notably via Telegram and rdsys) became crucial as allowlists and rapid IP blocking intensified.

---

### Comment pulse
- Western democracies also restrict online speech via arrests and hate-speech laws → critics argue this is censorship too; defenders stress it’s incomparable to Iran/Russia repression.  
- Focus on Iran/Russia is technical → Tor fights network-level blocking there, not legal regulation in EU/UK — counterpoint: funding and politics may influence what’s highlighted.  
- WebTunnel/SNI imitation seen as broadly useful for resisting corporate tracking; others want easier exit-node/region selection to combat geo-blocking without manual config.

---

### LLM perspective
- View: The trend is from generic obfuscation toward high-fidelity mimicry of normal HTTPS and mainstream services.  
- Impact: Raises censorship costs by forcing regimes to risk collateral damage to popular platforms and ISP address space.  
- Watch next: Real-world robustness of Conjure, sustainability of Telegram-based bridge distribution, and usability improvements like safer exit-node selection.
