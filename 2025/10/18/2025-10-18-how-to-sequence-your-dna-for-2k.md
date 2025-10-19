# How to sequence your DNA for <$2k

- Score: 96 | [HN](https://news.ycombinator.com/item?id=45629970) | Link: https://maxlangenkamp.substack.com/p/how-to-sequence-your-dna-for-2k

- TL;DR
    - A small team sequenced a human genome at home for ~$1.1k using an Oxford Nanopore MinION, improvised heating, and basic kits. They produced ~1 Gb (~13% coverage) with ~25% contamination and a partly dead flow cell (623/2048 pores), yielding no reliable SNP calls. HN notes Nanopore’s higher error rate and Illumina’s dominance for clinical-grade data; long reads shine for structural variants. Outsourcing 30× WGS to Nebula/Dante is cheaper but raises privacy/trust concerns. The cited $1k MinION kit also appears discontinued/pricier now.

- Comment pulse
    - SBS still dominates clinical sequencing → lower error rates and cost; 30× WGS via Illumina under ~$1000 — counterpoint: ONT improving; strong for structural variants.
    - Outsourcing WGS is cheaper → Nebula/Dante advertise 30× for $300; often overseas. Users report data sharing, delays, and ownership risks.
    - MinION flow cell issues vary → typical starts exceed ~800 active pores; poor counts suggest mishandling; vendors may replace.

- LLM perspective
    - View: DIY WGS is feasible but decision-grade results need proper library prep, clean samples, higher depth, and reliable flow cells.
    - Impact: Lower entry costs shift genomics education and small-lab prototyping; clinical and ancestry insights remain with regulated providers.
    - Watch next: ONT R10.4.1/Q20+ duplex gains, cheaper MinION bundles, transparent DTC privacy terms, and standard outputs (BAM/VCF) for consumer downloads.
