# FreeBSD doesn't have Wi-Fi driver for my old MacBook. AI build one for me

- Score: 160 | [HN](https://news.ycombinator.com/item?id=47129361) | Link: https://vladimir.varank.in/notes/2026/02/freebsd-brcmfmac/

- TL;DR  
  A FreeBSD enthusiast used LLM coding agents (Claude/Pi/Codex/Gemini) to create a BCM4350 Wi‑Fi driver for a 2016 MacBook Pro by first asking AI to derive a detailed spec from Linux’s brcmfmac driver, cross‑checking that spec with multiple models, then having an agent implement and iteratively debug a fresh FreeBSD module. The result connects to WPA2 networks but is explicitly labeled experimental and unsafe. HN debates hype vs reality, license/clean‑room issues, and whether AI will soon auto-generate most drivers and bespoke software.

- Comment pulse  
  AI milestone but not magic → non‑expert orchestrated agents to get a working driver, yet it took months and remains fragile — counterpoint: still shows rapid capability trajectory.  
  Clean‑room worries → deriving a spec directly from GPL/open drivers then re‑implementing raises “license laundering” concerns; classic clean‑room keeps spec authors away from source.  
  Future of software → some predict ubiquitous AI‑generated drivers and custom apps; others note most users want off‑the‑shelf tools, like 3D printing hype fizzled.

- LLM perspective  
  View: Strong pattern: LLMs excel when turned into “junior engineers” managed via specs, milestones, and documentation loops.  
  Impact: Niche OSes, legacy hardware, and hobbyist projects gain cheap, semi‑working drivers and tools that were previously uneconomical.  
  Watch next: Better verification (fuzzing, formal checks) plus clearer IP guidelines will decide if these workflows move from toys to production.
