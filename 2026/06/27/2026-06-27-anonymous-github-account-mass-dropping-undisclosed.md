# Anonymous GitHub account mass-dropping undisclosed 0-days

- Score: 618 | [HN](https://news.ycombinator.com/item?id=48698617) | Link: https://github.com/bikini/exploitarium

### TL;DR
An anonymous GitHub account is dumping a large set of supposed “0-day” exploits against popular tools (Ghidra, nmap, Docker, VLC, Gitea, etc.). HN commenters who reviewed the proofs-of-concept say many are configuration quirks, crashes, or already-known classes of bugs rather than practical, remotely exploitable vulnerabilities. A few (e.g., nmap, nghttp2) might be more serious but need careful exploitation. The thread broadens into frustration over buzzword inflation (“0-day”, “RCE”) and AI-driven vulnerability noise overwhelming open-source maintainers.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Many PoCs are weak → require unrealistic conditions, just crash apps, or show reachability into libraries; only a few parser bugs look plausibly high-impact.  
- “0-day” and “RCE” labels are overused → some entries resemble known/fixed CVEs or benign bugs; marketing language obscures actual exploitability.  
- AI tools inflate vuln volume → trivial issues get CWE IDs and dramatic wording; maintainers face more noise—counterpoint: some AI-generated sets (e.g., Mythos) were reportedly mostly real.  

---

### LLM perspective
- View: The combination of mass PoC dumps and AI scanners is turning vulnerability discovery into a high-volume, low-signal activity.  
- Impact: Open-source maintainers and security teams must invest more in triage, prioritizing clear exploit chains over theoretical bugs.  
- Watch next: Better exploitability scoring, deduplication against existing CVEs, and norms for labeling “research PoC” vs “real 0-day” are needed.
