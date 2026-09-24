# GPT-6 Astra has gained the ability to drive a car

- Score: 285 | [HN](https://news.ycombinator.com/item?id=49817404) | Link: https://drivingbench.com/

### TL;DR

DrivingBench connected general-purpose models to a Toyota Corolla’s steering, accelerator, and brakes on a fixed cone course. GPT-6 Astra completed the course after traveling 134.7 meters on its second attempt in 5:22, following 49% progress on its first; Fable 5.1 peaked at 45%, Grok 4.6 at 11%, and GPT-5.6 Sol at 6%. The cars moved extremely slowly for safety and latency. Researchers and HN commenters stressed this demonstrates closed-course control, not practical autonomous driving in traffic.

### Comment pulse

- Cloud latency prevents road deployment → real driving stacks need predictable, high-frequency local control for disturbances and rapidly changing hazards.
- Astra showed strong spatial adaptation → it used feedback across one continuous chat to improve from a partial run to completion.
- The benchmark probes general capability → a real car provides embodied feedback — counterpoint: the tiny, slow cone course has limited external validity.

### LLM perspective

- View: The result is an impressive systems experiment but far below safety-critical driving competence.
- Impact: Researchers gain a physical benchmark for perception, control, memory, and recovery under latency.
- Watch next: Measure intervention rates, control frequency, robustness, unseen courses, weather, moving obstacles, and local-model performance.
