# FocusTube: A Chrome extension that hides YouTube Shorts

- Score: 158 | [HN](https://news.ycombinator.com/item?id=45687227) | Link: https://github.com/CaptainYouz/FocusTube

- TL;DR
  - FocusTube is a minimal Chrome extension that hides YouTube’s Shorts block on the homepage and shrinks thumbnails to reduce visual bait. HN leans toward lighter, script-based alternatives like uBlock filters to hide Shorts sitewide, noting breakage when YouTube changes the UI. Mobile/TV are harder: Android can use ReVanced; Apple TV lacks options; turning off history removes all recommendations. Discussion splits between frustration at dark-pattern nudges that block a true “off” switch and acceptance that Shorts thrive under TikTok-driven incentives.

- Comment pulse
  - uBlock filters hide Shorts sitewide → less overhead; needs updates for new UI; some imports fail — counterpoint: browser/profile differences cause breakage.
  - Mobile/TV: Android ReVanced hides Shorts; Apple TV lacks options; disabling history kills recommendations; ScrollGuard helps curb doomscrolling.
  - Product incentives push dark patterns; no true opt-out; Premium still nudged—counterpoint: Shorts succeed and copycat features chase TikTok retention.

- LLM perspective
  - View: Prefer dynamic CSS/DOM filters over packaged extensions; fewer permissions, easier updates via community lists.
  - Impact: Users cut distraction minutes; platforms may obfuscate selectors and restructure DOMs to preserve engagement.
  - Watch next: Community-maintained filter list with CI tests for selector breakage; clearer mobile controls; regulatory pressure for explicit opt-outs.
