# I Don't Have Spotify

- Score: 234 | [HN](https://news.ycombinator.com/item?id=45084673) | Link: https://idonthavespotify.sjdonado.com/

### TL;DR

I Don’t Have Spotify converts a music-service link into candidate links on other supported platforms. Parsers normalize metadata and construct a query; platform-specific adapters search public endpoints or official APIs and prefer verified matches where available. It supports tracks, albums, artists, and podcasts—but not playlists—across Spotify, Tidal, YouTube Music, Apple Music, Deezer, SoundCloud, Qobuz, Bandcamp, and Pandora. The project warns that relevance matching can be wrong, and asks for improvements that remain fast without brute-force retries that could trigger rate limits.

### Comment pulse

- Readers found the name memorable but unclear, and several said the landing page needs a real example and sharper error messages.
- Comparisons with Odesli found broader results for some obscure albums, though several returned destination links were themselves empty.

### LLM perspective

- View: A modular translation layer solves a real social problem created by fragmented streaming subscriptions.
- Impact: Best-effort search is useful, but false matches and missing results can undermine trust quickly.
- Watch next: Better examples, match scoring, and transparent confidence indicators would make failures easier to understand.
