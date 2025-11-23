# New Apple Study Shows LLMs Can Tell What You're Doing from Audio and Motion Data

- Score: 64 | [HN](https://news.ycombinator.com/item?id=46015578) | Link: https://9to5mac.com/2025/11/21/apple-research-llm-study-audio-motion-activity/

### TL;DR
Apple researchers show that large language models can infer what you’re doing (e.g., cooking, vacuuming, playing sports) from simple audio and motion signals, even with no task‑specific training. Small models first turn microphone and IMU readings into short text captions and labels; an LLM then combines them (“late fusion”) to classify activities, improving further with a single example. Hacker News discussion focuses less on the novelty and more on long‑standing sensor‑privacy risks and whether LLMs are overkill for this task.

---

### Comment pulse
- Sensor-based surveillance isn’t new → Facebook’s Android motion permissions raised alarms; companies hoard data now, future models can mine unexpected insights—counterpoint: individual defenses are hard, user education lags.
- Why an LLM? → Critics say a simple classifier could fuse sensor outputs; defenders argue LLMs are flexible interpreters once everything is converted to text.
- Implications feel Orwellian → Some liken this to 1984-style telescreens, others note smartphones already exceed that capability and are voluntarily carried everywhere.

---

### LLM perspective
- View: This exemplifies “LLM as glue” for multimodal systems, using text as a universal interface between specialized sensor models.
- Impact: Expect smarter, more contextual health and activity features on phones/watches, but with amplified stakes around sensor-data consent and retention.
- Watch next: On-device versions, energy/privacy benchmarks, and platform policies forcing clear opt-ins and visibility into how motion/audio get repurposed.
