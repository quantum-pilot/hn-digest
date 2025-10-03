# Playball – Watch MLB games from a terminal

- Score: 280 | [HN](https://news.ycombinator.com/item?id=45451577) | Link: https://github.com/paaatrick/playball

- TL;DR
    - Playball is a Node.js terminal app that shows MLB schedules, standings, and live play-by-play as text. Run via npx/npm or Docker; navigate with keys; customize colors and favorite teams. It pulls data from MLB’s StatsAPI—no video stream—so it’s discreet and low-bandwidth. HN notes the human-in-the-loop pipelines behind live stats and how baseball’s scorekeeping “DSL” fits text UIs. Discussion splits on MLB streaming: internationally robust, but US blackouts, DTC costs, and gambling promos irk fans.

- Comment pulse
    - Live data comes from humans + models → people tag every play; automation helps, but “eye test” inputs still drive advanced stats.
    - Streaming mixed bag → abroad, every game works; in US, blackouts, expensive DTC, gambling promos frustrate — counterpoint: MLB.tv/Statcast show strong tech investment.
    - Baseball suits text UIs → standardized scorekeeping acts like a DSL; fans mentally reconstruct plays from terse strings.

- LLM perspective
    - View: Text-first TUI avoids rights issues, leverages public StatsAPI; great for low-bandwidth, distraction-free following.
    - Impact: Helps engineers, terminal users, and radio-first fans track games at work or on servers without GUIs.
    - Watch next: Monitor MLB StatsAPI changes, rate limits, and ToS; add alerts, box-score diffs, and per-team notifications; benchmark update latency vs. Gameday.
