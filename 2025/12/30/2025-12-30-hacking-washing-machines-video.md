# Hacking Washing Machines [video]

- Score: 204 | [HN](https://news.ycombinator.com/item?id=46428496) | Link: https://media.ccc.de/v/39c3-hacking-washing-machines

### TL;DR
- Talk from 39c3 details how researchers reverse‑engineered BSH and Miele washing machines: probing proprietary internal buses, sniffing undocumented protocols, dumping and modifying firmware, and bypassing debug protections. They then use this knowledge to integrate even older appliances into Home Assistant‑style setups without cloud services, while discussing safety and isolation concerns. HN comments add real‑world stories from appliance testing labs, speculate about attack surfaces, and dig into optical IR diagnostic ports and other hidden interfaces on kitchen devices.

### Comment pulse
- Home appliances are rewarding engineering targets: rich sensor/actuator buses, easy automated testing, and everyday relevance—from LabView-controlled ovens to destructive hinge and grill experiments.  
- Talk humorously highlights new attack surface: compromised washers or dishwashers pranking users, extending IoT threat models into mundane, high-uptime household hardware.  
- Optical IR diagnostic ports give galvanic isolation from mains and simple UART-like IRDA links; commenters note similar hidden ports on devices like Thermomix.  

### LLM perspective
- View: Reverse-engineering proprietary appliance buses strengthens right-to-repair arguments and pressures vendors to adopt open, documented interfaces.  
- Impact: Home automation ecosystems could gain robust offline integrations with legacy machines, reducing dependence on fragile cloud APIs and mobile apps.  
- Watch next: Standardized, safety-reviewed debug and control ports on white goods would balance hackability, isolation, and liability for manufacturers and tinkerers.
