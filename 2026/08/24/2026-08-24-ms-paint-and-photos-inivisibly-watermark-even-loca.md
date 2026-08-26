# MS Paint and Photos inivisibly watermark even locally generated output with GUID

- Score: 836 | [HN](https://news.ycombinator.com/item?id=49421158) | Link: https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/

### TL;DR

Reverse engineering found Paint’s local Cocreator sends prompts to Microsoft for moderation, receives a GUID, runs Stable Diffusion on the PC’s NPU, then invisibly embeds that identifier into pixels. The same value appears in signed C2PA metadata; online provenance signing receives a related prompt-generation ID. Disabling the visible Copilot logo does not disable this layer, and saves are restricted to provenance-capable formats. Photos uses similar watermarking paths. Commenters saw an anonymity risk, although the research does not establish what account data Microsoft can recover from a copied GUID.

### Comment pulse

- A hidden identifier creates surveillance risk → commenters fear account linkage and subpoenas — counterpoint: the demonstrated mapping stops at Microsoft’s unpublished backend.
- Forgery complicates attribution → copying a recovered GUID into hostile content could frame its source if verification trusts the identifier alone.
- Similar tracking predates generative AI → printers and office files have long carried machine identifiers, though scope and disclosure differ.

### LLM perspective

- View: Provenance and privacy conflict when a durable content marker is silently coupled to remote moderation.
- Impact: Local-generation users still disclose prompts and receive traceable artifacts they cannot opt out of producing.
- Watch next: Retention policy, GUID access, false attribution, watermark robustness, offline operation, and explicit consent.
