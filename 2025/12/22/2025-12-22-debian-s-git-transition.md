# Debian's Git Transition

- Score: 186 | [HN](https://news.ycombinator.com/item?id=46352231) | Link: https://diziet.dreamwidth.org/20436.html

## TL;DR

Debian veterans Ian Jackson and Sean Whitton describe a long-term transition from traditional .dsc source packages and tarballs to treating git as the single canonical form of Debian source. Tools like dgit, tag2upload and git-debrebase provide a lossless bridge, standardizing on “patches-applied” branches and a permanent, append‑only git depository separate from Salsa. Core technology works, but widespread maintainer adoption, documentation rewrites, and whole‑archive importing are still needed; commenters broadly support ditching patch quilting and modernizing workflows.

## Comment pulse

- Patch quilting is harmful → HNers welcome patches-applied git history; quilting/gbp-pq add overhead and deter contributors — counterpoint: gbp-pq still useful for floating patch queues.  
- Transition scope is huge → Core tools already git-based, but long tail of packages and workflows makes migration slow and documentation-heavy.  
- Bundling source with packaging feels clumsy → Some prefer ports-style recipes; Debian prioritizes offline, reproducible builds and single-repo truth for code plus packaging.  

## LLM perspective

- View: Formalizing git as canonical Debian source aligns distro practices with modern VCS reality and improves transparency for derivatives.  
- Impact: Maintainers must adapt workflows; downstreams, CI systems, and security teams gain simpler, standardized ways to fetch and rebuild sources.  
- Watch next: tag2upload exit from beta, whole-archive importer deployment, and buildds/QA switching from .dsc inputs to git clones.
