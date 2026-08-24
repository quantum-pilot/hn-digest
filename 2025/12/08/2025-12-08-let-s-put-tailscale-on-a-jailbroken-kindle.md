# Let's put Tailscale on a jailbroken Kindle

- Score: 207 | [HN](https://news.ycombinator.com/item?id=46194337) | Link: https://tailscale.com/blog/tailscale-jailbroken-kindle

### TL;DR

A jailbroken, firmware-compatible Kindle can run Tailscale alongside KOReader, turning the e-reader into a remotely reachable tailnet device. The setup requires blocking updates, installing the jailbreak, KUAL, USB networking, ARM—not ARM64—binaries, and a reusable authentication key whose expiry is disabled. It enables SSH, Taildrop transfers, Calibre-Web access, and home-service experiments without sacrificing normal reading features. Commenters liked the ownership hack but stressed update fragility and noted Kobo offers a friendlier modding path.

### Comment pulse

- Modding restores device ownership → users valued SSH and odd tailnet experiments on otherwise closed hardware.
- Kindle maintenance remains brittle → current firmware can undo access, while Kobo is considered easier to extend.

### LLM perspective

- View: The hack’s real value is local control, with remote convenience as the reward.
- Impact: Technical readers gain an inexpensive endpoint, but ordinary owners inherit firmware vigilance and key-management risk.
- Watch next: Updated jailbreak coverage, durable startup automation, and safer authentication than a non-expiring reusable key.
