# Helping Valve to power up Steam devices

- Score: 363 | [HN](https://news.ycombinator.com/item?id=46006616) | Link: https://www.igalia.com/2025/11/helpingvalve.html

### TL;DR

Igalia details open-source work commissioned by Valve for new Steam hardware. For the ARM-based Steam Frame, FEX translates x86 code while Mesa's Turnip driver gained Adreno 700 support, tiled rendering, LRZ and autotuning improvements, plus correctness work across DXVK, vkd3d, and Zink. Testing spans more than 2.8 million Vulkan CTS cases and game-frame captures. Igalia also developed the Rust-based LAVD scheduler for latency and energy goals, while contributing AMD display and HDR work for Steam Machine.

### Comment pulse

- Readers praised Valve's upstream investment and contrasted it with dissatisfaction over Qualcomm's proprietary driver support.
- ARM Steam Deck speculation met a practical objection: available chips may not deliver Valve's desired performance leap.

### LLM perspective

- View: The durable product here is shared infrastructure, not merely support for one hardware launch.
- Impact: Upstream drivers and schedulers can lower costs for Linux gaming devices beyond Valve's catalog.
- Watch next: Real-device compatibility, FEX overhead, battery behavior, and adoption by third-party handhelds.
