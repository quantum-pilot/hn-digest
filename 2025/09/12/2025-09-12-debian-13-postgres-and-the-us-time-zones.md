# Debian 13, Postgres, and the US time zones

- Score: 262 | [HN](https://news.ycombinator.com/item?id=45218111) | Link: https://rachelbythebay.com/w/2025/09/11/debtz/

- TL;DR
    - Upgrading to Debian 13 can break Postgres (and other apps) if configs use legacy US/* time zones (e.g., US/Pacific). IANA moved these aliases to tzdb’s “backward” set long ago; Debian 13 split them into the optional tzdata-legacy package, so they’re missing by default. The fix: switch to canonical names like America/Los_Angeles (or install tzdata-legacy). HN discusses poor upgrade comms, similar breakage in GitLab v18, and offers discovery tips (timedatectl list-timezones).

- Comment pulse
    - Root cause → IANA US/* aliases live in tzdb/backward; Debian 13 made them optional via tzdata-legacy, so aliases disappear — counterpoint: deprecated since 1993.
    - Communication gap → Release notes omit it; maintainers expect users to read package-level NEWS, causing surprises during upgrades.
    - Wider impact → GitLab v18 invalidated old time zone names, breaking scheduled jobs when stored values failed validation.

- LLM perspective
    - View: Sensible cleanup surfaced by packaging; ship migration aids: postinst checks, alias-to-canonical rewrites, apt-listchanges alerts.
    - Impact: Debian 13 ops, Postgres/NGINX admins, any app persisting/validating tz names; Americas most affected due to US/* prevalence.
    - Watch next: Debian add tzdata-legacy Recommends where needed; scanners to flag US/* in configs/DBs; clearer deprecation timelines from tzdb maintainers.
