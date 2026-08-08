# LinkedIn scans for 6,278 extensions and encrypts the results into every request

- Score: 359 | [HN](https://news.ycombinator.com/item?id=47967262) | Link: https://404privacy.com/blog/linkedin-is-scanning-your-browser-extensions-this-is-how-they-use-the-data/

### TL;DR

An analysis says LinkedIn’s Chrome JavaScript probes 6,278 extension IDs by fetching each extension’s known web-accessible file and recording which requests succeed. A second system searches page modifications for extension URLs. Detected IDs reportedly enter RSA-encrypted telemetry sent to LinkedIn and a fingerprint header attached to later session requests, alongside 48 device signals. The author argues this undisclosed inventory can expose job-search, accessibility, political, religious, security, and workplace-tool use to a service tied to verified identities. A Bavarian cybercrime investigation is reportedly open.

### Comment pulse

- Some called extension detection standard anti-scraping fingerprinting — counterpoint: critics objected to its scale, secrecy, identity linkage, and enforcement consequences.
- Readers questioned whether the transmitted header truly contains reversibly encrypted results because the article shows no captured example.
- Chrome does not directly list extensions; exposed package resources create an installation oracle that Brave reportedly blocks.

### LLM perspective

- Independent reproduction should publish request samples, decryption evidence, timing, and account-state differences.
- Browsers could restrict extension-resource requests to extension-originated code or require explicit permission.
- LinkedIn should disclose purpose, retention, sharing, user decisions, and appeal mechanisms for detected software.
