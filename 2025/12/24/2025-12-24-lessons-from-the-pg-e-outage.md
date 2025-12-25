# Lessons from the PG&E outage

- Score: 131 | [HN](https://news.ycombinator.com/item?id=46371730) | Link: https://waymo.com/blog/2025/12/autonomously-navigating-the-real-world

### TL;DR
Waymo describes how a major PG&E power outage in San Francisco darkened thousands of traffic lights, causing gridlock and stressing its robotaxi fleet. Cars are programmed to treat dark signals as four‑way stops but often request remote “confirmation,” which created a huge spike in human-assistance calls, delays, and some blocked intersections. Waymo temporarily paused service and promises software updates to better detect widespread outages, refined emergency protocols, and expanded first-responder training. HN debates technical readiness, central learning benefits, and public-road obligations.

---

### Comment pulse
- Open question: Can Waymo reliably obey human traffic directors (police, construction workers, ferry staff)? Gesture interpretation is known-hard; commenters note no strong public evidence either way.  
- Centralized learning praised: one fix updates 1,000 cars at once → safer over time—counterpoint: humans handled the outage; AVs needing bespoke updates may stay brittle.  
- Disaster-mode design: some say city-scale outages should’ve been core to plans; others note combinatorial emergencies, limited remote support, and evidence of real autonomy at scale.

---

### LLM perspective
- View: Core issue isn’t dark lights, it’s dependence on scarce remote confirmation; that’s a systemic scaling bottleneck and failure mode.  
- Impact: AV operators must harden “rare event” handling, emergency integration, and policies for when their fleets must rapidly and safely self-park.  
- Watch next: Regulators may demand metrics on remote-ops load, intersection blocking, emergency drills, and independent audits of unusual-situation behavior.
