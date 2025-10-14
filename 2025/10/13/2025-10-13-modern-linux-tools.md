# Modern Linux tools

- Score: 200 | [HN](https://news.ycombinator.com/item?id=45566548) | Link: https://ikrima.dev/dev-notes/linux/linux-modern-tools/

- TL;DR
  - A curated list of “modern” Linux tools—often faster, more ergonomic drop‑ins and utilities—grouped as CLI replacements, new CLIs, help, and GUIs. HN splits: portability-first admins stick to built-ins on heterogeneous servers; developers cite clear wins like ripgrep, fd, fzf, jq, hyperfine. Some standardize installs with Nix/Ansible; others say “written in Rust” isn’t a feature and want problems stated. Consensus: master the classics, adopt modern tools where they measurably help on machines you control.

- Comment pulse
  - Portability-first → remote servers rarely have these; keep minimal extras via automation (Ansible). — counterpoint: on personal dev machines, modern tools’ ergonomics outweigh setup.
  - Some replacements are clear wins → ripgrep/fd/fzf/jq/hyperfine speed common tasks; aligns with UNIX “replace when better” ethos.
  - Hype isn’t enough → “written in Rust” or “modern” isn’t a feature; state problems solved; license and Windows support influence adoption.

- LLM perspective
  - View: Learn POSIX core; use aliases for tools locally; reproduce via Nix, static binaries, or devcontainers when remote constraints allow.
  - Impact: Devs gain faster search, find, preview, and benchmarking; sysadmins stay portable with minimal installs and automation.
  - Watch next: Distro defaults adopting replacements, benchmark-driven comparisons (hyperfine), standardization efforts (eza vs ls), and remote-session packaging solutions.
