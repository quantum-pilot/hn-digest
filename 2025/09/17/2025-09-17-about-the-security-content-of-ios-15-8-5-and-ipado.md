# About the security content of iOS 15.8.5 and iPadOS 15.8.5

- Score: 346 | [HN](https://news.ycombinator.com/item?id=45270108) | Link: https://support.apple.com/en-us/125142

- TL;DR
  - Apple shipped iOS/iPadOS 15.8.5 for legacy devices to fix an ImageIO out‑of‑bounds write reportedly used in “extremely sophisticated” targeted attacks. Because image parsing runs across many apps, commenters infer a spyware/zero‑click vector and speculate a WhatsApp-linked chain. The backport highlights Apple’s relatively long security support and Android’s uneven timelines, often constrained by chipset vendors. Many see the update as preempting rapid weaponization beyond nation‑state actors. Bottom line: even very old iPhones/iPads should update immediately.

- Comment pulse
  - Apple long security support → longer device lifespan/ROI; Android improving (Pixel 7-year), EU mandates 5-year — counterpoint: iOS 'just works' hides issues, limits debugging.
  - Android updates constrained by Qualcomm/modem driver lifecycles → short kernel/baseband support; Google could extend via contracts; critics note Apple still relies on Qualcomm for modems.
  - Exploit likely in-the-wild spyware via image parsing; WhatsApp chain suggested; backport prevents mass reuse after RE; high-risk users should run newest OS.

- LLM perspective
  - View: Backporting to iOS 15 signals a high-risk, low-interaction image parsing bug worth patching across legacy devices.
  - Impact: Owners of 6s/7/SE1/Air 2/mini 4 and MDM fleets, kiosks, POS iPads gain critical mitigation.
  - Watch next: WhatsApp advisory details, exploit chain writeups, patches for iOS 16–18, and any Apple statement on support windows.
