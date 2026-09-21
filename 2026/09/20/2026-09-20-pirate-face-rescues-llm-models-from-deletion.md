# Pirate Face Rescues LLM Models from Deletion

- Score: 524 | [HN](https://news.ycombinator.com/item?id=49776699) | Link: https://pirateface.co/

### TL;DR

Pirate Face proposes a BitTorrent preservation layer for eligible Hugging Face assets, producing checksum-verified torrents and magnets with Hugging Face as a web seed and peers as fallback. It currently limits listings to MIT- or Apache-licensed material, plus an approved Kimi exception. However, listing an asset neither downloads nor seeds it, and direct publishing, API compatibility, and seeding rewards remain planned features. HN readers liked the preservation model but stressed that torrents survive only while peers keep copies available.

### Comment pulse

- BitTorrent fits model preservation → distributed copies can outlive a host, but inactive swarms still disappear without committed seeders.
- The current implementation may overpromise resilience → commenters noted missing seeders, per-torrent work, and publishing features that are not yet available.

### LLM perspective

- View: Verified manifests solve provenance, while durable availability remains a social and operational problem.
- Impact: Model publishers gain another distribution path only after enough peers retain complete copies.
- Watch next: Confirm live torrent creation, peer counts, revision pinning, and the promised publishing API.
