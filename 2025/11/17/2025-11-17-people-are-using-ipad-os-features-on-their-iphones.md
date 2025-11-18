# People are using iPad OS features on their iPhones

- Score: 129 | [HN](https://news.ycombinator.com/item?id=45950408) | Link: https://idevicecentral.com/ios-customization/how-to-enable-ipad-features-like-multitasking-stage-manager-on-iphone-via-mobilegestalt/

- TL;DR
  - An iOS sandbox escape targeting itunesstored/bookassetd lets tinkerers edit MobileGestalt on iPhones to mimic iPads: set DeviceClassNumber to iPad and enable Medusa/Stage Manager keys, unlocking windowed multitasking and the iPad dock on iOS 26.1/26.2b1. It requires finding offsets in libMobileGestalt, a Python script, repeated attempts, and carries bootloop risk if miswritten. HN debates utility: some want simplicity and will disable windows; others celebrate a glimpse of unlocked potential; practicality on small screens is questioned, with external displays suggested.

- Comment pulse
  - I want simplicity; iPadOS windows confuse users → seniors struggle; Apple offers toggles and you can disable windowing — counterpoint: defaults still surface complexity.
  - Unlock the device’s potential → locked-down iOS wastes powerful hardware; brief openness shows what developers could build; maybe suited for future foldable iPhones.
  - Small screens limit utility → windowed apps feel cramped on 11-inch iPad; better with external display, keyboard, mouse; also underscores iOS/iPadOS are largely the same.

- LLM perspective
  - View: Userland sandbox escape flips MobileGestalt flags; no root, brittle, and likely to be patched quickly by Apple.
  - Impact: Boosts tweak tooling (Nugget, Misaka), iCloud-bypass tooling, and security research; end users risk instability or bootloops if CacheData is miswritten.
  - Watch next: Patches in iOS 26.2/26.3, stricter MobileGestalt access, success-rate improvements, and any proof of external-display enablement on iPhones.
