# Hosting a website on a disposable vape

- Score: 975 | [HN](https://news.ycombinator.com/item?id=45252817) | Link: https://bogdanthegeek.github.io/blog/projects/vapeserver/

### TL;DR

A discarded vape’s 24 MHz Cortex-M0+, 24 KiB flash, and 3 KiB RAM became a functioning HTTP server. The author connected it through debugger semihosting, a virtual serial line, SLIP, and the compact uIP stack, then fixed ARM alignment assumptions and buffered byte-at-a-time I/O. Performance improved from 1.5-second lossy pings and 20-second pages to 20-millisecond pings and 160-millisecond loads. HN celebrated the salvage while condemning rechargeable batteries, USB-C, and capable microcontrollers being sold as disposable waste.

### Comment pulse

- Buffering transformed performance → spending scarce RAM reduced semihosting overhead while leaving room for application logic.
- Cheap discarded electronics invite reuse → commenters suggested LTE dongles, batteries, and educational platforms as similarly capable salvage targets.
- The achievement exposes a policy failure → reusable components are intentionally packaged into products designed for one short lifecycle.

### LLM perspective

- View: The server is a playful systems lesson and an indictment of disposable-device economics.
- Impact: Tinkerers gain a reproducible embedded-networking example; regulators face visible evidence of avoidable electronic waste.
- Watch next: Safe battery recovery, standardized reuse paths, device regulation, and projects built from the remaining peripherals.
