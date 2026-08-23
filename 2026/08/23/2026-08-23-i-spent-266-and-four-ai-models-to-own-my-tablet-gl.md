# I spent $266 and four AI models to own my tablet. GLM-5.3 finished it in a day

- Score: 589 | [HN](https://news.ycombinator.com/item?id=49409073) | Link: https://ericpardee.github.io/fire-hd-ownership/

### TL;DR

After Amazon software repeatedly shut down a 2021 Fire HD 10 kiosk, the author spent five months and $266.15 using four models to gain root on Fire OS 7.3.2.6. Kimi K3 identified an unpatched 2022 Mali vulnerability and built an unreliable exploit; GLM-5.2 diagnosed flaws; GLM-5.3 corrected shifted kernel offsets and page-table assumptions, achieved repeatable root in one day, then removed shutdown-capable Amazon packages. Newer firmware had patched the bug. Commenters debated hardware ownership, American-model safeguards, and whether a simpler non-root ADB command might have sufficed.

### Comment pulse

- Buyers should control paid hardware → the saga shows how protected vendor software can turn ownership into an expensive technical contest.
- Cloud safeguards blocked legitimate-seeming device work → counterpoint: exploit guidance is dual-use, and providers cannot verify ownership from prompts.
- ADB package removal might avoid root → the proposed command was not tested in the supplied account, so equivalence remains unresolved.

### LLM perspective

- View: This is an unusually documented success on stale firmware, not evidence that arbitrary locked tablets are now rootable.
- Impact: AI lowers exploit-development labor, while firmware patching, device isolation, and owner-access policies become more consequential.
- Watch next: Independent reproduction, the suggested ADB alternative, long-term kiosk stability, responsible disclosure details, and any broader affected-device list.
