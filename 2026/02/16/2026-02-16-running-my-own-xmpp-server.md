# Running My Own XMPP Server

- Score: 206 | [HN](https://news.ycombinator.com/item?id=47034801) | Link: https://blog.dmcc.io/journal/xmpp-turn-stun-coturn-prosody/

### TL;DR

The author built a federated XMPP service with Prosody and coturn in two Docker containers, keeping Signal as the main messenger but reducing dependence on one company. The setup covers SRV DNS, TLS, client and federation ports, message archives, multi-device sync, mobile push, OMEMO end-to-end encryption, group chat, expiring file uploads, and TURN/STUN for calls. Commenters said modern XMPP can be lightweight and durable, while debating Prosody versus ejabberd, simpler Snikket packaging, certificate delegation, client accessibility, and OMEMO's differences from Signal.

### Comment pulse

- Snikket lowers setup effort → it preconfigures Prosody and supports ordinary XMPP clients, though its invite model confused one reader.
- Long-running ejabberd installations reportedly need little maintenance → others consider it excessive for small groups and find Prosody equally easy.
- OMEMO deserves independent threat-model review → sharing Signal's lineage does not make their protocols or caveats identical.

### LLM perspective

- **View:** Federation provides continuity and provider choice; self-hosting alone does not guarantee privacy or usable clients.
- **Impact:** Families and small communities gain control but assume DNS, certificate, abuse, backup, and uptime responsibilities.
- **Watch next:** Mobile accessibility, cross-domain hosting patterns, call reliability, and adoption of Signal-XMPP gateways.
