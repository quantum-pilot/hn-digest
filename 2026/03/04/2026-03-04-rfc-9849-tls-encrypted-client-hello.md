# RFC 9849. TLS Encrypted Client Hello

- Score: 270 | [HN](https://news.ycombinator.com/item?id=47244291) | Link: https://www.rfc-editor.org/rfc/rfc9849.html

### TL;DR

RFC 9849 standardizes Encrypted ClientHello for TLS 1.3 and DTLS 1.3, encrypting the true server name and ALPN under a server-advertised HPKE public key. Clients send a benign outer hello plus encrypted inner hello; servers either accept it or securely supply retry configurations. Privacy depends on many sites sharing indistinguishable configurations and behavior, and still requires encrypted DNS because IP addresses expose the provider. The design includes padding, GREASE cover traffic, downgrade resistance, split-mode frontends, and recovery from deployment mismatches, while warning about tracking, timing, and middlebox impacts.

### Comment pulse

- Early adopters reported working implementations in Caddy, Nginx, Chrome, Android networking, and experimental Rustls work.
- A site’s own endpoint can still decrypt and fingerprint clients; ECH blocks unrelated observers, not the serving operator.
- Commenters welcomed bypassing SNI censorship; counterpoint: the same opacity complicates parental filtering and exposes tension with legal controls.

### LLM perspective

- **View:** ECH protects destination detail, not destination infrastructure; its privacy unit is the provider’s anonymity set.
- **Impact:** Broad, uniform deployment can frustrate passive filtering without changing application encryption or backend authentication.
- **Watch next:** Encrypted-DNS adoption, configuration sharing, key rotation, retry rates, middlebox failures, and policy-driven attempts to block real ECH.
