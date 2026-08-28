# This blog is running on a recycled Google Pixel 5 (2024)

- Score: 365 | [HN](https://news.ycombinator.com/item?id=45110209) | Link: https://blog.ctms.me/posts/2024-08-29-running-this-blog-on-a-pixel-5/

### TL;DR

An unused, carrier-locked Pixel 5 now hosts a Hugo blog through Termux, powered by a 100-watt solar panel and battery station and connected by USB-OTG Ethernet. Termux packages supply Hugo, SSH, cron, service management, editing, and file transfer without a custom ROM or Linux `proot`. A reverse proxy directs traffic to the phone; cron restarts the Hugo server, while `rsync` and Git provide desktop, NAS, and repository backups. The author reports good speed and reliability, with version mismatches and solar battery monitoring as the main early complications.

### Comment pulse

- Readers like reusing phones as low-power servers but question security support, network accessories, and comparison with existing idle infrastructure.
- Battery swelling is the dominant safety concern; proposed mitigations include charge limits, timers, inspection, or battery replacement.

### LLM perspective

- View: The project succeeds by matching an existing device and mature packages to a small, static workload.
- Impact: Reuse can extend hardware life, though battery safety and security updates become operational responsibilities.
- Watch next: Long-term battery condition, patch availability, solar uptime, and performance during traffic spikes.
