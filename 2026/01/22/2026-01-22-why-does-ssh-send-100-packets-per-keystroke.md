# Why does SSH send 100 packets per keystroke?

- Score: 226 | [HN](https://news.ycombinator.com/item?id=46723990) | Link: https://eieio.games/blog/ssh-sends-100-packets-per-keystroke/

### TL;DR

A high-scale terminal game revealed that stock SSH emitted roughly 90 small data packets per second after a keystroke. OpenSSH's 2023 timing defense sends randomized ping “chaff” to obscure typing rhythms when servers advertise a ping extension. Disabling that advertisement in a fork of Go's crypto library cut CPU from 29.90% to 11.64%, bandwidth from about 6.5 to 3 Mbit/s, and crypto time from 1.6 to 0.11 seconds. HN favored an upstream opt-out but warned broader switches could erode security.

### Comment pulse

- Library design → readers want a server capability switch for atypical TTY applications, while preserving privacy-first defaults.
- Alternatives → test-only null ciphers aid packet inspection; telnet or netcat may suit public games needing neither confidentiality nor standard SSH behavior.
- LLM role → some saw little beyond rubber-ducking, while others valued rapid packet analysis and momentum despite confident wrong turns.

### LLM perspective

- View: A sensible transport defense became pathological because application semantics differed from the terminal session SSH assumed.
- Impact: Interactive services inheriting general-purpose secure defaults may pay disproportionate CPU, syscall, crypto, and bandwidth costs.
- Watch next: Upstream extension controls, server-side negotiation design, benchmarks at 2,000 connections, and safe maintenance of the fork.
