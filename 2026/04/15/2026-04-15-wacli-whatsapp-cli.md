# Wacli – WhatsApp CLI

- Score: 227 | [HN](https://news.ycombinator.com/item?id=47775628) | Link: https://github.com/steipete/wacli

## TL;DR
wacli is a third‑party command‑line client for WhatsApp built on the WhatsApp Web protocol via whatsmeow. It lets you sync and locally store message history, continuously capture new messages, run fast offline full‑text search, send texts/files, and manage contacts and groups. Installation is via Homebrew or Go build, with a QR-based login and a persistent sync loop. HN discussion largely focuses on risk: because this is not an official API, accounts can be permanently banned, so it should be used cautiously and never for spam or aggressive automation.

---

## Comment pulse
- Third‑party clients risk suspension → WhatsApp bans for automation, high‑volume sending, or even mere use; appeals are unclear and often ineffective.  
- Telegram praised for automation → first‑class bot API, easy webhook integrations, great for alerts—counterpoint: WhatsApp dominates in many countries, so switching isn’t socially feasible.  
- WhatsApp underpins real markets → traders rely on unofficial tools for compliant bulk messaging; Meta seems uninterested despite WhatsApp’s potential as a Slack‑like business platform.

---

## LLM perspective
- View: Technically impressive local‑first CLI, but its unofficial status makes operational use risky for primary accounts.  
- Impact: Most useful for power users, ops teams, and hobby projects willing to sacrifice or isolate an account.  
- Watch next: Clearer rate‑limit guidance, safety tooling in wacli, and any movement from Meta on sanctioned automation channels.
