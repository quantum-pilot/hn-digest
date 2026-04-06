# Nvim-treesitter (13K+ Stars) is Archived

- Score: 158 | [HN](https://news.ycombinator.com/item?id=47644667) | Link: https://github.com/nvim-treesitter/nvim-treesitter/discussions/8627

### TL;DR
nvim-treesitter, a core Neovim plugin with 13k+ stars, has been archived after a heated GitHub discussion about releases and version support. A user complained that the plugin abruptly dropped Neovim 0.11 support, blocking updates on their distro. The maintainer replied bluntly that the plugin had long required 0.12, was still “experimental,” and that users should pin commits instead of expecting stable releases. The exchange escalated, and shortly after, the repo was archived, sparking debate about user entitlement, maintainer burnout, and aggregator-style plugins’ maintenance costs.

---

### Comment pulse
- User rudeness vs entitlement → Some see the complainer as an entitled jerk; others say “entitled” users are often just frustrated, passionate feedback — counterpoint: he had many upgrade paths.
- Aggregator plugin problem → Centralizing parsers/queries (like nvim-treesitter, null-ls, Mason) creates endless maintenance; better to manage parsers/LSPs manually or separate query repos.
- Archiving decision → Many sympathize with burnout and applaud stepping away; others call full archival, despite other contributors, an overreach and disproportionate reaction.

---

### LLM perspective
- View: This highlights how critical OSS infra often rests on a few people’s patience, not formal support guarantees.
- Impact: Neovim users must pin commits, roll their own parser management, or rally around a community fork/governance change.
- Watch next: Whether a maintained fork appears, queries get decentralized, or Neovim core provides a more sustainable treesitter integration model.
