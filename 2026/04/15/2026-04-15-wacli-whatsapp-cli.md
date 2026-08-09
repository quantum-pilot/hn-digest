# Wacli – WhatsApp CLI

- Score: 227 | [HN](https://news.ycombinator.com/item?id=47775628) | Link: https://github.com/steipete/wacli

### TL;DR

Wacli is a Go-based third-party WhatsApp command-line client built on whatsmeow and the unofficial WhatsApp Web protocol. After QR authentication, it locally captures message history, supports fast offline search, sends text and files, downloads media, and manages contacts, groups, and participants; human-readable and JSON output enable scripts. Older-history backfill is best-effort, per-chat, and needs the primary phone online. Commenters strongly warned that automation or even third-party login can trigger account suspension because Meta does not officially support this interface.

### Comment pulse

- Personal, human-rate automation may lower risk — counterpoint: bans can still be severe, permanent, and difficult to appeal.
- Telegram’s bot API is easier and officially automation-friendly, but WhatsApp’s national and business network effects make migration impractical.
- Commodity markets need consent-based bulk and compliance tooling that Meta reportedly considers too small to support.

### LLM perspective

- Use a disposable account, conservative rates, backups, and consent; never make critical records depend on unofficial access.
- Local indexing improves search privacy while creating a sensitive datastore requiring permissions, encryption, and retention controls.
- Watch Meta protocol changes, ban reports, official API expansion, and history-sync reliability.
