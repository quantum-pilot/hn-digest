# The 'Toy Story' You Remember

- Score: 1087 | [HN](https://news.ycombinator.com/item?id=45883788) | Link: https://animationobsessive.substack.com/p/the-toy-story-you-remember

- TL;DR
  - Toy Story and many 90s Disney features were rendered digitally but finished on 35mm, with colors deliberately biased to counter film’s response. Early home videos came from film prints; later digital-to-digital transfers (pioneered on A Bug’s Life) removed grain and altered saturation/contrast, subtly changing the films’ feel. Preservationists debate the “correct” look; studios haven’t settled on theatrical-intent grades. HN likens this to audio mastering and retro games, and urges documenting compensations and separating process artifacts from creative intent.

- Comment pulse
  - Compensation vs intent must be explicit → document in pipeline (RFDs, ARCHITECTURE.md), keep transforms separate, ensure reproducible renders; otherwise scaffolding becomes product.
  - 35mm scans aren’t ground truth → projection, lab, scanning and grading vary — counterpoint: mismatches exist (e.g., Aladdin sky), meaning some digital grades miss intent.
  - Analogues: retro games on CRTs, AM-radio mastering, vinyl vs CD → hardware shaped art; memories and preferences differ, making a single “correct” look elusive.

- LLM perspective
  - View: Ship two grades: film-intent simulation and digital-native; embed color transforms (ACES ODT/IDT) and rationale as metadata, not tribal knowledge.
  - Impact: Studios/streamers add ‘theatrical’ modes; archives budget for 35mm-scanned references; artists regain control over home/streaming presentation.
  - Watch next: Official reference LUTs for 90s catalogs, ACES updates for film-out emulation, and Disney+/Blu-ray releases labeled by intended viewing path.
