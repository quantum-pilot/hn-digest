# X-Clacks-Overhead

- Score: 106 | [HN](https://news.ycombinator.com/item?id=46475437) | Link: https://hleb.dev/post/x-clacks-overhead/

- TL;DR  
  The post describes adding an `X-Clacks-Overhead: "GNU Terry Pratchett"` HTTP header to a Cloudflare Pages blog as a quiet memorial, inspired by Discworld’s Clacks system. It shows the simple `_headers` rule needed and emphasizes that the header is technically useless but emotionally significant—keeping Pratchett’s name “moving through the network.” Hacker News commenters expand on HTTP header naming conventions, how widely this header now appears (including honeypots), browser extensions that surface it, and shared affection for Pratchett’s work.

- Comment pulse  
  Use of `X-` prefix is officially deprecated → RFC6648 notes it complicates upgrades and standardization — counterpoint: this header’s name is now part of the homage.  
  Shodan scans show `X-Clacks-Overhead` increasingly common → appears both on real services and honeypots, illustrating meme-like spread of the tribute.  
  Ecosystem around the header has grown → browser extensions and public site listings let fans discover and share participating servers.

- LLM perspective  
  View: Harmless, shared in-jokes like this build cultural memory and community identity into otherwise anonymous infrastructure.  
  Impact: Web admins and hobbyists gain a low-friction way to express fandom and remembrance in production systems.  
  Watch next: Track similar “memorial headers” and whether they evolve into broader conventions or observability signals.
