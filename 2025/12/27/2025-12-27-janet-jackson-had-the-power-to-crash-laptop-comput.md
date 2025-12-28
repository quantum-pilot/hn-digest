# Janet Jackson had the power to crash laptop computers (2022)

- Score: 211 | [HN](https://news.ycombinator.com/item?id=46403291) | Link: https://devblogs.microsoft.com/oldnewthing/20220816-00/?p=106994

### TL;DR
A Windows XP-era support case found that Janet Jackson’s “Rhythm Nation” music video could crash certain laptops—sometimes even neighboring machines not playing the video. The audio track contained frequencies that matched a mechanical resonance in a widely used 5400‑rpm hard drive, causing enough vibration to disrupt disk operation. The OEM shipped a secret audio filter to notch out those tones. HN readers connect this to other acoustic–hardware interactions, debunked resonance myths, and fine points of vibration physics and bridge failures.

---

### Comment pulse
- Acoustic resonance in computing → Data centers and storage arrays still battle fan- and sound-induced vibration that disrupts HDD I/O; “Shouting in the Datacenter” and Tesla “earthquake machine” are cited analogues.  
- Too-good-to-be-true stories → Chicken-skull resonance and similar anecdotes get linked and then skeptically debunked—counterpoint: this case has a named engineer and CVE, not pure legend.  
- Meta and physics pedantry → JLo’s dress “inventing” Google Images and Tacoma Narrows “resonance” are invoked; commenters nitpick flutter vs resonance and mock over-grandiose explanatory prose.

---

### LLM perspective
- View → Acoustic coupling into tightly packed, cost-optimized hardware is an underappreciated failure mode that software engineers usually never model.  
- Impact → Hardware vendors, data-center designers, and performance engineers need cross-disciplinary awareness of vibration, airflow, and audio environments.  
- Watch next → Standardized acoustic-stress tests for storage, better documentation of “mystery” filters, and clearer criteria for when such bugs merit security CVEs.
