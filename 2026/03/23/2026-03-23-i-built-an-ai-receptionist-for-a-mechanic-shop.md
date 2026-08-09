# I built an AI receptionist for a mechanic shop

- Score: 200 | [HN](https://news.ycombinator.com/item?id=47487536) | Link: https://www.itsthatlady.dev/blog/building-an-ai-receptionist-for-my-brother/

### TL;DR

A developer built Axle, a voice receptionist for her brother’s mechanic shop, combining Vapi telephony, Voyage embeddings, MongoDB retrieval, Claude responses, and callback logging. The agent answers only from a 21-document knowledge base, escalates unknowns, and is intended to recover leads from 100-plus missed weekly calls; production deployment and booking remain unfinished. HN mechanics warn that repair quotes depend on diagnosis, parts availability, and changing prices, while others see promise for routine questions if uncertainty, handoff, and real-world outcomes are measured.

### Comment pulse

- Written intake with photos can reduce misunderstandings and lets staff review asynchronously before calling.
- A shared human receptionist or smarter voicemail may capture leads reliably — counterpoint: good agents eliminate holds for routine tasks.
- Live voice adds latency and transcription risks, especially for names and email addresses requiring exact capture.

### LLM perspective

- **View:** Limit initial scope to hours, status updates, intake, and callbacks; avoid diagnostic pricing.
- **Impact:** Shop staff gain triage data, but poor quotes could damage reputation and margins.
- **Watch next:** Call conversion, escalation rate, transcription accuracy, latency, customer disclosure, and quote disputes.
