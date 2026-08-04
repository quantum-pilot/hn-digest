# Windows 11 New Media Player Uses 3.5x More RAM, Charges for Popular Video Codecs

- Score: 246 | [HN](https://news.ycombinator.com/item?id=48609343) | Link: https://www.extremetech.com/computing/windows-11s-new-media-player-uses-35x-more-ram-charges-for-popular-video

### TL;DR

Tests cited by ExtremeTech put Windows 11’s Media Player at roughly 377MB idle RAM versus 103MB for the classic player, with local-video startup rising from two to three seconds. Windows 11 24H2 also drops bundled AC-3 decoding, while HEVC playback uses a paid Store extension; the legacy player remains optional and VLC supplies its own codecs. HN readers criticized the user-facing regression but corrected claims that web technology caused it: the app is C# with UWP/WinUI XAML, largely inherited from 2014–2017 Groove Music and rebranded in 2022.

### Comment pulse

- Codec pricing may reflect rising patent-pool costs → licensing pressure offers context — counterpoint: commenters rejected degrading Windows while Microsoft funds costly acquisitions.
- The HEVC paywall is inconsistent → a long-standing Store product link reportedly installs Microsoft’s extension free, despite the paid listing.
- Standalone codec packs have faded → VLC, MPC-HC/BE, SMPlayer, and mpv generally handle today’s common formats without separate installation.

### LLM perspective

- **View:** A modest absolute RAM increase becomes consequential when bundled software simultaneously slows down and loses default format support.
- **Impact:** Users on 8GB PCs bear the bloat; third-party players gain relevance through predictable codecs and mature performance.
- **Watch next:** Benchmark working-set composition, playback CPU and power, codec coverage, and cold-start latency across Media Player, VLC, and MPC.
