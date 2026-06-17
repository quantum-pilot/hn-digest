# TIL: You can make HTTP requests without curl using Bash /dev/TCP

- Score: 231 | [HN](https://news.ycombinator.com/item?id=48558018) | Link: https://mareksuppa.com/til/bash-dev-tcp-http-without-curl/

### TL;DR
Bash has a special `/dev/tcp/host/port` redirection that opens a TCP socket, letting you hand‑craft simple HTTP/1.1 requests from ultra‑minimal containers with no `curl`, `wget`, or `nc`. It’s useful for quick connectivity checks (e.g., `/health`) by writing a request with `printf` and reading the response with `cat`, but lacks TLS, retries, parsing, or HTTP/2/3 support. HN commenters reminisce about telnet‑level protocol hacking, emphasize this is “just TCP, not HTTP,” and debate minimal images vs always including `curl`.

---

### Comment pulse
- Manual protocol tinkering is educational → telnetting to ports 80/25/110 taught people that HTTP/SMTP/POP3 are just text over sockets—counterpoint: newer TLS/binary protocols hinder this style.  
- Precision matters → bash only opens TCP; you’re implementing HTTP yourself. `nc` or similar is wiser when available; full bash webservers hide C helpers underneath.  
- Minimal vs practical images → some want stripped containers and tricks like `/dev/tcp`; others argue `curl` is small, ubiquitous, and worth including even in production.

---

### LLM perspective
- View: Treat `/dev/tcp` as a last‑resort debugging tool, not a substitute for real HTTP clients or protocol libraries.  
- Impact: Helps ops/infra engineers verify connectivity inside locked‑down containers without modifying images or installing packages.  
- Watch next: Container hardening may further restrict shells; track base images, `curl` defaults, and whether tools like `nc` remain standard.
