# Tether: iMessage, SMS, etc. on Linux

- Score: 432 | [HN](https://news.ycombinator.com/item?id=49415386) | Link: https://zackbartel.com/blog/2026/08/tether/

### TL;DR

Tether links an iPhone with Linux to provide iMessage and SMS access, notifications, contacts, file transfer, clipboard synchronization, and browser OTP autofill. Its paired components communicate with mutual TLS, while Bluetooth protocols provide messaging features and Firefox- and Thunderbird-family extensions handle emailed codes. The author describes difficult Bluetooth edge cases and a clean-room MIT implementation inspired by prior GPL projects. Discussion highlights Apple interoperability barriers, technical limitations around message metadata, possible call support, and an immediate relicensing of ancs4linux to MIT.

### Comment pulse

- Open interoperability gained momentum → ancs4linux’s author responded to the licensing concern by switching the project to MIT.
- Bluetooth remains imperfect → prior implementers struggled with group recipients, attachments, links, adapter variability, and ANCS behavior.
- The iPhone app is still a broker → commenters distinguish this bridge from direct participation in Apple’s private ecosystem.

### LLM perspective

- View: Tether succeeds by combining several partial interfaces into useful continuity, not by fully recreating Apple’s stack.
- Impact: Linux users can keep iPhones without surrendering routine desktop messaging and transfer conveniences.
- Watch next: Phone-call support, client compatibility, Bluetooth reliability, and security review are the clearest expansion tests.
