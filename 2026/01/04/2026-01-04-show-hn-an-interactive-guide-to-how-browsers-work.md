# Show HN: An interactive guide to how browsers work

- Score: 160 | [HN](https://news.ycombinator.com/item?id=46488654) | Link: https://howbrowserswork.com/

### TL;DR

An open-source interactive guide traces a page load from address-bar input through URL normalization, HTTP request construction, DNS resolution, TCP’s handshake and retransmission, response handling, streaming HTML parsing, DOM mutation, and layout-paint-composite rendering. Small simulations aim to build intuition without installation, deliberately omitting TLS, HTTP-version nuances, and other complexity. HN readers liked the approachable format but requested coverage of dependent resources such as scripts, styles, and images, plus clearer qualification that the DOM model describes modern rather than every historical browser.

### Comment pulse

- Interactive simulations make invisible stages concrete → readers can manipulate requests, packets, parsing, DOM changes, and rendering work.
- Subresource loading is the largest practical gap → scripts, stylesheets, and images explain missing content and parser or render delays.
- Historical precision matters → early and minimalist browsers lacked standardized DOMs, so universal claims should specify modern engines.

### LLM perspective

- View: The guide works as a mental-model scaffold when omissions are explicit and stages remain causally connected.
- Impact: Newcomers gain vocabulary, while web engineers can locate latency and rendering problems earlier.
- Watch next: Add caching, TLS, HTTP/2 and HTTP/3, parser-blocking scripts, subresource discovery, and performance timelines incrementally.
