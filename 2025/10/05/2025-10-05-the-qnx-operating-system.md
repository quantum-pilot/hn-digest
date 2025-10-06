# The QNX Operating System

- Score: 152 | [HN](https://news.ycombinator.com/item?id=45481892) | Link: https://www.abortretry.fail/p/the-qnx-operating-system

TL;DR
QNX began at Waterloo in 1979 as a tiny, message‑passing microkernel that brought UNIX‑like multitasking and network transparency to early PCs. It powered Ontario’s diskless ICON school computers, then evolved into POSIX‑compliant QNX 4, the Photon microGUI, and a famed one‑floppy GUI/web demo. Neutrino added portability and SMP; Amiga flirted then chose Linux; automotive became a core market. HN remembers ICONs and the demo’s magic, but also IPC overhead in data‑heavy systems and QNX’s later hobbyist‑unfriendly shift.

Comment pulse
- Microkernel isolation great; message-based I/O added latency, pushing some to Linux with RT patches for FireWire DMA—Law of Conservation of Ugly.
- ICON nostalgia: ARCNET-booted 80186 school machines, trackballs, labs later scrapped; QNX4 DOOM ran on 486SX.
- Dazzling 1.44MB GUI+browser demo impressed; later decisions hurt goodwill: hobbyist license/Photon dropped, self-hosting ended, features locked to products—counterpoint: still prized for reliability.

LLM perspective
- View: QNX shows microkernels can excel in real-time; IPC costs exist, but modularity, restarts, and determinism are strong tradeoffs.
- Impact: Linux’s ecosystem won desktops; QNX thrives in safety-critical embedded/automotive where certifications and predictability dominate.
- Watch next: Compare PREEMPT_RT and seL4 vs QNX latency; track BlackBerry QNX’s openness and ISO 26262/IEC 62304 certification updates.
