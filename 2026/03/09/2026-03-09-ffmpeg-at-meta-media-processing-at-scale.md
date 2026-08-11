# FFmpeg at Meta: Media Processing at Scale

- Score: 219 | [HN](https://news.ycombinator.com/item?id=47305236) | Link: https://engineering.fb.com/2026/03/02/video-engineering/ffmpeg-at-meta-media-processing-at-scale/

### TL;DR

Meta runs FFmpeg and ffprobe tens of billions of times daily across more than one billion video uploads, making duplicated decoding and process startup expensive. It has now retired its divergent internal FFmpeg fork for video-on-demand and livestreaming after collaborating with FFmpeg, FFlabs, and VideoLAN to upstream parallel multi-output encoding and in-loop decoding for real-time quality metrics. FFmpeg 6 through 8 gained the relevant work; Meta keeps only hardware-specific MSVP patches private. HN welcomed community-wide efficiency gains but questioned why upstreaming came so late and criticized the post’s self-congratulatory framing.

### Comment pulse

- Upstreaming eliminated duplicate forks and benefits every FFmpeg user — counterpoint: Meta could have integrated earlier instead of carrying private divergence.
- Single-decode, multi-output encoding cuts overhead; commenters wanted time-axis parallelization for one-output jobs, though interframe dependencies complicate splitting.
- Bellard and volunteer maintainers created immense commercial value; readers hoped the ecosystem compensates them proportionally.

### LLM perspective

- **View:** At billion-upload scale, upstream maintainability becomes an efficiency feature, not merely community relations.
- **Impact:** Meta reduces rebase risk; other media pipelines gain parallelism and live quality measurement without a private fork.
- **Watch next:** Regression data, performance benchmarks, maintainer funding, and future codec or metric contributions.
