# Flock Hardcoded the Password for America's Surveillance Infrastructure 53 Times

- Score: 110 | [HN](https://news.ycombinator.com/item?id=46555807) | Link: https://nexanet.ai/blog/53-times-flocksafety-hardcoded-the-password-for-americas-surveillance-infrastructure

## TL;DR

A security researcher found Flock Safety had embedded a single default ArcGIS API key in 53 public JavaScript bundles, with no IP/referrer restrictions, granting organization‑wide access to 50 private mapping items. Because FlockOS centralizes license‑plate hits, patrol cars, drones, body cams, 911 incidents, registrant PII, and more for ~12k deployments, this effectively exposed a national‑scale surveillance map. A second, unpatched token‑minting flaw suggests systemic credential mismanagement. HN discussion centers on vendor incompetence, local resistance to Flock, and some skepticism about the technical proof.

## Comment pulse

- Flock is a profit‑driven surveillance vendor with amateur security → hardcoded org‑wide key, boastful CEO, DOJ‑grant funding, YC backing encourage growth over safety.  

- Cities can push back → examples in Washington and Oregon where public pressure led to non‑renewals or votes against Flock deployments.  

- Governments buy complex tech without real technical review → CIOs/auditors sidelined in ShotSpotter debates; electeds swayed by sales claims — counterpoint: one commenter doubts the key truly exposed data vs billing access.

## LLM perspective

- View: Centralized “single map” architectures turn any leaked org‑wide key into a full‑spectrum breach of physical operations.  

- Impact: Law‑enforcement tech vendors will face stronger demands for independent pen‑tests, secret‑scanning, and least‑privilege cloud configurations.  

- Watch next: FTC/Congress response to Wyden’s calls, disclosure of Flock’s audits, and similar ArcGIS misconfigurations at other vendors.
