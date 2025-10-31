# Hello-World iOS App in Assembly

- Score: 170 | [HN](https://news.ycombinator.com/item?id=45755821) | Link: https://gist.github.com/nicolas17/966a03ce49f949dd17b0123415ef2e31

TL;DR
A hand-written ARM64 iOS “Hello World” shows how to bootstrap UIKit entirely from assembly: set up an autorelease pool, build an AppDelegate class dynamically via the Objective‑C runtime, call UIApplicationMain, create a UIWindow and UIViewController, and paint the screen yellow. The code showcases selectors, objc_msgSend, register saving, and CoreFoundation string construction. HN finds it a great learning artifact but impractical for production, notes it still rides atop UIKit, asks for build/deploy steps and calling‑convention nits, and debates App Store/optimization realities.

Comment pulse
- Assembly teaches internals → understanding calling conventions and stack discipline helps when frameworks misbehave — counterpoint: still atop UIKit; not truly “bare metal.”
- Practicality questioned → unlikely App Store win; real speedups come from bypassing UIKit and driving GPU/Metal directly.
- Nits and asks → register preservation doubts, ARM “word” terminology confusion, and a request for build/deploy instructions.

LLM perspective
- View: Great minimal demo of ARM64 + Obj‑C runtime; not a pattern for shipping apps.
- Impact: Improves debugging literacy: crash triage, symbolization, selector mismatches, and interop with C/Swift.
- Watch next: Release build scripts for clang/ld; show Metal triangle from assembly; verify calling conventions and register clobbers with tests.
