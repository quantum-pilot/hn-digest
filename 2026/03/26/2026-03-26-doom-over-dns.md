# DOOM Over DNS

- Score: 188 | [HN](https://news.ycombinator.com/item?id=47490705) | Link: https://github.com/resumex/doom-over-dns

### TL;DR

This proof of concept compresses shareware DOOM and .NET engine libraries, splits them across about 1,964 Cloudflare DNS TXT records, retrieves them with PowerShell 7, and loads the assemblies and WAD directly into memory without writing the WAD to disk. A single Pro zone fits the data; free zones hold 185 chunks apiece and require striping across domains. The project removes audio and uses Win32 windowing. HN enjoys the stunt but corrects its framing: DNS acts as cached storage and transport, not the environment executing the game.

### Comment pulse

- This is playful, not practical storage — counterpoint: normalizing honor-system abuse could encourage providers to restrict shared infrastructure.
- A precise description is loading assets from TXT records → all computation still occurs in PowerShell and .NET on the client.
- DNS tunnels and filesystems predate the demo → novelty comes from packaging the mechanism into runnable shareware DOOM.

### LLM perspective

- **View:** The stunt demonstrates DNS’s general data channel and caching behavior, not distributed computation.
- **Impact:** It offers educational value but little advantage over legitimate static hosting.
- **Watch next:** Resolver TXT limits, cache behavior, provider enforcement, integrity checks, and multi-zone resilience.
