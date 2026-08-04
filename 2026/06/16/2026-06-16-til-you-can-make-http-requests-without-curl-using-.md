# TIL: You can make HTTP requests without curl using Bash /dev/TCP

- Score: 231 | [HN](https://news.ycombinator.com/item?id=48558018) | Link: https://mareksuppa.com/til/bash-dev-tcp-http-without-curl/

### TL;DR

Bash can open a raw TCP socket through its special `/dev/tcp/host/port` redirection, letting a minimal container send a hand-written HTTP/1.1 request when curl, wget, and netcat are absent. The technique writes through a file descriptor and reads the response directly; `Host` and `Connection: close` prevent common failures. It is only a diagnostic shortcut: no TLS, redirect handling, chunk decoding, compression, retries, or portability beyond suitably compiled Bash. HN stressed that Bash supplies transport, not HTTP, while celebrating manual text protocols as useful demystification.

### Comment pulse

- Manual requests are educational → interacting with plaintext protocols exposes their structure and removes perceived magic, though TLS and binary protocols reduce accessibility.

- Production use is unsafe → incomplete parsing breaks on ordinary HTTP features — counterpoint: a narrow health check need not recreate a general client.

- Minimal images divide operators → some value fewer packages and ad hoc probes; others consider curl essential for production diagnosis.

### LLM perspective

- **View:** This is best understood as a socket probe with an HTTP-shaped payload, not a replacement client.

- **Impact:** Operators can test internal reachability without rebuilding containers, but scripts gain protocol and shell-specific failure modes.

- **Watch next:** Confirm Bash net-redirection support, enforce timeouts, test chunked responses, and install proper tooling for recurring checks.
