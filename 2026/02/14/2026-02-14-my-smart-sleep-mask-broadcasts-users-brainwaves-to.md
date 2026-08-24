# My smart sleep mask broadcasts users' brainwaves to an open MQTT broker

- Score: 308 | [HN](https://news.ycombinator.com/item?id=47015294) | Link: https://aimilios.bearblog.dev/reverse-engineering-sleep-mask/

### TL;DR

A researcher reverse-engineered an unnamed Kickstarter sleep mask after connection problems and found hardcoded credentials shared by every app installation. Those credentials opened the company’s MQTT broker, exposing live streams from roughly 25 masks and other sensors; the author captured EEG from two users and inferred possible REM and slow-wave sleep. Because the same broker carries commands, he says outsiders could also trigger vibration, heat, audio, or electrical muscle stimulation. The company was privately notified. Commenters condemned neural-data exposure, questioned wellness-device oversight, and blamed shortcut-heavy product development.

### Comment pulse

- Brainwave data need not reveal thoughts to be sensitive → sleep stage, alertness, occupancy, and health-adjacent signals can still expose users.
- Shared broker credentials collapse tenant isolation → one leaked app secret enables passive surveillance and potentially active stimulation across devices.
- Crowdfunded wellness hardware can outrun security review → counterpoint: commenters debated whether LLM-assisted engineering might improve or worsen rushed products.

### LLM perspective

- View: The gravest flaw is not cloud EEG storage alone, but shared authorization spanning telemetry and physical actuation.
- Impact: Users face privacy and bodily-interference risks; vendors handling neurotechnology need security controls closer to medical-device expectations.
- Watch next: Credential rotation, per-device authentication, broker access controls, on-device processing, incident notification, firmware updates, and independent remediation testing.
