# YouTube, your RSS feeds are broken

- Score: 319 | [HN](https://news.ycombinator.com/item?id=48030964) | Link: https://openrss.org/blog/youtube-your-feeds-are-broken

## TL;DR
YouTube still exposes RSS feeds for channels, but the article argues they’re now unreliable, hidden, and polluted with Shorts, reflecting a broader trend of big platforms undermining open, user-controlled feeds in favor of algorithmic engagement and ad revenue. The author (from Open RSS) frames this as part of a long fight to keep RSS alive and offers Open RSS as a workaround. HN commenters trade technical tricks, point out quirks in YouTube’s implementation, and note Open RSS’ own rough edges.

---

## Comment pulse
- Workarounds exist: using `playlist_id=UULF…` in the feed URL mostly filters regular videos; some readers like Serial auto-separate Shorts — counterpoint: Shorts still leak through.
- Users worry publicity will prompt Google to kill RSS outright; others speculate on monetized, delayed feeds with revenue shares rather than removal.
- Technical nitpicks: the `<link>` tag for feeds only appears after a hard refresh, and Open RSS itself shows caching / network-block issues for some ISPs.

---

## LLM perspective
- View: This is a governance problem: feed reliability is deprioritized because it weakens engagement control and ad targeting.
- Impact: Power users, researchers, and creators relying on predictable syndication are pushed toward brittle hacks and third-party intermediaries.
- Watch next: Standardized tests for feed correctness, browser-level UI for autodiscovered feeds, and whether YouTube tightens or loosens RSS access.
