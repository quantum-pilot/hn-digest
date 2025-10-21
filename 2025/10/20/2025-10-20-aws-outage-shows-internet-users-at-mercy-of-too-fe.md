# AWS outage shows internet users 'at mercy' of too few providers, experts say

- Score: 235 | [HN](https://news.ycombinator.com/item?id=45646649) | Link: https://www.theguardian.com/technology/2025/oct/20/amazon-web-services-aws-outage-hits-dozens-websites-apps

- TL;DR
    - An AWS us-east-1 incident triggered elevated API errors across core services (incl. DynamoDB), disrupting 2,000+ companies and major apps worldwide; Amazon rate‑limited traffic while recovering. Downdetector logged 8.1m user reports, spanning banking, tax, gaming and messaging. The Guardian argues this concentration in a few hyperscalers warrants diversification and oversight. HN focuses on trade‑offs and implementation reality: operator perspectives, platform lock‑in, and national sovereignty concerns shape what “diversification” can practically mean.

- Comment pulse
    - Multi-cloud is costly; most businesses tolerate ~16 hours/year downtime. — counterpoint: concentration creates systemic risk; multiple providers mean not everyone fails simultaneously.
    - Quoted “experts” lack ops backgrounds; practitioners want a blameless postmortem and details on us-east-1/DynamoDB dependency.
    - Diversification exists at IaaS, but PaaS lock-in (DynamoDB, Redshift) hinders switching; sovereign-tech advocates warn against national reliance on foreign hyperscalers.

- LLM perspective
    - View: Prioritize multi‑region, provider‑agnostic architectures; treat managed PaaS as dependencies with explicit failure modes and graceful degradation.
    - Impact: Expect regulators to expand “critical third party” oversight; enterprises revisit RTO/RPO, regional isolation, and us‑east‑1 reliance.
    - Watch next: AWS root‑cause and blast‑radius report; customer chaos drills; measurable multi‑region failovers; guidance on PaaS portability patterns.
