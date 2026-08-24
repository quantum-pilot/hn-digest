# I cracked a $200 software protection with xcopy

- Score: 78 | [HN](https://news.ycombinator.com/item?id=46170060) | Link: https://www.ud2.rip/blog/enigma-protector/

### TL;DR

A researcher spent hours inspecting Enigma Protector’s packed installer, RSA licensing, hardware binding, and anti-debugging before checking the installed Bass Bully VST3 payload. The plugin contained no Enigma runtime or license checks, so copying its VST and ROM files produced a working package without breaking Enigma’s cryptography. The lesson is to threat-model post-installation assets and inspect the simplest attack surface first. Commenters disputed the framing, saying only a musician’s plugin configuration was bypassed and runtime DRM might deliberately be avoided for live-performance reliability.

### Comment pulse

- The protection product itself was not cracked → its controls worked on the installer; the unprotected payload made them irrelevant after installation.
- Runtime checks could strengthen licensing → payload enforcement closes the copy gap — counterpoint: performers may prefer reliability over stronger DRM during shows.
- Tone drew criticism → commenters saw needless ridicule of a solo musician who may have exported the plugin through a third-party tool.

### LLM perspective

- View: Security spending fails when deployment omits the protected asset, but stronger DRM remains a product tradeoff.
- Impact: Vendors must align licensing controls with piracy risk, support burden, performance, and legitimate-user reliability.
- Watch next: Payload-level checks, reproducible runtime-overhead tests, and clearer vendor documentation of protection scope.
