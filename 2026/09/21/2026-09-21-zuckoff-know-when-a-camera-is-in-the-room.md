# ZuckOff Know when a camera is in the room

- Score: 604 | [HN](https://news.ycombinator.com/item?id=49785429) | Link: https://zuckoff.app/

### TL;DR

ZuckOff listens for Bluetooth manufacturer signatures and names associated with camera glasses, then displays evidence, rough signal strength, and a local device log. It covers several Meta, Luxottica, Snap, and Oculus identifiers, supports alerts and exports, and says no account or off-device transfer is required. The site explicitly warns that silent devices can evade detection and that a nearby match does not prove recording. The sparse HN discussion redirects readers to an older thread and recommends an established open-source alternative instead.

### Comment pulse

- Detection is probabilistic rather than definitive → quiet glasses may be missed, while a recognized broadcast proves neither who wears them nor active recording.
- Commenters prefer the open-source predecessor → they characterize it as hand-coded, tracker-free, and free of in-app purchases.

### LLM perspective

- View: Transparent limitations make this useful as an awareness sensor, not a camera detector in the strict sense.
- Impact: Users can notice some nearby wearables, but acting on uncertain alerts could create needless confrontation.
- Watch next: Publish reproducible captures, rule updates, false-positive rates, privacy audits, and comparisons with the cited alternative.
