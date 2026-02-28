# Show HN: RetroTick – Run classic Windows EXEs in the browser

- Score: 171 | [HN](https://news.ycombinator.com/item?id=47180083) | Link: https://retrotick.com/

## TL;DR
RetroTick is a browser-based experiment that loads classic Windows executables and screensavers via drag‑and‑drop, partially re‑implementing Win32 so apps can run client‑side. It also doubles as an in‑browser resource viewer, exposing icons, bitmaps, dialogs and Delphi forms. Commenters like the speed and novelty but report poor compatibility with many real‑world EXEs. A notable thread is the meta-story: much of RetroTick, including its README, was quickly built with Claude Code, highlighting how LLMs accelerate niche emulation projects.

## Comment pulse
- LLM-built project feels timely → README openly recommends using Claude Code; author says core functionality came together within an hour with AI assistance.  
- Compatibility is weak today → one tester’s 22 old games mostly failed or froze, implying big Win32 gaps — counterpoint: others report screensavers working.  
- Resource-inspection shines → hidden ‘View Resources’ menu mimics Resource Hacker in the browser, letting users inspect icons, dialogs, version info, and Delphi forms.

## LLM perspective
- View: Recreating Win32 in WebAssembly with AI help is a powerful pattern for preserving legacy software interactively.  
- Impact: Hobbyist devs can prototype compatibility layers faster, but systematic API coverage still demands manual testing and debugging.  
- Watch next: automated regression suites of popular EXEs, performance benchmarks against Wine/BoxedWine, and tools for crowd-sourced reporting of failing binaries.
