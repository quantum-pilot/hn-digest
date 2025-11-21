# Firefox 147 Will Support the XDG Base Directory Specification

- Score: 306 | [HN](https://news.ycombinator.com/item?id=45992829) | Link: https://www.phoronix.com/news/Firefox-147-XDG-Base-Directory

### TL;DR
Firefox 147 will finally honor the XDG Base Directory spec on Linux, addressing a 21‑year‑old bug. New installs without `~/.mozilla` will store profiles under `$XDG_CONFIG_HOME/mozilla` and use the existing XDG cache directory, reducing dotfile clutter. However, there’s no automatic migration from `~/.mozilla`, and Firefox still doesn’t cleanly separate configuration, cache, and data into `$XDG_CONFIG_HOME`, `$XDG_CACHE_HOME`, and `$XDG_DATA_HOME`. HN discussion welcomes the move but criticizes the partial compliance and migration story.

---

### Comment pulse
- Partial XDG compliance → Firefox now uses XDG config/cache and keeps `~/.mozilla` if present, avoiding data loss but skipping migration and real config/data/cache split.  
- Signal effect → A major app adopting XDG may push others toward cleaner homedirs; OpenSSH remains cautious, citing security and complexity of multiple config paths.  
- Practical benefits → Cleaner homes, easier renames and migrations; past Thunderbird/Icedove breakage shows why separating config from data matters — counterpoint: legacy apps must prioritize not breaking setups.

---

### LLM perspective
- View: This is a pragmatic compromise: new users get XDG, existing users stay stable, at the cost of incomplete spec adherence.  
- Impact: Linux desktop users, distro packagers, and backup tools benefit from more predictable paths and fewer ad‑hoc dotdirectories.  
- Watch next: Whether Firefox later splits data vs config, adds migration tools, and whether other big apps follow with full XDG adoption.
