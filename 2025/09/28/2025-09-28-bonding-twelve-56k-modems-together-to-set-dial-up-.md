# Bonding twelve 56K modems together to set dial-up broadband records

- Score: 112 | [HN](https://news.ycombinator.com/item?id=45400828) | Link: https://www.tomshardware.com/networking/enthusiasts-bond-twelve-56k-dial-up-modems-together-to-set-dial-up-broadband-records-a-dozen-screeching-boxes-achieve-record-668-kbps-download-speeds

### TL;DR

The Serial Port combined twelve 56K modems into one logical connection using Multilink PPP, reaching 668.8 kbps and streaming low-resolution YouTube without buffering after an initial delay. The setup used a Windows XP computer, multiport serial cards, a Cisco gateway, and an ISP-side digital modem system; the article calls it a probable record because the group found no reports beyond four bonded modems. Commenters supplied historical context on PPP bonding, persistent dial-up latency, and the specialized digital path required for 56K.

### Comment pulse

- Former operators recalled bonding modem, ADSL, ISDN, and T1 links when added bandwidth justified costly lines and equipment.
- Readers clarified that the gateway connected analog lines into digital telephony infrastructure rather than ordinary compressed VoIP.

### LLM perspective

- View: The experiment is compelling archaeology: obsolete constraints become an engineering puzzle rather than a product proposal.
- Impact: Bonding scales throughput, but cannot erase latency, line expense, or fragile period-specific dependencies.
- Watch next: Whether additional modems expose a practical Multilink PPP limit or serial and host bottlenecks first.
