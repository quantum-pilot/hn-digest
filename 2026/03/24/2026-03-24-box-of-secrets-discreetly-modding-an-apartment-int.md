# Box of Secrets: Discreetly modding an apartment intercom to work with Apple Home

- Score: 254 | [HN](https://news.ycombinator.com/item?id=47488686) | Link: https://www.jackhogan.me/blog/box-of-secrets/

### TL;DR
The author helps a friend whose apartment intercom stopped working because management let its cellular plan lapse. After failing to hack the Doorking router or fake phone signaling, they instead tap the solenoid line that physically unlocks the gate. An ESP32 relay board, powered from the intercom’s AC feed via a regulator, runs Rust firmware implementing Matter, exposing the gate as an Apple Home lock. The relay defaults to pass‑through, so the original system still works. HN debates the legality, ethics, and alternatives.

---

### Comment pulse
- Modding a shared building access system is ethically and legally risky → bypasses logs, broadens access, raises liability for crimes or failures — counterpoint: many say risk is negligible in practice.  
- Others automate intercoms via telephony → voicemail or Asterisk/VoIP play DTMF tones or prompt for passcodes, enabling logging and fine‑grained guest codes.  
- Several note off‑the‑shelf options and hacks → local boards, Nuki Opener, Doorman, or smart speakers/Home Assistant, while lamenting how poor and fragmented intercom products still are.

---

### LLM perspective
- View: Technically elegant: intercept the simplest actuator (solenoid) instead of wrestling proprietary protocols or brittle router exploits.  
- Impact: Encourages more DIY integrations of legacy building hardware with Matter/HomeKit; raises awareness of shared‑infrastructure consent and security tradeoffs.  
- Watch next: Commodity “bolt‑on” ESP32/Matter boards for intercoms and gates, with clearer legal guidance and safer, auditable access‑sharing features.
