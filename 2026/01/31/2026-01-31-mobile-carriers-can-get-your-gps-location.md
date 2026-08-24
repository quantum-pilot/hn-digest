# Mobile carriers can get your GPS location

- Score: 375 | [HN](https://news.ycombinator.com/item?id=46838597) | Link: https://an.dywa.ng/carrier-gnss.html

### TL;DR

The author argues that cellular location extends beyond tower-derived estimates: 2G/3G RRLP and 4G/5G LPP can ask a handset to return its own GNSS coordinates through control-plane signaling that users rarely see. Historical cases are cited as evidence that carriers or authorities have obtained precise phone coordinates, but the author explicitly does not know whether those protocols were the mechanisms used. Apple’s iOS 26.3 feature limits precise location sharing on supported in-house-modem devices; the author wants users to control GNSS responses and be notified of requests.

### Comment pulse

- Accountability dominated → commenters wanted opt-outs, notifications, legal recourse, and penalties when agencies or companies bypass user choices.
- Emergency tradeoffs surfaced — counterpoint: disabling precise responses may protect privacy but could impair location during crash detection or emergency calls.
- Alternative meshes drew interest → users debated LoRa range, routing, encryption placement, congestion, and radiolocation risk.

### LLM perspective

- View: The article describes a protocol capability while carefully withholding certainty about which systems specific authorities actually used.
- Impact: Invisible handset-assisted positioning complicates assumptions that disabling app permissions prevents carriers from obtaining precise coordinates.
- Watch next: Device and carrier support, emergency exceptions, user-visible logs, remote-request controls, retention policy, and independent protocol testing.
