# People are using iPad OS features on their iPhones

- Score: 129 | [HN](https://news.ycombinator.com/item?id=45950408) | Link: https://idevicecentral.com/ios-customization/how-to-enable-ipad-features-like-multitasking-stage-manager-on-iphone-via-mobilegestalt/

### TL;DR

A sandbox escape affecting iOS through 26.1 and 26.2 Beta 1 can modify the normally protected MobileGestalt capability cache. By changing device-class and Medusa multitasking keys, experimenters can expose iPad-style windows, dock, multitasking, and Stage Manager on iPhones. The process extracts the plist, locates an encoded key offset in `libMobileGestalt`, modifies it with a Python tool, and repeatedly attempts the unreliable write before rebooting. Incorrect placement can bootloop a device. Commenters see both untapped hardware potential and severe screen-size limitations.

### Comment pulse

- Device-control advocates welcome evidence that Apple ships capabilities users cannot normally choose to enable.
- Practical users doubt windowed apps help on phones, though external displays or reference-and-type workflows could benefit.

### LLM perspective

- View: The experiment reveals shared platform machinery more clearly than it proves a good phone interface.
- Impact: Enthusiasts gain customization at the cost of exploit dependence, instability, and likely update fragility.
- Watch next: Tool integration, external-display behavior, Apple's patch, and recovery success after malformed cache writes.
