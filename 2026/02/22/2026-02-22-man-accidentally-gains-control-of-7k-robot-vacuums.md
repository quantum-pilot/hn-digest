# Man accidentally gains control of 7k robot vacuums

- Score: 172 | [HN](https://news.ycombinator.com/item?id=47111400) | Link: https://www.popsci.com/technology/robot-vacuum-army/

- TL;DR  
  - A developer building a joystick app for his DJI Romo vacuum discovered that DJI’s cloud backend effectively authenticated him as owner of almost 7,000 vacuums worldwide, exposing live cameras, microphones, floor maps, and locations. He disclosed the flaw; DJI quickly auto-patched and downplayed it. The incident highlights how trivial backend mistakes in “smart” devices turn household robots into surveillance systems. Hacker News commenters connect this to similar thermostat/HVAC issues, argue over self-hosted alternatives, and call for real fines to deter negligence.

- Comment pulse  
  - IoT reuse-of-credentials pattern → similar flaw reported in Mysa thermostats; commenters fear HVAC hacks could trigger grid-stressing heating or cooling spikes.  
  - Lockdown vs convenience → some advocate Valetudo, fully local vacuums; others say tinkering defeats purpose of time-saving devices and isn’t realistic for most buyers.  
  - Accountability and design critique → many see shared credentials as gross negligence deserving fines; others blame under-resourced engineers and call internet-connected appliances an “anti-feature.”

- LLM perspective  
  - View: Treat every cloud-linked appliance as a security camera; if that feels unacceptable, require local-only modes or skip the product.  
  - Impact: Manufacturers skimping on per-device auth keys, logging, and disclosure processes risk regulatory penalties once incidents reach privacy regulators’ radar.  
  - Watch next: IoT security labels, required third‑party pen‑tests for sensor-rich devices, and simpler, vendor‑supported paths to install open-source firmware.
