# Android now stops you sharing your location in photos

- Score: 298 | [HN](https://news.ycombinator.com/item?id=47750669) | Link: https://shkspr.mobi/blog/2026/04/android-now-stops-you-sharing-your-location-in-photos/

### TL;DR

OpenBenches maps memorial-bench photos using embedded GPS metadata, but its operator says Android now strips location from uploads through both photo and file pickers, PWAs, QuickShare, Bluetooth, and email; only USB transfer preserves it for desktop upload. The likely rationale is protecting users who unknowingly expose precise coordinates. Native apps can request ACCESS_MEDIA_LOCATION, pushing the volunteer project toward costly Android and iOS clients. Commenters strongly favored privacy-by-default yet criticized removing all informed opt-in paths, citing broken civic-reporting tools and proposing an explicit “include location” permission.

### Comment pulse

- Privacy advocates called silent GPS attachment a dangerous anti-feature because ordinary photo uploads can expose homes, routines, and other deanonymizing metadata.
- Developers supported stripping by default — counterpoint: a permission prompt could preserve niche workflows without granting every website coordinates.
- OpenBenches was not alone: a low-friction bicycle-infrastructure reporting service also lost automatic geolocation, substantially increasing volunteer-reporting friction.

### LLM perspective

- **View:** Privacy defaults work best when they remove surprise, not capability; explicit, scoped consent is the missing middle.
- **Impact:** Web projects lose platform parity with native apps, increasing cost and weakening open, account-free public-interest services.
- **Watch next:** Browser permission proposals, Chrome’s ACCESS_MEDIA_LOCATION handling, restoration of transfer metadata, user comprehension tests, and adoption by other platforms.
