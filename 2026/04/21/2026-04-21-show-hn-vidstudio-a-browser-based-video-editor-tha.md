# Show HN: VidStudio, a browser based video editor that doesn't upload your files

- Score: 234 | [HN](https://news.ycombinator.com/item?id=47847558) | Link: https://vidstudio.app/video-editor

### TL;DR

VidStudio is a free, accountless video editor that keeps source files, projects, and rendering inside the browser, using WebCodecs, FFmpeg WebAssembly, Workers, and IndexedDB. It advertises multitrack timelines, frame-accurate seeking, source trimming, transforms, text, and H.264/AAC MP4 export; practical limits come from device memory, browser codec support, and local-only project storage. Hacker News praised its speed, transparent persistence, and related conversion tools, but testers hit codec failures and incomplete track handling. The creator also acknowledged overlooked FFmpeg licensing obligations and promised compliance changes.

### Comment pulse

- Local processing restores privacy and instant distribution — counterpoint: browser codecs, RAM ceilings, and nonportable IndexedDB projects constrain reliability.
- A Firefox tester praised performance but found track movement unclear; the creator confirmed clips cannot yet move between tracks.
- FFmpeg’s LGPL permits closed applications only with compliance duties; codec configuration may introduce stronger GPL requirements.

### LLM perspective

- **View:** The privacy architecture is the strongest differentiator; feature breadth matters less until import and timeline basics work consistently.
- **Impact:** Creators gain a no-upload option for sensitive footage, while failed codec paths can still block ordinary phone recordings.
- **Watch next:** Published FFmpeg sources and relinking path, GPL codec choices, decoding, track manipulation, offline installation, and cross-device project portability.
