# "Fix" MacBook Neo Cursor Lag: Record 1 Pixel of the Screen Every 10 Seconds

- Score: 207 | [HN](https://news.ycombinator.com/item?id=48654465) | Link: https://gist.github.com/retroplasma/ec21767d0a8380c7ea9c2fbee1c7d6bf

### TL;DR

A MacBook Neo workaround eliminates cursor lag near screen edges and Terminal windows by continuously recording one screen pixel every 10 seconds to `/dev/null`. A generated menu-bar app requests screen-recording permission, uses little CPU/GPU, and can pause during fullscreen playback, though it leaves a privacy indicator. HN’s leading theory is that recording keeps WindowServer compositing the cursor, avoiding a stalled transition from hardware overlay to software rendering. Commenters called the hack effective but ugly, suggested enlarging the cursor, and worried about hidden power costs and forgotten startup fixes.

### Comment pulse

- Cursor-mode switching is the likely fault → experts suspect synchronization around GPU queues, fences, display planes, or WindowServer, but lack confirming code.
- Enlarging the cursor can force a similar rendering path → tiny changes fixed older fullscreen bugs, but Neo reportedly needs a noticeable increase.
- The workaround trades correctness for persistence → minimal overhead may justify it — counterpoint: startup hacks can waste power long after upstream fixes arrive.

### LLM perspective

- **View:** The workaround is diagnostic: unrelated UI changes both appear to pin cursor compositing into a stable mode.
- **Impact:** A tiny OS graphics bug creates enough daily friction that users accept screen-recording permissions and persistent indicators.
- **Watch next:** Measure battery draw and cursor transitions across Apple updates; disable the login item once lag no longer reproduces.
