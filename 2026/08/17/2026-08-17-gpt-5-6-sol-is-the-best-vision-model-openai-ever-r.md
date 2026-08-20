# GPT 5.6 Sol is the best "vision" model OpenAI ever released

- Score: 363 | [HN](https://news.ycombinator.com/item?id=49329575) | Link: https://blog.roboflow.com/openai-gpt-5-6/

### TL;DR

Roboflow’s forthcoming benchmark finds GPT-5.6 Sol is OpenAI’s strongest vision model yet, especially for detection: mAP@50 rose from GPT-5.5’s 13.8 to 46.2, and counting reached 73.0%. OCR remained similar at 90.7%, while targeted extraction fell to 82.5% versus 87.6%. Large images around 2,000 pixels destabilized boxes unless resized or given more reasoning. Sol averaged about 10 seconds and 2.5 cents per image. Commenters stressed that Gemini 3.5 Flash still led nearly every tested task at lower cost and traditional detectors suit scaled production.

### Comment pulse

- Sol’s visual cohesion impressed UI users → counterpoint: subjective design judgment is a weak benchmark and Gemini remained stronger overall.
- General VLMs reduce custom development → specialized detectors or OpenCV remain faster and cheaper for narrow, repeated tasks.
- Apparent rotated boxes suggested EXIF trouble → author says investigation with OpenAI instead traced instability to large image resolution.

### LLM perspective

- View: Sol closes OpenAI’s detection gap, but “best OpenAI vision model” should not be mistaken for best practical vision system.
- Impact: Agents gain better screen and document grounding; high-volume robotics and annotation pipelines still need model routing or specialization.
- Watch next: Release the full benchmark, retest current Gemini versions, and publish accuracy after standardized resizing and coordinate formats.
