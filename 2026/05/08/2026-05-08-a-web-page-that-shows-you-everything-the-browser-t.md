# A web page that shows you everything the browser told it without asking

- Score: 520 | [HN](https://news.ycombinator.com/item?id=48062178) | Link: https://sinceyouarrived.world/taken

### TL;DR

An interactive page inventories information a browser can expose without a permission prompt: IP-derived location, device and display traits, language, timezone, GPU, fonts, battery data, and user preferences. It turns those signals into a local fingerprint-like barcode while explaining canvas, font, clipboard, and login-detection techniques it says it did not all execute. The creator claims no local storage, transient geolocation, and only two anonymous server events. HN readers agreed fingerprinting matters but criticized low-contrast design, inaccurate deductions, and ominous prose that confuses useful settings with surveillance.

### Comment pulse

- Many location, battery, screen, and lifestyle guesses were wrong, weakening the page’s rhetorical confidence.
- Privacy-focused Firefox configurations reportedly produced stronger protection; others noted inaccurate data can itself resist stable tracking.
- Critics found timezone and theme detection benign — counterpoint: combined signals can identify browsers even when individual inferences are false.

### LLM perspective

- Separate observed values, probabilistic inferences, and merely available APIs to teach capabilities without overstating certainty.
- Fingerprint risk depends on stability and joint uniqueness, not whether each field accurately describes the person.
- Measure repeatability across browsers, sessions, VPNs, and privacy modes.
