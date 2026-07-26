# The Fedora 45 Sausage Factory

- Score: 132 | [HN](https://news.ycombinator.com/item?id=49046525) | Link: https://supakeen.com/weblog/the-fedora-45-sausage-factory/

- TL;DR  
  Fedora 45’s “sausage factory” shows how a git commit becomes installable artifacts. Packagers push to dist-git, Koji builds RPMs in clean chroots, and Bodhi gates updates with testing, karma, and CI. Pungi snapshots tagged builds, then orchestrates lorax, Kiwi, Image Builder, and rpm-ostree to produce ISOs, cloud/WSL images, containers, and atomic desktops, all described via productmd metadata and validated by openQA. Major tooling or policy changes flow through a formal FESCo-governed Changes process.

- LLM perspective  
  - View: Fedora’s pipeline is a modular graph of specialized tools glued by tags, metadata, and config.  
  - Impact: Distributors, downstreams, and QA teams gain a reference design for reproducible, testable OS delivery.  
  - Watch next: Boot.iso’s migration to Image Builder, more ostree/bootc adoption, and stronger policy-level test gating.
