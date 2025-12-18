# A Safer Container Ecosystem with Docker: Free Docker Hardened Images

- Score: 268 | [HN](https://news.ycombinator.com/item?id=46302337) | Link: https://www.docker.com/blog/docker-hardened-images-for-every-developer/

## TL;DR

Docker is making its Docker Hardened Images (DHI) catalog free and open source (Apache 2.0), aiming to make “secure-by-default” base images the norm. These Alpine/Debian-based, mostly distroless images ship with SBOMs, SLSA Level 3 provenance, VEX, signatures, and transparent CVE reporting, plus hardened Helm charts and MCP servers. Revenue comes from an Enterprise tier with strict CVE SLAs, FIPS/STIG variants, customization, and Extended Lifecycle Support, while HN debates market saturation, long‑term pricing trust, and onboarding friction.

## Comment pulse

- Docker employee: free hardened images are funded by paid SLAs, regulated variants, and custom builds; emphasis on SBOMs, attestations, and VEX for real transparency.  

- Some see a crowded hardened-image market (Chainguard, Iron Bank, others); Docker giving away the core offering may erode competitors’ paid value—counterpoint: easier adoption could grow overall demand.  

- Skeptics cite Docker’s history of “free-then-paid” shifts, login/PAT and CI/CD friction, and fear another Bitnami-style rug-pull before betting infrastructure on DHI.  

## LLM perspective

- View: Technically, Apache-licensed, attestable base images with strong provenance meaningfully reduce supply-chain risk for mainstream teams.  

- Impact: Could standardize “good enough” container security, pressuring niche hardened-image vendors to differentiate beyond low CVE counts.  

- Watch next: Strength of public repos and tooling, migration automation quality, and whether Docker formalizes non-paywall guarantees for the free tier.
