# Microsoft new Outlook takes 10 seconds to do what Outlook Classic does instantly

- Score: 587 | [HN](https://news.ycombinator.com/item?id=48584207) | Link: https://www.windowslatest.com/2026/06/15/microsofts-new-outlook-takes-10-seconds-to-do-what-outlook-classic-does-instantly-on-windows/

### TL;DR

Windows Latest measured New Outlook taking about 10 seconds to open a message from a Windows notification, versus near-instant Outlook Classic; manually opening New Outlook and selecting the message took roughly five seconds. The WebView2 client also used 10 processes, 490–636 MB idle memory, and about 4% idle CPU, compared with Classic’s 117–148 MB and under 1%. Microsoft delayed enterprise migration to March 2027, while HN blamed broader software-quality incentives—but pushed back that web technology itself is not destiny, citing faster webmail implementations and Outlook’s own browser version.

### Comment pulse

- WebView2 is not sufficient explanation → Fastmail and Outlook.office.com can feel fast; poor load order and unnecessary rendering are implementation choices.

- Perceived latency matters → incremental rendering and immediate input handling can make slow work usable; Outlook sometimes drops typing before reply UI appears.

- Platform frustration drives switching → several users moved personal or work workflows to Linux — counterpoint: specialized Windows and RDP features remain hard to replace.

### LLM perspective

- **View:** The notification path is a product regression: startup parity is irrelevant when the user’s intended message arrives last.

- **Impact:** Enterprise users lose time at high frequency; IT departments face migration resistance and longer dependence on Classic Outlook.

- **Watch next:** July PST import, August unified inbox, offline behavior, notification fixes, and Classic support through April 2029.
