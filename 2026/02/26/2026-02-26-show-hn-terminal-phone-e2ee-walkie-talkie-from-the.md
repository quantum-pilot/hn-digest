# Show HN: Terminal Phone – E2EE Walkie Talkie from the Command Line

- Score: 281 | [HN](https://news.ycombinator.com/item?id=47164270) | Link: https://gitlab.com/here_forawhile/terminalphone

### TL;DR

TerminalPhone is a single Bash script for Linux and Android Termux that sends push-to-talk voice clips and text through Tor onion services without accounts, phone numbers, port forwarding, or central servers. It compresses audio with Opus, applies shared-secret encryption, and can authenticate protocol messages with HMAC nonces. Typical 10-second clips stay under 20 KB. Its documented limits include out-of-band secret exchange, no forward secrecy, and endpoint compromise. The author reports roughly two-to-three-second latency and says full-duplex audio performed poorly, making walkie-talkie pacing intentional.

### Comment pulse

- Readers liked onion addresses as both stable identity and NAT traversal, eliminating separate rendezvous infrastructure.
- Tor relay bandwidth and network blocking remain costs — counterpoint: more ordinary onion applications could add useful cover traffic.
- Twenty-one ciphers drew criticism; the author conceded the extra OpenSSL layer is redundant but prefers pre-network encryption.

### LLM perspective

- **View:** The project optimizes for deployability and anonymity, not cryptographic minimalism or live conversation.
- **Impact:** Trusted pairs gain a low-bandwidth voice channel if they can exchange secrets securely and tolerate delay.
- **Watch next:** Authenticated-encryption defaults, forward secrecy, interoperability testing, and latency across censored or congested networks.
