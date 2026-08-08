# How OpenAI delivers low-latency voice AI at scale

- Score: 221 | [HN](https://news.ycombinator.com/item?id=48013919) | Link: https://openai.com/index/delivering-low-latency-voice-ai-at-scale/

### TL;DR

OpenAI reworked its WebRTC stack for point-to-point voice sessions by separating a stateless UDP relay from stateful transceivers. Clients still use standard WebRTC through a small set of public ports; ICE username fragments encode routing hints so the relay can steer the first packet to the transceiver owning ICE, DTLS, SRTP, and session state. Geo-steered signaling and distributed ingress shorten the network path, while a narrow Go implementation avoids kernel bypass. Commenters praised the Pion-based design but stressed that transport latency cannot fix premature turn-taking or older voice-model capabilities.

### Comment pulse

- Users with natural pauses found responses intrusive — counterpoint: that is endpointing behavior, while low transport delay enables faster interruption.
- Some engineers questioned optimizing WebRTC before model speed; others valued a reusable, globally scalable media foundation.
- The cited 900 million is potential ChatGPT reach, not disclosed concurrent voice usage, limiting capacity interpretation.

### LLM perspective

- Measure end-to-end latency by transport, VAD, model inference, synthesis, and playback; optimize the dominant tail.
- Offer configurable pause tolerance or push-to-talk without sacrificing rapid barge-in.
- Publish p50/p95 setup and media latency, packet loss, relay overhead, failover behavior, and regional load.
