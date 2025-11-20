# Show HN: I made a down detector for down detector

- Score: 524 | [HN](https://news.ycombinator.com/item?id=45974012) | Link: https://downdetectorsdowndetector.com

- TL;DR  
WebFetch’s “DownDetector’s Down Detector” is a small site that pings downdetector.com from several regions to answer the question “is the outage tracker itself down?”. It even adds recursive domains that watch each other for comic effect. HN commenters mostly enjoy the joke but also discuss the serious need for independent status checks on separate stacks, nuances of the recent Cloudflare-related Downdetector incident, and broader choices between US and European infrastructure providers and their perceived reliability.

- Comment pulse  
  - Using a separate “down detector for DownDetector” illustrates good practice: independent monitors on different stacks/regions reduce correlated failures—counterpoint: recursion here is playful, not robust SRE.  
  - Thread branches into EU vs US infrastructure: some solo devs happily migrated to Hetzner/Bunny/Infomaniak; others note incidents there too and Cloudflare/AWS’s visibility bias.  
  - Several clarify Downdetector’s recent “outage” was Cloudflare’s human-verification breaking, leaving the site technically up but effectively unusable—status checkers should model this distinction.

- LLM perspective  
  - View: Turning a joke into a tiny multi-region probe nicely demonstrates composable monitoring patterns without overengineering.  
  - Impact: Indie tools like this highlight gaps in perceived reliability and transparency of large status pages and outage trackers.  
  - Watch next: Generalized “status of status pages” tools combining synthetic checks, crowdsourced reports, and clear degraded-vs-down labeling.
