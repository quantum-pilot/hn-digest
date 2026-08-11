# Open Camera is a FOSS camera app for Android

- Score: 197 | [HN](https://news.ycombinator.com/item?id=47219462) | Link: https://opencamera.org.uk/

### TL;DR

Open Camera is a free GPLv3 Android camera app exposing controls many stock apps hide: manual ISO, exposure and focus, RAW, HDR, bracketing, log video, histograms, focus peaking, metadata removal, geotagging, grids, and remote triggers. Availability varies by device and Camera2 support. HN photographers valued disabling computational post-processing, choosing granular resolutions, and retaining noisy aesthetics, but reported a clunky, slow interface. One major compatibility gap is unfilterable phantom camera IDs that can crash Android’s camera server, pushing some privacy-focused ROM users back to a network-blocked Pixel camera app.

### Comment pulse

- Manual controls and minimal processing serve artists seeking camera-like authorship rather than a stock app’s polished computational look.
- Hardware fragmentation remains painful: Fossify lacks multiple lenses, PhotonCamera processes slowly, and Open Camera cannot blacklist broken auxiliary IDs.
- Removing excess EXIF and selecting smaller resolutions reduce unwanted metadata and storage without depending on vendor presets.

### LLM perspective

- **View:** FOSS camera quality depends as much on undocumented vendor hardware behavior as on the app’s feature set.
- **Impact:** Privacy-conscious photographers gain control but may sacrifice lens switching, image pipelines, responsiveness, and device-specific reliability.
- **Watch next:** Auxiliary-camera filtering, Camera2 compatibility reports, processing latency, F-Droid availability, and graceful recovery from camera-server crashes.
