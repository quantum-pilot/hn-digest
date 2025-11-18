# WeatherNext 2: Our most advanced weather forecasting model

- Score: 191 | [HN](https://news.ycombinator.com/item?id=45954210) | Link: https://blog.google/technology/google-deepmind/weathernext-2/

TL;DR
Google DeepMind’s WeatherNext 2 is a probabilistic AI weather model that generates hundreds of ensemble forecasts on a single TPU in under a minute. Using a Functional Generative Network to inject structured noise, trained on marginals yet capturing joint structure, it achieves 1‑hour resolution and beats the prior WeatherNext on 99.9% of variables across 0–15 days. Data is in Earth Engine/BigQuery, with Vertex AI access, and it’s rolling into Search, Gemini, Pixel Weather, and Maps. HN discusses CRPS-based training for diverse outputs, real-world hurricane gains, and modeling geometry/verification.

Comment pulse
- Even imperfect forecasts aid decisions → planners need scenarios; ensembles reduce paralysis (Arrow anecdote). — counterpoint: ‘no-precip 90%’ baselines ignore high-impact extremes.
- CRPS-style objectives encourage diverse, calibrated outputs → inject noise and train probabilistically; helpful beyond weather for tasks needing multiple distinct solutions.
- Performance/practicality praised → recent hurricane tracks matched reality; US GFS seen regressing — counterpoint: demand for transparent benchmarks and grid geometry details.

LLM perspective
- View: FGN yields fast, physically consistent ensembles without costly NWP; still needs rigorous calibration and extreme-event validation.
- Impact: Operational tools shift AI-first for 0–15 days; HPC spend reallocates to TPUs; insurers, logistics, and utilities gain scenario-based planning.
- Watch next: Head-to-head against ECMWF/IFS and GraphCast; open CRPS/BS reliability curves; geodesic treatment for micro/mesoscale; agency acceptance for warnings.
