# NIST was 5 μs off UTC after last week's power cut

- Score: 152 | [HN](https://news.ycombinator.com/item?id=46355949) | Link: https://www.jeffgeerling.com/blog/2025/nist-was-5-μs-utc-after-last-weeks-power-cut

### TL;DR
NIST’s Boulder campus lost grid power for days after extreme winds, then a backup generator for its main ensemble clock failed. Staff rerouted emergency power and used batteries and alternate clocks on campus to keep the Internet time service running; the resulting deviation from UTC stayed under 5 microseconds. That’s negligible over the public internet (where millisecond jitter dominates) but matters for ultra-precise fiber and scientific users. The episode highlights how fragile time infrastructure is and the risks of GPS dependence.

---

### Comment pulse
- Time-over-fiber intrigue → HN dives into NIST’s fiber time-transfer, likely for labs, telescopes, GNSS backup, not mainly HFT—counterpoint: some assume commercial finance is a key user.  
- Scope of outage → Only Boulder NTP servers drifted; others were fine, and most systems should use pool.ntp.org, making real-world impact essentially zero.  
- “Bad time vs no time” → Serving unknown-bad time can corrupt many systems; with known outage, clients can fall back, alarm, or ignore that source.

---

### LLM perspective
- View: This was a successful live-fire test of time-distribution resilience, exposing edge cases without causing visible public failures.  
- Impact: High-precision labs, telecom, and GNSS integrity monitoring care most; ordinary NTP and consumer systems barely register microsecond errors.  
- Watch next: Deployment of multi-source PNT (GPS, BPS, fiber), smarter NTP client strategies, and public visibility into critical time-service incidents.
