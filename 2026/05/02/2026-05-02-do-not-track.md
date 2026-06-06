# Do_not_track

- Score: 175 | [HN](https://news.ycombinator.com/item?id=47988592) | Link: https://donottrack.sh/

### TL;DR
The article proposes a single environment variable, `DO_NOT_TRACK=1`, as a universal opt‑out for CLI/SDK telemetry, crash reporting, ad tracking, and any non‑essential network calls. Instead of memorizing many project‑specific flags, users would set one variable that tools agree to honor, ideally alongside (or replacing) existing opt‑outs. Hacker News welcomes the simplicity but is skeptical: browser DNT was widely ignored, most software is already opt‑out by default, and network‑level blocking or aggregating existing env flags may be more realistic.

---

### Comment pulse
- Universal flag is conceptually neat → But normalizing opt‑out implies default consent to tracking, which many find inherently wrong and creepy.  
- DNT history suggests failure → Advertisers ignored browser DNT; devs expect similar noncompliance here—counterpoint: some CLI authors might voluntarily adopt it.  
- Practical users prefer control points → Suggestions include DNS blocklists, host‑level blocking, or tools that collect and set many telemetry env vars at once.

---

### LLM perspective
- View: This is a coordination problem; success depends on social norms among developers, not technical difficulty.  
- Impact: Most likely early adopters are privacy‑conscious OSS tools, creating pressure but not binding large vendors.  
- Watch next: Track real projects adding support, emergence of meta‑tools (env managers), and any standards‑body or distro endorsement.
