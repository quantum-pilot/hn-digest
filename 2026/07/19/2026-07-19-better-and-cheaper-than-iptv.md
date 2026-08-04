# Better and Cheaper Than IPTV

- Score: 322 | [HN](https://news.ycombinator.com/item?id=48964015) | Link: https://github.com/stupside/castor

### TL;DR

Castor is a Go command-line tool that extracts playable video from a supplied web page or direct URL, transcodes it with ffmpeg, and streams it at full quality to DLNA televisions; Chromecast support is experimental. It discovers streams by observing headless Chrome network traffic, can search TMDB against user-configured sources, and optionally burns Whisper-generated subtitles. It bundles no catalog, bypasses no DRM, and warns users to cast only authorized material. Hacker News praised simpler public-HLS alternatives but debated anti-bot escalation, AI-assisted authorship, and whether Castor’s movie-oriented interface invites piracy.

### Comment pulse

- Direct HLS catalogs can be simpler → TV Explorer’s 10,000-plus public channels loaded nearly instantly — counterpoint: browser playback still showed controls and aspect-ratio bugs.
- Browser automation fuels an arms race → headless clients can spoof interaction and fingerprints, while detection increasingly burdens legitimate Linux, Tor, and JavaScript-averse users.
- Purpose and presentation conflict → authorization disclaimers separate tooling from sources — counterpoint: trending-movie discovery makes neutral casting look piracy-adjacent.

### LLM perspective

- **View:** Technical neutrality depends on defaults as much as disclaimers; product design shapes the use case users reasonably infer.
- **Impact:** Users with non-Chromecast televisions gain higher-quality casting, while site operators face more capable extraction clients and policy ambiguity.
- **Watch next:** Test site compatibility, subtitle latency, transcoding load, DLNA quirks, Chromecast support, lawful-source examples, and transparent automation behavior.
