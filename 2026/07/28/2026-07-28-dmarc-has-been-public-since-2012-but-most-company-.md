# DMARC has been public since 2012 but most company domains still don't enforce it

- Score: 173 | [HN](https://news.ycombinator.com/item?id=49081783) | Link: https://ciphercue.com/blog/dmarc-enforcement-gap-rua-fragmentation-2026

### TL;DR

CipherCue scanned 67,336 tracked domains and found 45.1% lacked DMARC, while another 23.3% published monitoring-only p=none; just 15.2% requested quarantine and 16.3% rejection. The sample is not a worldwide census, but suggests enforcement—not record publication—is the larger gap. The article blames difficult aggregate reports and unknown legitimate senders that administrators must inventory before blocking failures. HN debated utility: DMARC prevents visible-domain impersonation, not trustworthy-sender judgment or all phishing, and strict receivers risk losing legitimate mail because forwarding and major senders remain misconfigured.

### Comment pulse

- Authentication scope divides readers → critics find little spam signal — counterpoint: DMARC verifies visible-domain authorization, enabling reputation and raising impersonation costs.
- Receivers hesitate to enforce → SPF/DKIM failures from large senders and forwarding breakage create user complaints when legitimate messages are rejected.
- Unused domains offer an easy win → publish rejecting SPF and DMARC policies, cover subdomains, and use a null MX when receiving nothing.

### LLM perspective

- View: DMARC is identity plumbing, not trust scoring; value emerges when authentication feeds reputation, abuse response, and layered filtering.
- Impact: Small organizations bear disproportionate discovery costs because SaaS platforms, forgotten senders, and delegated DNS obscure domain usage.
- Watch next: Measure migration from p=none, false-positive rates, forwarding behavior, sender-inventory time, and adoption after the 2026 standards-track update.
