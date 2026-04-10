# Top laptops to use with FreeBSD

- Score: 268 | [HN](https://news.ycombinator.com/item?id=47701148) | Link: https://freebsdfoundation.github.io/freebsd-laptop-testing/

- TL;DR  
  - FreeBSD’s laptop compatibility page aggregates probe data and user reports to score graphics, networking, audio, and USB on popular notebooks, highlighting fully supported models like various ThinkPads, Framework laptops, and some HP/ASUS/Acer systems. HN commenters welcome an official guide but stress that wireless networking remains the main pain point, especially Broadcom and some MediaTek chips. Many recommend Intel WiFi or USB dongles, praise FreeBSD’s coherent design (ZFS, jails, stable base), yet note it still demands hands-on tweaking.

- Comment pulse  
  - Intel MacBooks can run FreeBSD well if repurposed; onboard Broadcom WiFi often unusable, needing dongles or card swaps—counterpoint: T2-era models likely problematic.  
  - Older and Gen1 ThinkPads generally work, sometimes after replacing MediaTek WiFi; one user prefers NUC-style desktops, avoiding laptop WiFi/Bluetooth entirely.  
  - Readers doubt matrix reliability given OEM hardware revisions and high scores despite flaky WiFi; suggest USB adapters or bhyve tunneling, lament opaque wireless-driver development.

- LLM perspective  
  - View: Hardware matrix is valuable but must prioritize networking and track sub-model hardware IDs to avoid misleading compatibility claims.  
  - Impact: Clearer guidance could steer FreeBSD users toward WiFi-friendly platforms like Framework and ThinkPad, while discouraging Broadcom/MediaTek-heavy configurations.  
  - Watch next: Watch for updated WiFi stacks, driver backports, and community-maintained dongle lists; these will define FreeBSD’s viability on modern laptops.
