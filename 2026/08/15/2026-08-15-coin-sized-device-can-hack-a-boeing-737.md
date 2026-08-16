# Coin-sized device can hack a Boeing 737

- Score: 120 | [HN](https://news.ycombinator.com/item?id=49282951) | Link: https://www.wired.com/story/this-coin-sized-device-can-hack-a-boeing-737/

### TL;DR

Researchers built a sub-$100, coin-sized Wi-Fi implant that, after brief physical access to an externally reachable Boeing 737 port, can overpower signals on an internal avionics bus. In a test bed and Boeing lab, it spoofed autopilot waypoints and takeoff-related values while hiding changes from one cockpit display. Manual control and another display offer recovery paths, and Boeing says existing layers limit real-world feasibility. Commenters debated whether trusted-maintainer access makes this ordinary insider risk or exposes an avoidable, unauthenticated design weakness.

### Comment pulse

- Physical access is the hard part → counterpoint: airside staff can blend near aircraft, and trusted roles have enabled past breaches.
- Maintenance workers already reach critical systems → trust does not justify leaving a high-privilege signal path unauthenticated or easily implantable.
- Disabling or sealing the connector seems simplest → readers questioned what maintenance function it serves and whether safer access can replace it.

### LLM perspective

- View: The finding updates aviation’s insider-threat model: trusted physical access should not automatically grant unauthenticated command authority.
- Impact: Airlines may tighten ground access and inspections before costly avionics redesigns add isolation, detection, or authentication.
- Watch next: Seek independent replication, affected-fleet scope, Boeing mitigation details, and operational controls for detecting hidden implants.
