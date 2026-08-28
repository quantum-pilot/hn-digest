# Reverse engineering Solos smart glasses

- Score: 166 | [HN](https://news.ycombinator.com/item?id=45087803) | Link: https://jfloren.net/b/2025/8/28/0

### TL;DR

John Floren turned discounted 2018 Solos cycling glasses into a general wireless display by capturing their Android Bluetooth traffic. Replaying packets revealed images encoded as run-length counts plus little-endian RGB565 colors, preceded by a header containing command, length, offset, and 428×240 dimensions. A short Python program converts arbitrary images, chunks them over RFCOMM, and displays them without modifying the glasses. Remaining mysteries include the half-sized length field, repeated transmissions, and commands enabling microphone and speaker support.

### Comment pulse

- Readers suggested the length may count 16-bit words, perhaps inherited from a pre-RLE protocol design.
- Cyclists debated utility and safety; some prefer bike computers, while others value glanceable power and heart-rate data.
- The author is exploring notifications and navigation by displaying directory-generated images newest first.

### LLM perspective

- View: Capturing and mutating known-good packets converted an undocumented accessory into an inexpensive wearable display platform.
- Impact: Hobbyists can prototype heads-up information systems without destructive hardware changes.
- Watch next: Resolving packet semantics, activating audio, and measuring latency for navigation or live notifications.
