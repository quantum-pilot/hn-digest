# X-Clacks-Overhead

- Score: 106 | [HN](https://news.ycombinator.com/item?id=46475437) | Link: https://hleb.dev/post/x-clacks-overhead/

### TL;DR

A Terry Pratchett fan added `X-Clacks-Overhead: "GNU Terry Pratchett"` to every response from a Cloudflare Pages blog using a simple `_headers` file. The header references the Clacks network in *Going Postal*, keeping Pratchett’s name circulating as a quiet memorial without changing site behavior or performance. HN readers shared similar tributes, browser extensions, and playful custom headers; one technical aside noted that RFC 6648 deprecated the `X-` prefix convention for newly defined application parameters because it creates interoperability and standardization problems.

### Comment pulse

- The signal is a durable memorial → site owners keep Pratchett’s name moving through ordinary network traffic.
- Hidden headers invite playful culture → personal jokes and extensions turn invisible metadata into small moments of discovery.
- The name preserves legacy convention → newer custom parameters generally should avoid `X-`, according to RFC 6648.

### LLM perspective

- View: Technically unnecessary conventions can still carry community memory and make infrastructure feel human.
- Impact: Static-site operators can participate with one configuration line and no visible interface changes.
- Watch next: Check header persistence across CDNs, asset paths, redirects, and future platform configuration changes.
