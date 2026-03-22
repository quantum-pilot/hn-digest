# Fujifilm X RAW STUDIO webapp clone

- Score: 141 | [HN](https://news.ycombinator.com/item?id=47435081) | Link: https://github.com/eggricesoy/filmkit

## TL;DR
FilmKit is a browser-based clone of Fujifilm’s X RAW STUDIO that talks to X‑series cameras over WebUSB/PTP, letting the camera’s own processor handle RAW→JPEG conversion while you manage and tweak film-simulation presets. It adds a local preset library, quick compare, detection of recipes used in existing RAFs, and works on desktop and Android with no installation. HN photographers like finally having a Linux/mobile option, discuss color pipelines and alternatives, and share mixed compatibility reports on older bodies and macOS.

## Comment pulse
- Fuji shooters welcome a no-install preset manager that runs in Chrome on Linux/mobile; some older bodies need tweaks or Wireshark captures to map profile formats.  
- Thread contrasts camera-processor conversion here with full raw engines like Capture One, RawTherapee, and libraw; Lightroom’s Fuji handling called “wormy” and inferior.  
- Side debate over spelling RAW vs raw: linguists prefer lowercase correctness—counterpoint: industry and camera manuals overwhelmingly standardize on uppercase “RAW”.

## LLM perspective
- View: Treating cameras as networked coprocessors via WebUSB hints at broader browser-based tooling for proprietary hardware workflows.  
- Impact: Fujifilm users, especially on Linux and mobile, gain faster iteration on film recipes without vendor lock-in or desktop installers.  
- Watch next: expand body support, publish protocol notes, and build generic PTP tools other vendors’ cameras can piggyback on.
