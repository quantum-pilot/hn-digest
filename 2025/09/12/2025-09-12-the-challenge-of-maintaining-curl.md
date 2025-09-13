# The challenge of maintaining curl

- Score: 183 | [HN](https://news.ycombinator.com/item?id=45217858) | Link: https://lwn.net/Articles/1034966/

- TL;DR
    - Daniel Stenberg’s OSS Summit keynote highlights curl’s paradox: billions of devices depend on it, yet it’s maintained mostly by one person. Beyond coding, he handles security, support, infra—and corporate demands, compliance questionnaires, CRA queries—often without payment. AI has worsened noise: fabricated vulns and scraper traffic eat time and bandwidth. Despite occasional grants and thanks, sustainable backing is rare. HN notes real donation blockers: compliance, invoicing, and tax rules; suggests merchants‑of‑record and warns that licensing “ransom” tactics risk forks.

- Comment pulse
    - Donating is hard → compliance, AML/KYC, vendor assessments, invoicing/tax status block simple support; merchants‑of‑record can reduce friction — counterpoint: still burdensome for big‑corp procurement.
    - AI-fueled vuln spam → LLM-generated reports seek CVE clout/bounties, wasting maintainer time; some include fabricated APIs; fear maintainers might accept LLM patches.
    - Funding tactics debate → AGPL-threat GoFundMe proposed; critics say forks would neuter leverage; note: Germany’s Sovereign Tech Agency gave curl ~€200k.

- LLM perspective
    - View: Sustainability hinges on predictable, low-friction funding plus noise-tolerant processes; single-maintainer risk is systemic across critical OSS.
    - Impact: Vendors relying on curl should budget sponsorship/support contracts; adopt mirrors/CDNs to offload bandwidth; standardize procurement for OSS vendors.
    - Watch next: CRA guidance, OpenSSF frameworks, merchant‑of‑record offerings, and curated vuln-intake portals; measurable: sponsor counts, revenue mix, bot traffic vs. source downloads.
