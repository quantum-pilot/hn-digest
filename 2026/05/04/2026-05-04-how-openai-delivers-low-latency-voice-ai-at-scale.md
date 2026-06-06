# How OpenAI delivers low-latency voice AI at scale

- Score: 221 | [HN](https://news.ycombinator.com/item?id=48013919) | Link: https://openai.com/index/delivering-low-latency-voice-ai-at-scale/

## TL;DR
OpenAI explains how it serves real-time voice AI (ChatGPT voice, Realtime API) to hundreds of millions of users over WebRTC while running everything on Kubernetes. Traditional “one UDP port per session” WebRTC doesn’t scale well in cloud clusters (port exhaustion, security, autoscaling, and state stickiness). They instead use a split design: a stateless UDP relay with a tiny public port footprint plus a stateful “transceiver” that owns WebRTC state. Routing is encoded into ICE ufrag, enabling first-packet steering, global relays near users, and consistently low latency without changing client-side WebRTC.

---

## Comment pulse
- WebRTC nerds happy: OpenAI uses Pion and standard WebRTC; article praised as a great real-world scaling case and learning resource.  
- UX complaints: ultra-fast turn-taking plus aggressive VAD makes GPT interrupt natural pauses; users want smarter pause handling or configurable delay—counterpoint: this is above-transport, not network latency.  
- Capability gap: realtime voice stuck on older GPT‑4o; some prefer Grok or Gemini Flash Live 3.1 for smarter, tool-using conversations despite OpenAI’s superior voice stack.

---

## LLM perspective
- View: Smart, minimal WebRTC changes let infra scale without fragmenting client behavior or depending on exotic kernel networking.  
- Impact: Any large voice/developer platform on Kubernetes can copy the relay+transceiver pattern to tame UDP and keep infra simple.  
- Watch next: Better VAD/turn-taking models, user-configurable interaction timing, and deployment of frontier models into this low-latency stack.
