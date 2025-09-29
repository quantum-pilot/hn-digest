# Bonding twelve 56K modems together to set dial-up broadband records

- Score: 112 | [HN](https://news.ycombinator.com/item?id=45400828) | Link: https://www.tomshardware.com/networking/enthusiasts-bond-twelve-56k-dial-up-modems-together-to-set-dial-up-broadband-records-a-dozen-screeching-boxes-achieve-record-668-kbps-download-speeds

- TL;DR
  - Two tinkerers from The Serial Port bonded twelve 56K modems via Multilink PPP on a Windows XP box—using multi‑port serial cards and a Cisco gateway bridging analog lines to PRI—to hit 668.8 kbps and stream 240p YouTube. Windows ME stalled at two ports; XP scaled and dialed all links simultaneously. HN reminisces about 4‑modem EQL/MLPPP and even bonded ADSL/T1, notes that true 56k needs a digital path (G.711 or PRI), and debates cost/latency trade‑offs versus satellite and rural broadband policy failures.

- Comment pulse
  - MLPPP/EQL bonding works beyond nostalgia → 4×56k on Linux EQL, ISDN/T1 on Cisco, and even bonded ADSL1 delivered multi‑megabit links in the 2000s.
  - Modems over VoIP require a digital path → 56k depends on T1/PRI; use G.711, disable echo/silence; 28.8–44k achievable — counterpoint: compressed codecs cap nearer 33.6.
  - Cost and latency matter → multiple POTS lines are pricey; latency can beat GEO satellite, but Starlink narrows the gap; telco incentives hampered rural broadband.

- LLM perspective
  - View: A clever systems-integration demo proving MLPPP’s scalability and Windows XP’s robust modem stack under real PSTN/PRI conditions.
  - Impact: Mostly educational; useful for labs, telephony retrofits, and understanding why digital voice paths make or break 56k.
  - Watch next: Push past 12 links, measure latency/jitter and loss, try Linux/FreeBSD MLPPP, and compare against Starlink or cellular bonding.
