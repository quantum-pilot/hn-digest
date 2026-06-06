# Pwnd Blaster: Hacking your PC using your speaker without ever touching it

- Score: 633 | [HN](https://news.ycombinator.com/item?id=48382310) | Link: https://blog.nns.ee/2026/06/03/katana-badusb/

### TL;DR
A researcher reverse‑engineered the Creative Sound Blaster Katana V2X soundbar and found its custom control protocol (CTP) is fully exposed over Bluetooth Low Energy—no pairing, no auth. Because firmware updates use CTP and only check a trivial SHA‑256 checksum, anyone within ~15 m can flash arbitrary firmware via BLE. The bar is USB‑connected and already enumerates as a HID, so a tiny patch turns it into a remote Rubber Ducky–style keyboard and potential bugging device. Creative’s response: this is not a cybersecurity risk; no vendor fix exists, so the researcher released an unofficial firmware patcher that disables CTP over Bluetooth.

---

### Comment pulse
- Vendor denial is absurd → remote arbitrary firmware flashing on a USB‑trusted, mic‑equipped device is textbook vulnerability, even if attack radius is small.  
- Pattern: hardware brands bolt on software/BLE late, often via opaque third parties, leaving unmaintainable, unaudited firmware and no real security ownership.  
- Some argue practical risk is low (niche device, proximity required) → vendor likely did a crude cost–benefit and decided to ignore it—counterpoint: that normalizes unsafe designs.

---

### LLM perspective
- View: This is a classic “peripheral as attack vector” case; USB HID + unauthenticated OTA is an especially toxic combo.  
- Impact: Any BLE‑enabled peripheral with update channels should now be suspect; corporate security baselines need to treat them as potential endpoints.  
- Watch next: Independent audits of popular USB/BLE peripherals, OS‑level controls over new HID devices, and pressure for signed, authenticated firmware updates.
