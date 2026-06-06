# Show HN: Building a web server in assembly to give my life (a lack of) meaning

- Score: 386 | [HN](https://news.ycombinator.com/item?id=48080587) | Link: https://github.com/imtomt/ymawky

## TL;DR

Ymawky is a fork-per-connection web server for Apple Silicon macOS, written entirely in ARM64 assembly with direct syscalls and no libc. It serves static files from a local docroot on 127.0.0.1, supports HTTP/1.0/1.1, range requests, multiple methods (GET/PUT/DELETE/HEAD/OPTIONS), MIME-type detection, directory listings and custom error pages. The author adds safeguards like path traversal checks, size limits, timeouts, atomic PUT uploads and process caps. HN commenters treat it as both a serious low-level learning project and a joyful “art piece” in an AI-heavy era.

## Comment pulse

- Assembly isn’t magical → once you build abstractions with macros/procedures, large assembly projects feel similar to higher-level languages; reading is harder than writing.  
- Passion projects matter → building complex things “by hand” is likened to Minecraft maps: commercially useless maybe, but uniquely meaningful and creatively valuable.  
- Community inspiration → others share similar asm web servers; author credits prior work and a parody O’Reilly cover as direct motivation.

## LLM perspective

- View: This is an unusually thorough example of a real HTTP server built directly on syscalls, ideal for educational code reading.  
- Impact: Best suited for systems-programming learners, security folks, and curious web devs wanting to see HTTP/OS details without framework noise.  
- Watch next: Ports to Linux, minimal benchmarks, and a hardening/security-audit writeup would turn it into a canonical assembly reference.
