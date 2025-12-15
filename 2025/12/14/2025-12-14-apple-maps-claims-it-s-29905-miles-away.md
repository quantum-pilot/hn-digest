# Apple Maps claims it's 29,905 miles away

- Score: 142 | [HN](https://news.ycombinator.com/item?id=46262950) | Link: https://mathstodon.xyz/@dpiponi/115651419771418748

### TL;DR
An AirTag lost in Mexico led Apple Maps to show a distance of 29,905 miles—longer than Earth’s circumference—indicating a path-length/routing bug rather than simple GPS drift. Commenters discuss how accumulated numerical imprecision, penalties for closed roads, and roads’ fractal-like geometry can explode total route length. Others recount Tesla and Volvo navigation systems getting “stuck” after ferries or GPS loss, raise GPS spoofing and dead-reckoning tradeoffs, and lament modern map UIs that even hide basic tools like a scale bar.

### Comment pulse
- Path-length absurdity → likely due to accumulated rounding errors and inflated weights for closed segments, not user mis-estimation—counterpoint: interview “Fermi questions” wouldn’t prevent such bugs.  
- In-car nav bugs → GPS loss plus dead-reckoning and bad mode-switch logic cause wildly wrong positions; vendors also juggle GPS-spoofing risks vs user experience.  
- Mapping UX critique → disappearing scale bars and controls emulate minimalistic scrollbars, but hinder quick, eyeballed distance estimates.

### LLM perspective
- View: Distance UIs should sanity-check against Earth’s circumference and plausible travel speeds, failing gracefully instead of displaying impossible numbers.  
- Impact: Repeatedly wrong distances or stuck locations erode trust in both smartphone and in-car navigation more than minor route quirks.  
- Watch next: Better test suites for ferries/tunnels, adversarial GPS conditions, and clearer map affordances like persistent scale indicators.
