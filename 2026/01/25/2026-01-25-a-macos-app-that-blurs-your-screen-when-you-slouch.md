# A macOS app that blurs your screen when you slouch

- Score: 433 | [HN](https://news.ycombinator.com/item?id=46754944) | Link: https://github.com/tldev/posturr

### TL;DR

Posturr is an open-source macOS utility that uses the camera and Apple’s Vision framework to estimate posture locally. After calibration, it tracks nose and shoulder positions, progressively blurs every display when the user deviates, and clears the blur when posture improves. Menu controls expose sensitivity, dead zone, recalibration, and a compatibility renderer; the default blur relies on a private CoreGraphics API. It supports macOS 13+, multiple displays, and keeps images unstored and untransmitted. The project is MIT-licensed but its documented download requires a one-time Gatekeeper bypass.

### Comment pulse

- Fixed posture is not settled science → commenters favor frequent movement — counterpoint: a calibrated reminder may still interrupt prolonged slouching.
- Laptop ergonomics limit software remedies → sustained work often still needs a raised screen and external keyboard.

### LLM perspective

- View: Local processing makes the camera-based intervention unusually privacy-conscious.
- Impact: Immediate visual friction may change habits, but false detections can disrupt concentration.
- Watch next: Detection accuracy, private-API breakage, signing, and evidence that posture enforcement reduces discomfort.
