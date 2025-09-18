# YouTube addresses lower view counts which seem to be caused by ad blockers

- Score: 329 | [HN](https://news.ycombinator.com/item?id=45276262) | Link: https://9to5google.com/2025/09/16/youtube-lower-view-counts-ad-blockers/

- TL;DR
  - Creators saw sharp view drops since mid‑August, mostly on desktop. Evidence points to ad blockers: EasyList recently started blocking YouTube’s “start-of-playback” view ping, so many desktop plays aren’t counted. YouTube says ad blockers can skew reported views and denies a systemic bug or AI age checks as the cause. Ad revenue appears stable, implying only metrics are suppressed. HN worries: sponsorship deals and recommendations depend on view counts, and tech-heavy channels may be hit harder; others blame Google’s poor, scammy ads for driving adblock adoption.

- Comment pulse
  - Root cause → EasyList added YouTube’s view-attribution endpoint to a privacy list, blocking desktop pings; YouTube didn’t change code — counterpoint: orchestrated pressure on creators.
  - Business impact → Public views drive sponsorship rates and algorithmic discovery; tech-focused, desktop-heavy audiences lose leverage despite stable ad revenue.
  - Ad quality backlash → Frequent scams, deepfakes, NSFW ads justify adblocking for many; paying Premium feels unfair if platforms can’t vet ads.

- LLM perspective
  - View → This is a measurement-layer breakage; expect divergent public vs. revenue metrics until filter maintainers adjust.
  - Impact → Recommendation systems relying on views may misrank desktop-heavy niches, subtly reshaping which creators grow.
  - Watch next → EasyList rule updates, YouTube clarifying counted signals, creators publishing A/B tests across devices and blocker configurations.
