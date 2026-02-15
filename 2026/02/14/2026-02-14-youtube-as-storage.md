# YouTube as Storage

- Score: 152 | [HN](https://news.ycombinator.com/item?id=47012964) | Link: https://github.com/PulseBeat02/yt-media-storage

- TL;DR  
    - Open-source tool encodes arbitrary files into lossless FFV1/MKV video, optionally encrypts them, and later decodes them, enabling “YouTube as storage” via CLI or GUI. It uses fountain codes for redundancy so data can theoretically survive transcoding. HN likes the technical ingenuity but notes this clearly violates YouTube’s ToS, is extremely storage-inefficient, and risks account bans. Discussion widens into YouTube’s long‑tail economics, AI training value of archived videos, and the inevitability of deleting low-value content.

- Comment pulse  
    - YouTube's long tail became an AI goldmine → archiving everything pays off for training—counterpoint: videos still vanish and storage limits will eventually bite.  
    - Project is clever but violates YouTube ToS → service is for video sharing, not generic storage; heavy use risks account bans or data deletion.  
    - Encoding files into video is possible but inefficient → YouTube recompression and transcoding threaten bit-perfect recovery, demanding extreme redundancy and many accounts to resist removals.

- LLM perspective  
    - View: Treat this as an educational steganography/erasure-coding demo, not a serious backup strategy or production storage layer.  
    - Impact: Highlights how opaque platform policies make “free” infrastructure unreliable; self-hosted or paid storage remains safer for critical data.  
    - Watch next: Benchmarks on decode success after real YouTube transcoding, and experiments with other services or codecs preserving more payload.
