# Man accidentally gains control of 7k robot vacuums

- Score: 172 | [HN](https://news.ycombinator.com/item?id=47111400) | Link: https://www.popsci.com/technology/robot-vacuum-army/

### TL;DR

While building a game-controller app for his DJI Romo vacuum, engineer Sammy Azdoufal discovered that his credentials exposed nearly 7,000 other devices across 24 countries. He could reportedly access live cameras, microphones, maps, status data, and approximate locations because DJI’s backend treated him as their owner. He disclosed the issue rather than exploiting it; DJI says automatic patches on February 8 and 10 resolved it. Commenters called for penalties, local operation, and open protocols, while disagreeing that enthusiast firmware is practical for ordinary buyers.

### Comment pulse

- Similar credential failures in thermostats suggest a recurring device-identity problem, with potential effects ranging from surveillance to coordinated power demand.
- Local-only replacement software reduces cloud exposure — counterpoint: installation and maintenance can defeat the labor-saving purpose for many consumers.
- Readers treated internet dependence as an anti-feature and argued that exposing household cameras and microphones should trigger meaningful regulatory penalties.

### LLM perspective

- **View:** Remote sensors turn an authorization defect into physical surveillance, so device ownership requires stronger isolation than ordinary account data.
- **Impact:** Vendors must isolate device identities and minimize remote sensor access; consumers cannot repair server-side trust failures locally.
- **Watch next:** DJI’s additional controls, independent retesting, user notification, audit requirements, local-mode availability, and penalties for mass exposure.
