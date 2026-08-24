# Clean-room implementation of Half-Life 2 on the Quake 1 engine

- Score: 313 | [HN](https://news.ycombinator.com/item?id=46958231) | Link: https://code.idtech.space/fn/hl2

### TL;DR

Rad-Therapy II reimplements parts of Half-Life 2 on the open Nuclide/FTE QuakeWorld stack, with game logic built through QuakeC. It is not a complete campaign: deathmatch and other limited modes work, and users must supply original Half-Life 2 and Deathmatch assets from Steam or disc. The code carries an ISC license while Valve retains content rights. Commenters treated it chiefly as an experimental offshoot of open-engine reimplementation work, debated what clean-room means without original or decompiled client code, and pointed to other source ports and demakes.

### Comment pulse

- The project explores compatibility, not replacement → original assets remain mandatory and the single-player game is unfinished.
- Clean-room status concerns process → commenters understood it as avoiding original or decompiled client code, not eliminating every legal question.
- Open-engine value exceeds immediate playability → related FreeHL work targets running legacy content on independently maintained stacks.

### LLM perspective

- View: Its achievement is format and behavior reconstruction across engine generations, even without a complete playable campaign.
- Impact: Engine hackers gain a testbed for QuakeC, Nuclide, FTE, and compatibility with user-supplied licensed commercial assets.
- Watch next: Campaign progress, physics and scripting fidelity, asset-loading coverage, platform support, legal documentation, and upstream Nuclide integration.
