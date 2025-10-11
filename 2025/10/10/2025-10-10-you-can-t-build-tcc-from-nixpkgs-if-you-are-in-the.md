# You can't build tcc from Nixpkgs if you are in the UK

- Score: 138 | [HN](https://news.ycombinator.com/item?id=45540011) | Link: https://github.com/NixOS/nixpkgs/issues/444342

- TL;DR
  - A Nixpkgs fetcher (fetchFromRepoOrCz) that pulls tarballs from repo.or.cz breaks in the UK because the host geo‑blocks UK IPs to avoid the Online Safety Act. Packages like tinycc, cdimgtools, syslinux, glpng, and docutils fail with “not in gzip format” as the block page is downloaded instead. docutils is being switched to PyPI; fetchgit may now be viable since LLVM docs aren’t in Darwin bootstrap. Most users see binaries from cache.nixos.org, but HN debated the law’s chilling effect, VPN workarounds, and decentralized mirrors.

- Comment pulse
  - OSA chills small hosts → repo.or.cz fears vague compliance and liability; UK block is safest — counterpoint: use cache/VPN.
  - Breakage scope → only packages using fetchFromRepoOrCz fail; Hydra unaffected; binaries often substitute, but local/modified builds in UK break.
  - Resolutions → switch sources (PyPI for docutils), add mirrors, or use fetchgit now LLVM docs aren’t in bootstrap; consider decentralized/p2p distribution.

- LLM perspective
  - View: Single-source fetchers fail under jurisdictional blocks; bake multiple mirrors and failure detection into fetchers.
  - Impact: UK-based builders, on-prem CI, and bootstrap paths without curl are fragile; maintainers carry mirror curation overhead.
  - Watch next: Track PRs switching sources, repo.or.cz policy changes, and Nix tooling for prioritized mirror lists with hash parity tests.
