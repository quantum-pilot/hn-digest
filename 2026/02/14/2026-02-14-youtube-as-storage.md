# YouTube as Storage

- Score: 152 | [HN](https://news.ycombinator.com/item?id=47012964) | Link: https://github.com/PulseBeat02/yt-media-storage

### TL;DR

This C++ tool turns arbitrary files into 4K, 30-fps FFV1/MKV video frames, then reconstructs them later. Wirehair fountain codes add redundancy and repair, while optional XChaCha20-Poly1305 encryption protects contents; CLI and Qt interfaces support single-file and batch workflows. The intended destination is YouTube, effectively shifting storage costs to its video infrastructure. Commenters questioned whether transcoding preserves enough signal, noted that videos can disappear, and cited terms explicitly forbidding general-purpose file storage. Even if technically recoverable, uploads risk inefficiency, deletion, or account bans.

### Comment pulse

- Historical storage abundance encouraged the experiment—counterpoint: growth, AI uploads, and stalled cost declines may eventually force deletion policies.
- Some called corporate capacity fair game; others saw deliberate cost-shifting as abuse of shared infrastructure explicitly outside the service’s purpose.
- Fountain-code redundancy may survive compression, but transcodes, removed videos, or banned accounts can still exceed the recovery budget.

### LLM perspective

- View: This is an error-correction demonstration masquerading as storage; durability depends on a hostile, undocumented transformation and retention layer.
- Impact: Experimenters gain a clever codec exercise while externalizing compute, capacity, policy, and account risk to YouTube.
- Watch next: Measure recovery after every transcode tier, bandwidth expansion, redundancy overhead, deletion tolerance, and platform encoder changes.
