# FFmpeg has issued a DMCA takedown on GitHub

- Score: 543 | [HN](https://news.ycombinator.com/item?id=46394327) | Link: https://twitter.com/FFmpeg/status/2004599109559496984

## TL;DR
FFmpeg issued a DMCA takedown against a Rockchip GitHub repo that had copied FFmpeg code, removed license/attribution, and relicensed it as Apache‑2.0. Commenters clarify that the LGPL doesn’t ban copy‑pasting or static linking itself, but requires preserving license terms and enabling relinking with modified library versions, which Rockchip didn’t do. Others note Rockchip acknowledged licensing issues on GitHub yet delayed remediation for over a year. Discussion then widens to AI‑generated code echoing copyrighted sources without attribution or clear ownership.

*Content unavailable; summarizing from title/comments.*

## Comment pulse
- LGPL nuance → Static linking and copy‑pasting are allowed if users can relink and original notices remain; Rockchip couldn’t legally relicense FFmpeg code as Apache‑2.0.  
- Vendor response → Rockchip noted licensing issues, said they were busy, then stalled ~1.5 years before takedown — counterpoint: archived GitHub discussion is patchy.  
- AI code concerns → Some foresee DMCA-style clashes once LLMs regurgitate licensed snippets; others note AI outputs lack copyright, so original projects retain enforceable rights.

## LLM perspective
- View → Open-source projects increasingly use DMCA tools against SoC vendors that treat community libraries as copy‑paste firmware blobs.  
- Impact → Hardware vendors must budget legal/compliance work for GPL/LGPL code reuse; casual relicensing or header-stripping now risks DMCA embarrassment.  
- Watch next → Track GitHub DMCAs against SoC vendors and whether AI coding tools integrate license checks to prevent infringements.
