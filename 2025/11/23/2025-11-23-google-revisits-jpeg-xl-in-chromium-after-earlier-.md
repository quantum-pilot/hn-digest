# Google Revisits JPEG XL in Chromium After Earlier Removal

- Score: 175 | [HN](https://news.ycombinator.com/item?id=46021179) | Link: https://windowsreport.com/google-revisits-jpeg-xl-in-chromium-after-earlier-removal/

### TL;DR

Chromium’s team reopened its JPEG XL tracker and now welcomes a performant, memory-safe decoder with committed long-term maintenance, but announced no shipping date. A submitted C++ implementation is described as feature-complete, including animation, yet remains under review and may not satisfy the team’s Rust-oriented security expectation. Meanwhile Safari, an optional Windows extension, PDF standardization, and production workflows demonstrate broader adoption. The shift is meaningful permission for outside work, not confirmation that Google itself has resumed implementation or that users can enable support.

### Comment pulse

- Reopening signaled real policy movement → Chrome will accept a maintained memory-safe decoder. — counterpoint: welcoming contributions is not active implementation.
- Codec tradeoffs remained contested → JPEG XL offers speed and mature workflows, while AV2 may improve compression at higher compute cost.
- Current patch drew skepticism → its C++ decoder appears incompatible with Chrome’s stated safety condition despite broad feature coverage.

### LLM perspective

- View: The reopening removes a governance barrier, but decoder ownership and implementation language still determine whether support ships.
- Impact: Native Chrome decoding would reduce deployment friction for archival, photographic, medical, and creative workflows already adopting the format.
- Watch next: Rust decoder maturity, maintainer commitments, Chromium review outcomes, automated test completion, and an actual launch decision.
