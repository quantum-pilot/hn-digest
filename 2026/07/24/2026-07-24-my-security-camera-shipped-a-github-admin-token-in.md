# My security camera shipped a GitHub admin token in its login page

- Score: 489 | [HN](https://news.ycombinator.com/item?id=49034292) | Link: https://hhh.hn/hanwha-github-token/

- TL;DR  
  Researcher downloads Hanwha Vision camera firmware, uses binwalk, Ghidra, and an LLM to reverse‑engineer an obfuscated updater, recovering a hardcoded AES key/IV shared across models. Decrypting the root filesystem and scanning with trufflehog reveals a GitHub personal access token with admin rights to hundreds of org repos, accidentally bundled into the web UI via `process.env` leakage in a Vite build. Only 3 of ~500 firmwares contain this token. Hanwha revokes it within 12 hours, but the incident highlights chronic IoT supply‑chain security failures.

- Comment pulse  
  Open/replaceable camera firmware is feasible → Thingino, OpenIPC, Wyrecam and ONVIF+VLAN setups let users avoid trusting vendor stacks, with varying maturity.  
  DoD IPs in env vars are alarming → suggests defense ties or IP squatting; could also be coincidence given DoD’s huge address space—counterpoint: don’t assume malice without routing evidence.  
  IoT security remains abysmal → hardcoded secrets, reused keys, weak QA; users should isolate cameras on separate VLANs without internet to limit inevitable compromise impact.

- LLM perspective  
  View: LLM‑assisted reverse engineering turns opaque firmware into auditable code, lowering the bar for independent security research.  
  Impact: Vendors must assume their binaries will be inspected; obfuscation and shared keys are no longer credible protections.  
  Watch next: Automated firmware scanners integrating LLMs, trufflehog, and SBOMs as a CI “gate” to catch leaked secrets before shipping.
