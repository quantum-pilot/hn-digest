# Hijacking the PS5's RTMP stream

- Score: 285 | [HN](https://news.ycombinator.com/item?id=49879702) | Link: https://yashgarg.dev/posts/hijacking-ps5-rtmp-stream/

### TL;DR

Yash Garg redirects a PS5’s Twitch broadcast to a Mac for Discord screen sharing without a capture card. Twitch first uses a TLS-protected discovery endpoint, but the console’s selected ingest host accepts plain RTMP. A local dnsmasq returns the Mac’s address for Twitch ingest domains; nginx-rtmp receives the resulting 1080p60 H.264/AAC stream, and mpv displays it with reported sub-second delay. A menu-bar app packages the components. Commenters clarified the Twitch-versus-YouTube path and questioned why console broadcast traffic remains unencrypted.

### Comment pulse

- DNS control enables local capture → the PS5 resolves the final Twitch ingest hostname dynamically and sends plain RTMP to the substituted address.
- YouTube redirection was only a proof → its API check stopped the diverted broadcast after roughly 60 seconds.
- Unencrypted ingest creates privacy exposure → intermediaries could observe broadcast traffic—counterpoint: commenters considered client exploitation through simple RTMP less likely.

### LLM perspective

- View: This is protocol redirection around a platform limitation, not a PS5 software exploit.
- Impact: Users gain inexpensive local capture but depend on Sony and Twitch preserving current hostname and transport behavior.
- Watch next: Endpoint changes, enforced RTMPS, stream-key exposure, broader network testing, and maintained packaging of the workaround.
