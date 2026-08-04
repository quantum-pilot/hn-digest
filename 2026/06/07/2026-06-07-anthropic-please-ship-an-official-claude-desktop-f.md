# Anthropic, please ship an official Claude Desktop for Linux

- Score: 436 | [HN](https://news.ycombinator.com/item?id=48434436) | Link: https://github.com/anthropics/claude-code/issues/65697

### TL;DR

A feature request asks Anthropic to publish an official, signed Claude Desktop build for Ubuntu LTS and Debian—or at least state its Linux roadmap. Claude Code already ships native Linux packages, and Cowork reportedly runs Claude Code inside Linux VMs, yet Linux users lack desktop extensions, computer use, dictation, scheduled tasks, richer artifacts, and supported plugin testing. Community repackages fill the gap but handle credentials and files without vendor audit. HN agreed demand exists but debated whether Electron portability outweighs Linux fragmentation, QA, support, and opportunity costs.

### Comment pulse

- Security → Unofficial builds can be polished yet remain unaudited credential-handling software; vendor signing would reduce structural trust risk.
- Support burden → Maintainers report compatibility failures across distributions, compositors, sandboxes, graphics stacks, and aging hardware; coding is not the dominant cost.
- Feasibility → Discord and community ports show complex Electron clients can work — counterpoint: successful packaging does not eliminate long-term QA obligations.

### LLM perspective

- **View:** The minimum responsible response is explicit policy and security guidance, even if a supported build remains uneconomic.
- **Impact:** Linux plugin authors lose workflow parity, while Anthropic externalizes packaging and trust costs to volunteers.
- **Watch next:** Track an official roadmap, recommended package, security review, Flatpak feasibility, extension parity, distro support matrix, and issue routing.
