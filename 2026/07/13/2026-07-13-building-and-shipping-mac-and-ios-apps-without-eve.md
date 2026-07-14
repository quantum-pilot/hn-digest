# Building and shipping Mac and iOS apps without ever opening Xcode

- Score: 256 | [HN](https://news.ycombinator.com/item?id=48896665) | Link: https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/

### TL;DR
The piece describes how to fully build, sign, notarize, and ship Mac and iOS apps using command‑line tools and scripts—often generated and driven by coding agents like Claude—without ever opening Xcode’s GUI. It leans on Xcode’s underlying CLIs plus automation pipelines that an LLM can both author and operate. Hacker News discussion focuses on security risks of giving agents broad filesystem access, sandboxing via VMs/containers or separate users, emerging non‑Xcode tools, and the slightly surreal, self‑referential “Claude teaching you to ask Claude” dynamic.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Running agents on your main Mac is risky → people report LLMs exfiltrating home dirs; mitigate with VMs, Docker, separate users, or offline SSH keys.  
- iOS apps can be built from Linux/WSL → tools like xtool and sideloadly let you compile and sideload IPAs over USB without Xcode.  
- New CLIs (strudel, Axiom) wrap Apple tooling → they expose signing/notarization/DMG creation in LLM‑friendly ways—counterpoint: true Linux build servers still blocked by Xcode/macOS dependency.

---

### LLM perspective
- View: Treat Xcode as a headless backend; let LLMs drive its CLIs while humans review scripts and logs.  
- Impact: Lowers friction for indie devs and scripting‑oriented teams; also reshapes how CI and remote build farms handle Apple platforms.  
- Watch next: Hardened agent sandboxes, reproducible VM images for Apple builds, and whether Apple formalizes LLM/automation support around its toolchain.
