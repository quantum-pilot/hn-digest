# The Tor Project is switching to Rust

- Score: 315 | [HN](https://news.ycombinator.com/item?id=46243543) | Link: https://itsfoss.com/news/tor-rust-rewrite-progress/

## TL;DR
- Tor is progressively replacing its legacy C code with Arti, a Rust-based core aimed at avoiding memory-safety bugs inherent in C. The 1.8.0 release introduces a redesigned, usage-based circuit timeout system with randomized idle shutdowns to make circuit lifetimes less predictable, reducing fingerprinting and linkability. It also adds a command to migrate onion-service authorization keys from classic Tor into Arti’s keystore plus various routing and directory-cache refinements. HN discussion centers on fingerprinting tests, Rust adoption choices, and Tor’s inherent latency.

## Comment pulse
- Browser fingerprinting tests are misleading → EFF’s CoverYourTracks penalizes randomized defenses; combining uniqueness and persistence tests gives a truer sense of tracking risk.  
- Rust is welcomed for security-critical Tor components → memory-safe languages are viewed as strictly better for hostile inputs—counterpoint: pushing Rust into fast-changing UIs can hurt iteration and maintainability.  
- Users complain Tor is slow → latency comes from multi-hop onion routing and network size; Arti targets safety, while Zcash community grants quietly helped fund the rewrite.

## LLM perspective
- View: Another high-risk anonymity system embracing Rust normalizes memory-safe designs across privacy networks, cryptographic stacks, and browser engines.  
- Impact: Safer cores don’t instantly fix ecosystem risk; legacy relays, misconfigured onion services, and user behavior remain major attack surfaces.  
- Watch next: Roadmaps for retiring C relays, hardened operator tooling, and independent measurements of fingerprinting reductions from Arti’s behavioral changes.
