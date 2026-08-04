# The Fedora 45 Sausage Factory

- Score: 132 | [HN](https://news.ycombinator.com/item?id=49046525) | Link: https://supakeen.com/weblog/the-fedora-45-sausage-factory/

### TL;DR

A Fedora 45 walkthrough traces a package from a dist-git commit through Koji’s isolated RPM builds, Bodhi’s testing gates, and Pungi’s frozen package snapshot into repositories, installer media, cloud/container images, and OSTree deployments. Lorax, Kiwi, Image Builder, rpm-ostree, productmd, and openQA each handle specialized stages, while Fedora’s Changes process governs major pipeline modifications. Readers praise the end-to-end map as practical troubleshooting documentation and ask how to contribute; one thread cautions that clean buildrooms can still conceal undeclared dependencies pulled in transitively.

### Comment pulse

- Operational traceability matters → one user can now locate the image-building stage behind a filesystem-permission regression that previously resisted diagnosis.
- Contribution has approachable entry points → commenters recommend testing Bodhi updates, validating blocker-bug fixes during freezes, and working Fedora infrastructure backlog tickets.
- Build isolation has limits → fresh environments prevent ambient drift — counterpoint: transitive dependencies can hide missing BuildRequires until dependency graphs change.

### LLM perspective

- View: The pipeline’s complexity is manageable because explicit snapshots, metadata, stage barriers, and ownership boundaries preserve provenance.
- Impact: Release engineers can change individual builders while downstream consumers retain stable metadata and auditable package membership.
- Watch next: Track Fedora 45’s boot.iso proposal, pipeline documentation updates, reproducibility checks, and whether hidden BuildRequires are detected automatically.
