# Show HN: The text disappears when you screenshot it

- Score: 528 | [HN](https://news.ycombinator.com/item?id=45284311) | Link: https://unscreenshottable.vercel.app/?text=Hello

### TL;DR

The supplied interactive demo contains only the assertion that its text cannot be screenshotted; the explanation comes from HN discussion. Commenters describe a message perceptible through motion against changing noise but absent from a single captured frame. The protection is easily reversed by combining two screenshots with common layer modes, rapidly alternating captures, lowering rendering quality, or recording video. Participants compared it with random-dot motion effects and animated captchas, treating it as a clever perception experiment rather than secure anti-capture technology.

### Comment pulse

- Multiple frames recover the message through averaging, difference blending, or simple tab switching because temporal information survives outside one screenshot.
- It can add friction — counterpoint: video capture or an external camera defeats any serious sensitive-data use.

### LLM perspective

- View: The demo exploits human temporal perception, but its security premise collapses as soon as an attacker preserves multiple frames.
- Impact: Similar effects may inspire art, games, or demonstrations, yet could create false confidence if presented as data protection.
- Watch next: Examine frame-generation code, accessibility effects, compression behavior, capture-tool variance, and automated multi-frame reconstruction.
