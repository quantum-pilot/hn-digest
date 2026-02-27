# AirSnitch: Demystifying and breaking client isolation in Wi-Fi networks [pdf]

- Score: 309 | [HN](https://news.ycombinator.com/item?id=47167763) | Link: https://www.ndss-symposium.org/wp-content/uploads/2026-f1282-paper.pdf

### TL;DR
The paper systematically analyzes “client isolation” in Wi‑Fi—meant to stop devices on the same network from attacking each other—and finds non‑standard, inconsistent, and often broken implementations. By abusing shared group keys (GTK/IGTK), gateway routing (“gateway bouncing”), and switch‑like behavior of multiple BSSIDs (MAC spoofing/port stealing plus “broadcast reflection”), an authenticated insider or co‑located guest can often gain full MitM over other clients, including on different SSIDs. HN discussion stresses: this bypasses isolation, not Wi‑Fi crypto itself; risk is highest for guest/enterprise/mesh setups.

---

### Comment pulse
- Scope clarification → Attacker must authenticate to some co‑located SSID; co‑author: they “bypass client isolation,” not break all Wi‑Fi encryption—counterpoint: that still undermines many real deployments.  
- Who’s at risk → Enterprises, universities, shared/guest and Xfinity‑style public SSIDs on the same AP; single private home SSID with no guests is relatively safe.  
- Design trade‑offs → Client isolation protects against neighbor abuse but breaks many IoT assumptions; some users carry travel routers or use per‑device VLANs to regain control.

---

### LLM perspective
- View: Treat “client isolation” as untrusted marketing, not a security boundary, unless you’ve audited AP behavior across L2/L3 and multiple BSSIDs.  
- Impact: Network architects for campuses, offices, ISPs, and hotspot providers must redesign guest/private separation and key management; legacy APs may never be fully fixed.  
- Watch next: Vendor patches, a standardized definition of Wi‑Fi isolation, per‑device VLAN tooling, and independent test suites reproducing AirSnitch attacks for commodity gear.
