# Major P2P issues in Israel and possibly other Middle East countries

- Score: 261 | [HN](https://news.ycombinator.com/item?id=48431461) | Link: https://github.com/ValveSoftware/GameNetworkingSockets/issues/398

- TL;DR  
  - Players in Israel, parts of the Middle East, and China report that since mid‑March many Steam games can’t form direct P2P links and are forced through Steam’s relay network, dramatically increasing latency. Multiple titles and ISPs are affected while non‑Steam matchmaking works fine, suggesting a regression in Steam Networking / WebRTC behavior rather than local connectivity. Community experiments with older steamwebrtc DLLs and a January Steam client restore low‑lag paths, and Valve has acknowledged the problem and is coordinating a fix.

- Comment pulse  
  - Geopolitics theory: Middle‑East/China filters disrupt STUN, forcing relays; — counterpoint: some users show STUN still functioning, pointing to a Steam‑client change.  
  - People love how an open GitHub issue enables global debugging, workarounds, and vendor contact; others lament GitHub’s drift toward low‑signal, Reddit‑style comment quality.  
  - Meta‑debate: HN title omits the “Israel/Middle East” clause; some suspect clickbait or politics avoidance, others point out Hacker News’ strict title length.

- LLM perspective  
  - View: This bug illustrates how centralized matchmaking/relay layers quietly become single points of failure for whole multiplayer ecosystems.  
  - Impact: Studios depending solely on Steam Networking risk sudden regressions in key regions; netcode teams may add alternative backends or fallbacks.  
  - Watch next: Useful follow‑ups: Valve changelog explaining STUN/IP‑sharing behavior, regional traceroutes to SDR POPs, and reproducible latency benchmarks before/after fixes.
