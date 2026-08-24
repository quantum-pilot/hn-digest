# Home Depot GitHub token exposed for a year, granted access to internal systems

- Score: 260 | [HN](https://news.ycombinator.com/item?id=46247000) | Link: https://techcrunch.com/2025/12/12/home-depot-exposed-access-to-internal-systems-for-a-year-says-researcher/

### TL;DR

Security researcher Ben Zimmermann told TechCrunch he found a Home Depot employee’s GitHub token online in early November after exposure dating to early 2024. He said it could modify hundreds of private repositories and reach cloud infrastructure, fulfillment, inventory, and development pipelines. Home Depot did not answer his repeated private reports and had no published disclosure channel. After TechCrunch contacted the retailer on December 5, the token disappeared and access was revoked. Home Depot did not say whether logs could reveal misuse.

### Comment pulse

- Readers saw the missing disclosure channel and delay as governance failures — counterpoint: legal caution may explain public silence, not the technical response.
- Experiences with automatic key revocation varied; GitHub and Anthropic caught exposed credentials quickly, while other providers were harder to manage.
- Advice centered on minimizing secret scope, restricting origin where supported, and using SOPS or platform secret stores.

### LLM perspective

- View: This was a high-impact credential exposure, not proof of malicious exploitation.
- Impact: Write access to repositories and pipelines makes supply-chain compromise plausible.
- Watch next: Home Depot’s audit findings, credential-scanning controls, and creation of a disclosure channel.
