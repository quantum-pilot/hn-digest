# How Quake.exe got its TCP/IP stack

- Score: 459 | [HN](https://news.ycombinator.com/item?id=45962654) | Link: https://fabiensanglard.net/quake_chunnel/index.html

### TL;DR
The article explains how id Software shipped a single DOS binary, quake.exe, that could run both on bare DOS and under Windows 95 while gaining better networking on Windows. Quake was built with DJGPP and used CWSDPMI as its DOS extender; crucially, its DPMI client was designed to interoperate not only with CWSDPMI’s server but also with Windows 95’s DPMI host. This let the same executable benefit from Win95’s TCP/IP stack instead of relying solely on DOS networking drivers. Hacker News comments reminisce about DJGPP, early TCP/IP stacks, and DIY cabling.

---

### Comment pulse
- DOS extenders like DOS/4GW and CWSDPMI were swappable → users sped up loading by switching runtimes — counterpoint: commenters insist credit for DJ and Sandmann.  
- Early TCP/IP on DOS/Linux used userland stacks → KA9Q and Beame & Whiteside enabled networking pre-native support, but configuration and latency made Internet Quake impractical.  
- DIY hardware culture thrived → kids built null-modem cables and Covox-like sound devices to play multiplayer or MOD music, learning soldering and electronics along way.  

---

### LLM perspective
- View: Quake’s DPMI trick is an early example of targeting a low-level ABI instead of an OS, yielding surprising portability.  
- Impact: This approach let id ship one binary across DOS and Windows 95, easing players’ transition and simplifying distribution and patching.  
- Watch next: Similar techniques matter today for games on Steam Deck, Proton, and Wine; ABI choices can extend lifespans across platform shifts.
