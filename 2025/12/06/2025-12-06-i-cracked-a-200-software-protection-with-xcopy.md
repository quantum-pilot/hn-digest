# I cracked a $200 software protection with xcopy

- Score: 78 | [HN](https://news.ycombinator.com/item?id=46170060) | Link: https://www.ud2.rip/blog/enigma-protector/

### TL;DR
A reverse engineer bought a music plugin protected with Enigma Protector, a $200 commercial DRM wrapper boasting hardware-locked licenses, crypto signatures, and anti-debug tricks. Analysis showed the vendor only protected the installer; after installation, the plugin files were completely unprotected and ran fine when simply copied to another machine. The post argues this illustrates bad threat modeling and “security theater,” while commenters debate tone, indie‑dev shaming, and whether light DRM is acceptable to avoid harming live performances.

---

### Comment pulse
- DRM is to keep honest users honest; heavy runtime checks risk reliability, esp. for live music tools — counterpoint: researcher frames it as security failure.  
- Several readers see the post as an ego trip, mocking a small indie musician rather than the commercial protection vendor.  
- Some argue the protection product worked as documented; the real lesson is misconfigured deployment and weak threat modeling, not broken cryptography.  

---

### LLM perspective
- View: Security tooling vendors should surface common misconfigurations and defaults that leave installed payloads unprotected to reduce false sense of safety.  
- Impact: Audio and creative software devs need lightweight integrity checks plus clear UX, instead of expensive wrappers they don’t configure correctly.  
- Watch next: Benchmark how DRM schemes affect latency, crash rates, and support load in live tools; publish templates for minimal runtime enforcement.
