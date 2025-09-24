# Find SF parking cops

- Score: 496 | [HN](https://news.ycombinator.com/item?id=45350690) | Link: https://walzr.com/sf-parking/

- TL;DR
    - A hobbyist built a tool to track San Francisco parking-enforcement officers, likely by scraping an SFMTA site. Within hours of launch, the city changed the endpoint, taking the tool offline. Commenters reverse-engineered citation numbers, concluding a (x+1) mod 7 check digit explains observed “+11/+4” increments, matching a contract’s error-control requirement. Others praised the retro UI and leaderboard, and debated SFMTA fine schedules—e.g., fire-lane/hydrant violations costing less than ADA infractions. Overall: clever civic hacking meets fast governmental lockdown.

- Comment pulse
    - Data access patched quickly → SFMTA changed the endpoint within hours; scraper broke; users asked for screenshots.
    - Ticket number pattern → fits (x+1) mod 7 check digit; contract mentions validation; initial example used an invalid number — counterpoint: earlier math mix-up.
    - Project vibe and policy → same author as bop-spotter; praised retro “Nokia” UI; fee table shows fire-lane/hydrant fines lower than ADA violations.

- LLM perspective
    - View: Civic scrapers are brittle; tiny site changes break them despite clever reverse-engineering of numbering and endpoints.
    - Impact: Rapid agency patching deters watchdog tools; pushes developers toward official APIs, MOUs, or downloadable static datasets.
    - Watch next: SFMTA to publish a stable enforcement-data API, document the check-digit spec, or pursue takedowns of mirrors.
