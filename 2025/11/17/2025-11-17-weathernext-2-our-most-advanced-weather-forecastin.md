# WeatherNext 2: Our most advanced weather forecasting model

- Score: 191 | [HN](https://news.ycombinator.com/item?id=45954210) | Link: https://blog.google/technology/google-deepmind/weathernext-2/

### TL;DR

Google's WeatherNext 2 uses Functional Generative Networks to create hundreds of coherent forecast scenarios from one starting state by injecting noise within the model. Google says each forecast runs in under a minute on one TPU, reaches hourly resolution, is eight times faster, and beats WeatherNext Gen on 99.9% of evaluated variables and lead times through fifteen days. Data is available through Earth Engine and BigQuery, with Vertex AI early access, while forecasts are entering Search, Gemini, Pixel Weather, Maps Platform, and Maps.

### Comment pulse

- Practitioners highlighted CRPS training, which rewards accuracy while encouraging varied ensemble members under different noise draws.
- Commenters praised recent Google cyclone tracks but asked how models represent Earth's geometry and local terrain.

### LLM perspective

- View: Fast probabilistic ensembles matter more operationally than a single sharper deterministic forecast.
- Impact: Agencies and businesses can evaluate correlated regional risks without hours of supercomputer time.
- Watch next: Independent extreme-weather verification, calibration, geometric representation, local resolution, and public API limits.
