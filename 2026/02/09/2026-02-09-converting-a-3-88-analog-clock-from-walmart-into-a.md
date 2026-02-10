# Converting a $3.88 analog clock from Walmart into a ESP8266-based Wi-Fi clock

- Score: 360 | [HN](https://news.ycombinator.com/item?id=46947096) | Link: https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock

### TL;DR
A hobbyist converts a $3.88 Walmart quartz wall clock into a Wi‑Fi‑synced analog clock using a Wemos D1 Mini (ESP8266). The ESP8266 disconnects the stock oscillator, directly drives the Lavet stepping motor with bipolar pulses, and syncs via NTP every 15 minutes, including DST handling. Because the hands provide no feedback, an EERAM (SRAM+EEPROM) chip persistently tracks hand positions across power loss, configured via a tiny web UI. HN discussion focuses on this memory trick, related atomic/WWVB hacks, and whether hacking beats just buying a “smart” clock.

---

### Comment pulse
- DIY vs buying → Variable Walmart pricing and expensive projector/Wi‑Fi clocks spark debate on whether hacking is worth it versus off‑the‑shelf—even as Temu clocks drift annoyingly.  
- Smart persistence → The 47L04 EERAM gives wear‑free frequent writes for hand position; commenters note similar FRAM parts good for logs and device state.  
- Time signals → Related ESP32/RPi projects emulate WWVB‑style atomic clock broadcasts for hard‑to‑reach clocks; others warn transmitting on those LF bands is likely illegal.

---

### LLM perspective
- View: Clever pattern: hijack cheap consumer hardware, replace its brain, keep the analog form factor but gain NTP‑grade accuracy.  
- Impact: Useful reference for embedded developers needing frequent state persistence without flash wear, and for robust timekeeping in low‑feedback mechanisms.  
- Watch next: Higher‑capacity EERAM/FRAM use, standardized drivers for Lavet motors, and ultra‑low‑power Wi‑Fi/MCU combos for always‑on smart clocks.
