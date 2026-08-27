# A down detector for down detector's down detector

- Score: 191 | [HN](https://news.ycombinator.com/item?id=45976670) | Link: https://downdetectorsdowndetectorsdowndetector.com/

### TL;DR

This tiny page checks whether another site—already created to monitor Downdetector—is reachable from London, Sydney, and New Jersey, reporting HTTP status and latency. The supplied snapshot showed all three regions operational. Its purpose is mostly a recursive joke about monitoring the monitor’s monitor, and the source offers little beyond that status display. Discussion supplied the substance: readers extended the joke, questioned a monitoring page’s own dependency chain, and suggested that the final reliability layer should be extremely small and independently hosted.

### Comment pulse

- Commenters traced the page’s styling through Tailwind, Vercel, and AWS, weakening its claim to independent resilience.
- The recurring proposal was a dependency-light static page hosted on deliberately separate infrastructure.

### LLM perspective

- View: Recursive monitoring only adds assurance when each layer fails independently from what it observes.
- Impact: Convenience dependencies can quietly collapse a supposedly separate status path into the same failure domain.
- Watch next: Whether the checker removes CDN dependencies and documents how its regional probes are isolated.
