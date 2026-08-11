# Nearby Glasses

- Score: 198 | [HN](https://news.ycombinator.com/item?id=47140042) | Link: https://github.com/yjeanrenaud/yj_nearbyglasses

### TL;DR

Nearby Glasses is an Android app that scans Bluetooth Low Energy advertisements for company IDs associated with Meta, Luxottica, and Snap, then warns when a matching device appears within a configurable signal threshold. It stores no telemetry and keeps optional logs locally. Because manufacturer IDs cover many products, including VR headsets, the author emphasizes that false positives and missed glasses are likely and repeatedly warns users not to confront anyone. Field testing reportedly works, though some Pixel users needed the foreground-service setting before scans would start.

### Comment pulse

- Privacy-minded readers welcomed counter-surveillance — counterpoint: manufacturer-level detection cannot establish that someone is wearing or recording with glasses.
- Users suggested richer BLE fingerprints could reduce false positives beyond company IDs, though proprietary and randomized signals complicate reliable identification.
- Pixel reports show foreground-service configuration needs clearer onboarding before the app can serve as a dependable warning tool.

### LLM perspective

- **View:** The app detects vendor proximity, not intent, device type, or active recording.
- **Impact:** Alerts may improve awareness but can also provoke mistaken suspicion toward bystanders.
- **Watch next:** Measured precision, device-specific fingerprints, ignore lists, and a proposed no-glasses-found canary mode.
