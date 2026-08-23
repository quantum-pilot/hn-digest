# MartyPC is a cross-platform emulator of early PCs written in Rust

- Score: 206 | [HN](https://news.ycombinator.com/item?id=49405816) | Link: https://martypc.net/

### TL;DR

MartyPC is a Rust emulator on Windows, Linux, macOS, and browsers, focused on 8088-era PCs, XTs, and clones, with preliminary PCjr and Tandy 1000 support. Its niche is retro development: cycle-level execution, disassembly, memory inspection, breakpoints, and logging. The developer validates CPU behavior against a physical 8088 and reports 99.9997% cycle accuracy on the V2 suite; research also covers timers, DMA, and buses. Hardware breadth remains uneven, with several devices preliminary or partial. Commenters prized this accuracy-first approach, debated Rust’s suitability, celebrated Adlib support, and clarified the name’s demo-scene origin.

### Comment pulse

- Hardware-backed tests impressed readers because they compare real and emulated execution timing rather than relying only on software expectations.
- Emulator authors praised Rust for reducing memory-management and threading overhead—counterpoint: its prominence also provoked language-choice friction.
- Audio nostalgia centered on Adlib and Covox, while the project name initially suggested an unrelated FM Towns machine.

### LLM perspective

- View: Physical validation makes accuracy measurable, while explicit incompleteness prevents breadth claims from outrunning evidence.
- Impact: 8088 developers gain a diagnostic laboratory capable of exposing timing-sensitive behavior that compatibility-focused emulators may miss.
- Watch next: PCjr, Tandy, V20, DMA, storage, VGA, and parallel-port maturity; broader test suites; easier setup.
