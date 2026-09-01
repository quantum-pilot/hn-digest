# I turned my security cameras into an automatic bird identification system

- Score: 501 | [HN](https://news.ycombinator.com/item?id=49511856) | Link: https://jasontucker.blog/how-i-turned-my-security-cameras-into-an-automatic-bird-identification-system-with-birdnet-go/

### TL;DR

The author reused three RTSP security-camera microphones with self-hosted BirdNET-Go to identify birds continuously, send species alerts, track new visitors, publish optional BirdWeather observations, and integrate detections through MQTT and Home Assistant. Models run locally without subscriptions; a newer option recognizes 14,795 species. Over 12 months, the setup logged 418,726 detections across 271 species at 60.9% average confidence. Commenters shared doorbell, Raspberry Pi, dedicated microphone, and e-ink-display builds while warning about false positives, audio quality, and sensor-derived privacy.

### Comment pulse

- Existing RTSP cameras make wildlife monitoring inexpensive → one sensor can serve security and local acoustic classification.
- Dedicated 48 kHz microphones improve results → wind noise and low camera sampling rates can undermine detection.
- Always-on audio reveals unexpected information → charming bird data also demonstrates broader surveillance potential.

### LLM perspective

- View: The project succeeds by converting dormant sensor capability into an engaging, private household observatory.
- Impact: Families can learn local biodiversity, while deployments require careful microphone placement, consent, and confidence interpretation.
- Watch next: Measure false positives, speech suppression, seasonal accuracy, microphone quality, alert fatigue, and shared-data privacy.
