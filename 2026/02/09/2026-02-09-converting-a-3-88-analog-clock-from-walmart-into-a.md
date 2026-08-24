# Converting a $3.88 analog clock from Walmart into a ESP8266-based Wi-Fi clock

- Score: 360 | [HN](https://news.ycombinator.com/item?id=46947096) | Link: https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock

### TL;DR

A D1 Mini ESP8266 drives a modified quartz clock movement with bipolar pulses and synchronizes against NTP every 15 minutes, including daylight-saving adjustments. Software compares displayed and network time ten times per second, advances lagging hands, and waits when they are ahead because the mechanism cannot reverse. Since the clock provides no positional feedback, a 47L04 EERAM records hand positions each second and restores them after power loss; initial alignment uses a web page. Commenters highlighted the low-wear backup design, fragile motor wiring, variable price, radio-clock alternatives, and drive-circuit protection.

### Comment pulse

- EERAM matches frequent state tracking → SRAM handles continual writes, then capacitor-backed power-fail logic copies state once into EEPROM.
- Cheap movements require delicate intervention → hair-thin coil leads must be disconnected from their oscillator and driven reliably with tuned pulses.
- Network time is not the only path → commenters proposed WWVB emulation — counterpoint: transmitting on its frequency may be illegal.

### LLM perspective

- View: The cleverness lies less in NTP than reconstructing state for an open-loop mechanical display across power failures.
- Impact: Hobbyists gain an accurate analog interface, accepting permanent Wi-Fi dependence, hardware modification, calibration, and motor-driver electrical risks.
- Watch next: Clock-model compatibility, safe H-bridge designs, missed-step detection, offline behavior, security maintenance, EERAM endurance, and variants for projection clocks.
