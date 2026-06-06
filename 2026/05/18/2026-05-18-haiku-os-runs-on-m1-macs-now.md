# Haiku OS runs on M1 Macs now

- Score: 256 | [HN](https://news.ycombinator.com/item?id=48183579) | Link: https://discuss.haiku-os.org/t/my-haiku-arm64-progress/19044?page=2

### TL;DR
Haiku OS, the BeOS-inspired desktop OS, now boots on Apple Silicon, including bare-metal on an M1 MacBook Air via m1n1 + U-Boot, treating it like a UEFI PC. The current ARM64 port is highly experimental: mouse input is choppy in UTM, USB is fragile, display initially needed custom color-space conversion for Apple’s 10‑bit RGB. Developer tooling and packages are sparse; bootstrap images, manual haikuports setup, and cross-building from x86_64 are required until a dedicated ARM64 package buildbot exists.

---

### LLM perspective
- View: This is a proof-of-concept hardware bring-up, not a daily-driver OS for M1 yet.  
- Impact: Haiku gains relevance on modern ARM laptops and could outclass Linux on some low-power devices.  
- Watch next: Automated ARM64 haikuports builders, USB/input stability, GPU/display polish, and documented install flows for common Apple Silicon models.
