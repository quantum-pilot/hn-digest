# I Stored a Website in a Favicon

- Score: 288 | [HN](https://news.ycombinator.com/item?id=48606619) | Link: https://www.timwehrle.de/blog/i-stored-a-website-in-a-favicon/

## TL;DR
The author encodes an entire tiny webpage directly into a site’s favicon by treating each pixel’s RGB values as raw storage bytes. A 9×9 PNG (81 pixels × 3 bytes each) comfortably holds a 208‑byte HTML payload plus a 4‑byte length header. JavaScript bootstraps the page: it loads the favicon, draws it to a canvas, reads back pixel data, reconstructs the bytes, then injects the decoded HTML. It’s intentionally impractical but illustrates how “icons” are just arbitrary byte containers.

## LLM perspective
- View: Clever proof‑of‑concept showing every web asset is potential data storage, not just images or HTML.  
- Impact: Inspires browser‑side steganography tricks, code‑golf “smallest site” contests, and security curiosity about odd payload locations.  
- Watch next: Experiments with SVG/ICO metadata, service-worker bootstraps, and detecting or limiting hidden payloads in “innocent” resources.
