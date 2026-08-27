# How Quake.exe got its TCP/IP stack

- Score: 459 | [HN](https://news.ycombinator.com/item?id=45962654) | Link: https://fabiensanglard.net/quake_chunnel/index.html

### TL;DR

The DOS version of Quake gained internet multiplayer under Windows 95 through Mpath's Chunnel, not a native TCP/IP stack. A launcher loaded a DLL and virtual device driver that intercepted software interrupt 0x48, marshalled BSD-style socket calls across the DPMI boundary, and routed them to Windows Winsock. This avoided an expensive DOS networking package and disappeared once Win32 Quake variants called Winsock directly. Commenters recalled DJGPP, null-modem play, and the difficult networking landscape around early PC games.

### Comment pulse

- The bridge impressed technically minded readers → it connected protected-mode DOS code to Win32 networking with carefully marshalled calls.
- Period memories broadened the story → commenters recalled IPX, serial links, DJGPP, and poor latency from native DOS TCP/IP attempts.

### LLM perspective

- View: Chunnel was a pragmatic compatibility layer that turned Windows 95 into Quake's network adapter.
- Impact: Players gained accessible internet multiplayer without buying specialized DOS TCP/IP software.
- Watch next: Preservation efforts should document the proprietary Mpath components alongside the surviving Quake-side implementation.
