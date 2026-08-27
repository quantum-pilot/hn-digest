# AppLovin nonconsensual installs

- Score: 113 | [HN](https://news.ycombinator.com/item?id=45584226) | Link: https://www.benedelman.org/applovin-nonconsensual-installs/

### TL;DR

Benjamin Edelman alleges that AppLovin’s Android advertising stack can trigger app installations without meaningful consent. He says decompiled SDK, middleware, and partner-helper code traces ad taps—including possible misses on tiny close buttons—to installs, while 208 complaints, screenshots, and a video reportedly match code paths involving countdowns and “InstallOnClose.” Edelman discloses related financial interests and contrasts his evidence with AppLovin’s claim that every download reflects explicit choice. He argues manufacturer and carrier privileges, perhaps intended for device setup, lack safeguards limiting later use.

### Comment pulse

- Commenters described similar Samsung behavior and viewed carrier-granted installer privileges as a broad security risk.
- Suggested defenses included avoiding carrier devices, iOS, device-protection settings, work profiles, or managed-device controls.

### LLM perspective

- View: The cross-check between code paths and user reports makes the allegation substantial, though independently unverified here.
- Impact: Privileged installers turn deceptive ad design into an operating-system trust failure, not merely advertising misconduct.
- Watch next: Manufacturer responses, reproducible tests, and whether installer privileges become time-limited or revocable.
