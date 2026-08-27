# Firefox 143 for Android to introduce DoH

- Score: 201 | [HN](https://news.ycombinator.com/item?id=45275444) | Link: https://blog.mozilla.org/en/firefox/dns-android/

### TL;DR

Firefox 143 exposes DNS-over-HTTPS on Android through an opt-in “Increased Protection” setting, with regional defaults possible after performance testing. Mozilla says encrypted DNS hides plaintext queries from local networks and that Canadian 75th-percentile lookups improved 61% year-to-date, reaching within one or two milliseconds of native DNS. HN welcomed mobile parity but debated browser-level DNS: it offers consistent controls and vetted resolvers across Android variants, while potentially bypassing local filtering and concentrating queries with large providers.

### Comment pulse

- Browser DoH adds portability and explicit resolver choice → Android support varies, and OS or VPN DNS paths may leak or be substituted.
- Local control can be preferable → Pi-hole, AdGuard, or personal recursive DNS over VPN preserves filtering and avoids centralized resolvers.

### LLM perspective

- View: The feature trades network-local control for browser-enforced privacy policy and consistent behavior.
- Impact: Android users gain encrypted queries, while administrators may need to reconcile Firefox with existing DNS filtering.
- Watch next: Default-rollout regions, independent latency measurements, resolver compliance, and behavior during DoH failure.
