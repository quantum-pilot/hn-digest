# Helping Valve to power up Steam devices

- Score: 363 | [HN](https://news.ycombinator.com/item?id=46006616) | Link: https://www.igalia.com/2025/11/helpingvalve.html

- TL;DR  
    - Igalia describes its deep work with Valve on powering new Steam devices, especially the ARM-based Steam Frame VR headset. They extend FEX to translate x86 games to ARM and massively improve Mesa3D’s Turnip Vulkan driver for Qualcomm Adreno GPUs, adding optimizations, Vulkan extensions, CTS coverage, and automated visual regression testing. Kernel work (LAVD scheduler) and AMD display improvements target low-power, HDR-capable SteamOS hardware. HN readers praise Valve’s FOSS-first approach, criticize Qualcomm’s drivers, and speculate about future ARM Steam Deck-style devices.

- Comment pulse  
    - Valve backing Turnip and FEX is applauded → Qualcomm’s proprietary Adreno drivers underperform, so community-built Vulkan support feels like correcting a vendor failure.  
    - Valve seen as consumer-friendly → FOSS aligns with selling games, not platforms; goodwill becomes a profitable moat — counterpoint: motives are still purely commercial.  
    - Groundwork for ARM handhelds looks strong → Steam Frame, existing Snapdragon consoles, and BORE-like schedulers promise efficient portables beyond today’s AMD-based Steam Deck.

- LLM perspective  
    - View: Valve’s investment shows high-end Linux gaming now depends as much on toolchains and drivers as on silicon.  
    - Impact: Open Mesa/FEX stack on Adreno makes non-x86, non-AMD hardware viable for mainstream PC games and VR headsets.  
    - Watch next: measurable LAVD gains, ARM-based SteamOS devices, and whether Qualcomm embraces or competes with community drivers like Turnip.
