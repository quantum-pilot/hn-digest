# A decentralized peer-to-peer messaging application that operates over Bluetooth

- Score: 558 | [HN](https://news.ycombinator.com/item?id=46675853) | Link: https://bitchat.free/

### TL;DR

Bitchat is a public-domain messaging app for iOS, macOS, and Android that forms nearby Bluetooth mesh networks without internet, servers, or phone numbers. Devices discover peers and relay messages across hops, aiming to preserve communication during outages, disasters, protests, or poor connectivity. Discussion focuses less on censorship claims than practical limits: absent store-and-forward delivery, short radio range, mobile background restrictions, congested airtime, and the recurring advantage of well-placed repeaters. Alternatives and cross-platform reach also shape trust and usefulness.

### Comment pulse

- Reliability gap → without deferred store-and-forward, recipients must be present; commenters cite older systems and optional caching nodes as proven designs.
- Radio tradeoff → Bluetooth bootstraps local meshes, but limited range, scarce airtime, and scaling pressures favor LoRa or repeaters.
- Adoption divide → cross-platform availability helps, while distrust of sponsors and established alternatives complicates choosing a shared network.

### LLM perspective

- View: Infrastructure independence matters, but asynchronous delivery and propagation reliability determine whether the mesh works beyond demonstrations.
- Impact: Nearby groups gain an emergency channel; disconnected communities still need couriers, repeaters, or alternative radios.
- Watch next: Store-and-forward support, background behavior, large-event tests, battery use, and interoperability between platforms.
