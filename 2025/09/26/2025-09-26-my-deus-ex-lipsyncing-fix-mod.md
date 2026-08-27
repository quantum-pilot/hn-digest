# My Deus Ex lipsyncing fix mod

- Score: 259 | [HN](https://news.ycombinator.com/item?id=45382397) | Link: https://www.joewintergreen.com/my-deus-ex-lipsyncing-fix-mod-making-of/

### TL;DR

Joe Wintergreen explains a 2021 Deus Ex mod that repairs facial animation shipped in a degraded state. The UnrealScript used a reversed frame-time condition, disabling mouth-shape tweening at high rather than low frame rates, and its 0.1-second blend was too abrupt. Longer blends, a smooth mouth-close transition after speech, and slower visible blinks substantially improve conversations. One limitation remains outside accessible script code: phoneme updates arrive irregularly and too infrequently, so mouth shapes can still lag the dialogue despite smoother interpolation.

### Comment pulse

- Commenters celebrated extensive community restoration work and discussed another quirky Deus Ex system: cylindrical hit detection that can reject apparent headshots.
- Fans contrasted passionate mods with a newly announced remaster whose visual treatment drew skepticism.

### LLM perspective

- View: Small timing bugs can define a game’s perceived age more than asset resolution or polygon count.
- Impact: Source-adjacent scripting lets modders restore intended behavior even when inaccessible engine code limits completeness.
- Watch next: Whether future source access or remasters improve phoneme sampling without losing the original animation style.
