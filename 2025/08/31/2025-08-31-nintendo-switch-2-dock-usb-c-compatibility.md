# Nintendo Switch 2 Dock USB-C Compatibility

- Score: 298 | [HN](https://news.ycombinator.com/item?id=45087971) | Link: https://www.lttlabs.com/blog/2025/08/30/nintendo-switch-2-dock

- TL;DR
  - LTT Labs sniffed USB‑C PD traffic on Switch 2, its dock, and third‑party gear. They saw the console cap at ~15 W, Nintendo’s dock request 20 V/3 A upfront, and display‑out succeed only with certain docks/cables; charge times were ~2 h to 90%, ~3 h full. LTT suggests incompatibility may stem from imperfect USB‑C implementations rather than malice. HN debates intentional lock‑in via proprietary Vendor Defined Messages versus normal PD behavior, recalls Switch 1’s USB‑C missteps, and critiques LTT’s technical clarity.

- Comment pulse
  - Nintendo uses proprietary VDM handshake → repeated unstructured messages and a 'key' suggest lockout — counterpoint: VDMs are standard; likely one ID check, not cryptographic.
  - Switch 1 USB‑C was unsafe → users report bricked consoles/phones and e‑marked cable issues; early USB‑C immaturity blamed, with Switch 2 behavior improved.
  - LTT critique → video muddled PD/VDM basics; labs praised for neutrality but asked for clearer, deeper technical explanations.

- LLM perspective
  - View: Likely a modest proprietary handshake to verify dock capabilities (e.g., cooling), not total vendor lockout.
  - Impact: Consumers face accessory roulette; accessory makers must implement handshake; regulators watch USB‑C interoperability claims.
  - Watch next: Teardowns with PD logs; more third‑party docks demonstrating video out; any Nintendo or USB‑IF guidance; reproducible analyzer traces across setups.
