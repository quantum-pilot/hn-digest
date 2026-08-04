# Vancouver PD website features Quick Escape button that wipes itself from history

- Score: 352 | [HN](https://news.ycombinator.com/item?id=48914644) | Link: https://vpd.ca/

### TL;DR

The Vancouver Police Department homepage includes a Quick Escape control for visitors who may need to conceal safety-related browsing. Commenters inspecting its JavaScript said activation hides the page, retitles it, opens Canadian weather, and replaces the current tab with Google, reducing immediate visual and history exposure. They also found important limits: cookies, storage, caches, and earlier history remain, while a bright redirect may attract attention. HN compared more considered patterns from GOV.UK—triple-Shift activation—and New Zealand’s embedded Shielded Site, emphasizing discreet triggers, discoverability, and realistic threat modeling.

### Comment pulse

- GOV.UK earned praise → designers researched key choice, redirect destination, and user risk instead of treating escape as simple navigation.
- New Zealand offered stronger containment → an in-page iframe surfaces abuse resources without adding browsing history across government and private sites.
- Triple Shift is discreet → it avoids conspicuous Escape-key tapping — counterpoint: Sticky Keys conflicts and poor discoverability may undermine it.

### LLM perspective

- **View:** A panic control is a safety protocol; partial concealment must be described precisely rather than marketed as erasure.
- **Impact:** At-risk users need consistent, rehearsable behavior across sites; bespoke implementations increase cognitive load under pressure.
- **Watch next:** Test with survivor advocates across mobile, assistive technology, shared devices, storage inspection, slow networks, and blocked pop-ups.
