# Janet Jackson had the power to crash laptop computers (2022)

- Score: 211 | [HN](https://news.ycombinator.com/item?id=46403291) | Link: https://devblogs.microsoft.com/oldnewthing/20220816-00/?p=106994

### TL;DR

During the Windows XP era, “Rhythm Nation” allegedly crashed certain laptops because audio from the song excited a natural resonance in their 5,400-rpm hard drives; even a nearby laptop could fail. A manufacturer mitigated the issue with an audio filter that removed the offending frequencies, risking a mysterious legacy workaround after those drives disappeared. HN readers connected the story to acoustic effects on datacenter disk I/O and questioned its evidence, damping, and exact frequency, while Raymond Chen said an investigating colleague personally vouched for it.

### Comment pulse

- Engineering explanation → resonance may disturb the head assembly rather than platters; cheap laptops often omitted vibration damping.
- Evidence concern → the story rests on a colleague’s account, and Chen regarded its CVE treatment as likely a joke.
- Myth correction → Tacoma Narrows failed from aerodynamic flutter, a distinction the article explicitly acknowledges.

### LLM perspective

- View: Physical coupling can turn ordinary media into a hardware fault without any software vulnerability.
- Impact: Storage designers need acoustic simulation and damping; maintainers need rationale attached to narrow compatibility filters.
- Watch next: Reproduction on identified drive models and frequency sweeps would separate mechanism from anecdote.
