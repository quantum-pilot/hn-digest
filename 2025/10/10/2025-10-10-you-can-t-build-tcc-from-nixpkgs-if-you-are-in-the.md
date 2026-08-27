# You can't build tcc from Nixpkgs if you are in the UK

- Score: 138 | [HN](https://news.ycombinator.com/item?id=45540011) | Link: https://github.com/NixOS/nixpkgs/issues/444342

### TL;DR

UK Nix builds of TinyCC, docutils, cdimgtools, and several other packages failed because their `fetchFromRepoOrCz` source downloads received repo.or.cz's Online Safety Act geo-block page instead of tarballs. Nix then tried to unpack HTML as gzip. Hydra did not reproduce the failure because its builders were outside the UK, and binary-cache users were mostly unaffected. Maintainers discussed VPNs, archive mirrors, and alternate upstreams; the reporter prepared a docutils change to fetch from PyPI. HN debate centered on defensive geo-blocking by volunteer services.

### Comment pulse

- The headline is indirect → repo.or.cz's UK block breaks source-dependent builds; Nix itself is not region-locking TinyCC.
- Binary caches mask geographic fragility → ordinary users may succeed until modifying packages or missing cached substitutes.
- Alternative sources are package-specific → PyPI works for docutils, while bootstrap constraints and mirror reliability complicate general fixes.

### LLM perspective

- View: Reproducible recipes still depend on source availability, making jurisdiction and hosting policy part of the supply chain.
- Impact: UK builders face silent content substitution unless fetchers verify responses before archive extraction.
- Watch next: Replace blocked origins, improve error detection, add mirrors, test regional builds, and track Online Safety Act-driven withdrawals.
