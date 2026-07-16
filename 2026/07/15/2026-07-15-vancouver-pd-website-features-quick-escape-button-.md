# Vancouver PD website features Quick Escape button that wipes itself from history

- Score: 352 | [HN](https://news.ycombinator.com/item?id=48914644) | Link: https://vpd.ca/

### TL;DR
Vancouver Police Department’s website now has a “Quick Escape” button for people browsing safety or abuse resources while under surveillance. Clicking it fades the page out, renames the tab, opens a benign site in a new tab, and replaces the current page with Google, reducing obvious traces in browser history. Hacker News commenters compare this to more mature “exit quickly” designs in the UK and New Zealand, praise trauma‑informed UX, but note serious privacy gaps around cookies, storage, and discoverability.

---

### Comment pulse
- Gov.uk “exit this page quickly” pattern → thoughtful research (e.g., triple‑Shift shortcut) balances safety, plausibility, and not drawing attention—counterpoint: discoverability for at‑risk users remains hard.  
- NZ “Shielded Site” → in‑page iframe avoids history/cookie traces and is widely embedded on government/bank sites, plus zero‑rated data for access on some carriers.  
- VPD implementation → hard‑coded redirects, brightness change, and untouched cookies/storage may still expose victims if abusers are technically savvy or observant.

---

### LLM perspective
- View: These patterns are valuable harm‑reduction tools, but mustn’t be oversold as true anonymity or full safety.  
- Impact: Domestic abuse survivors and support orgs gain a bit more plausible deniability; browser and design standards may adapt.  
- Watch next: Standardized “safe exit” components, browser‑level APIs for ephemeral sessions, and audits of real‑world effectiveness against abuser tactics.
