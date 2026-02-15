# My smart sleep mask broadcasts users' brainwaves to an open MQTT broker

- Score: 308 | [HN](https://news.ycombinator.com/item?id=47015294) | Link: https://aimilios.bearblog.dev/reverse-engineering-sleep-mask/

- TL;DR  
This post describes using Claude to reverse‑engineer a Kickstarter EEG sleep mask: mapping its BLE protocol, extracting hardcoded MQTT credentials from the Flutter app, and discovering that every device worldwide streams raw brainwaves and accepts stimulation commands via an unauthenticated public broker. The author responsibly discloses the issue. HN commenters debate Kickstarter’s “ship fast” ethos, the precedent of insecure brain/health data, weak IoT security, and the need for regulation and on‑device, encrypted processing in neurotech.

- Comment pulse  
  - Kickstarter encourages hardware teams to underinvest in engineering, now amplified by LLMs making software seem “free” — counterpoint: some trust LLM output over bargain engineers.  
  - Insecure EEG streaming sets a worrying precedent for brain and sleep data, enabling stalking or burglary; limited research upside doesn’t justify lax privacy or consent.  
  - Neurotech founders and IoT veterans call for mandatory data‑security baselines, on‑device processing, encryption, and skepticism toward any cloud MQTT handling health‑adjacent stimulation devices.

- LLM perspective  
  - View: LLMs now make deep reverse‑engineering of opaque consumer devices accessible, exposing security failures that previously stayed obscure to non‑specialists.  
  - Impact: Expect more revelations about insecure IoT backends, pressuring small vendors to adopt proper auth, isolation, and region‑scoped infrastructure.  
  - Watch next: tools that scan firmware and brokers for shared credentials and unsafe commands, then assist disclosure and vendor remediation.
