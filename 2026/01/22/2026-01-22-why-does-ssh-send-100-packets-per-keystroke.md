# Why does SSH send 100 packets per keystroke?

- Score: 226 | [HN](https://news.ycombinator.com/item?id=46723990) | Link: https://eieio.games/blog/ssh-sends-100-packets-per-keystroke/

### TL;DR
The author was profiling a high-performance terminal game running over SSH and noticed ~100 packets per keystroke, even when no game data was sent. Packet captures plus `ssh -vvv` logs revealed OpenSSH’s 2023 “keystroke timing obfuscation”: it sends periodic SSH2_MSG_PING “chaff” packets (~20 ms apart) to hide real typing patterns. This is great for privacy but disastrous for a latency‑sensitive, bandwidth‑heavy game. Disabling the feature (client flag and then a forked Go SSH lib that omits the ping extension) cut CPU and bandwidth roughly in half. HN discussion centers on whether this should be configurable, the security vs performance tradeoff, alternatives like telnet/netcat, and how much LLMs actually helped the debugging process.

---

### Comment pulse
- Make chaff configurable in Go’s SSH lib → useful for machine‑to‑machine traffic—counterpoint: extra knobs risk “set and forget” weakened security in real terminals.  
- For non‑secure terminal games, just avoid SSH → use telnet, netcat, or SSH with a “none” cipher to see raw traffic.  
- Some see Claude as mostly a rubber duck → others note AIs’ sycophantic tone but still value their momentum and tooling suggestions.  

---

### LLM perspective
- View: This shows how invisible “secure by default” features can quietly dominate performance in unconventional uses of mature protocols.  
- Impact: Terminal app/game authors and infra engineers need to profile with current SSH defaults, not legacy mental models of behavior.  
- Watch next: Whether SSH/Go libraries grow explicit toggles, and emergence of AI tools specialized for safe, interactive protocol/pcap analysis.
