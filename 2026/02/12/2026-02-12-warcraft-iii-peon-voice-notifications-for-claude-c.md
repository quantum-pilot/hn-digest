# Warcraft III Peon Voice Notifications for Claude Code

- Score: 926 | [HN](https://news.ycombinator.com/item?id=46985151) | Link: https://github.com/tonyyont/peon-ping

## TL;DR
Peon-ping is a small but polished tool that hooks into Claude Code, Codex, Cursor, and OpenCode to play classic game voice lines (Warcraft, StarCraft, Portal, etc.) when AI agents start, finish, or need input. It defines an open Coding Event Sound Pack Specification so any IDE can map events to audio packs, with simple CLI controls, per-pack rotation, and “silent under N seconds” rules. HN discussion centers on how playful, nostalgic touches like this can meaningfully improve dev tools, plus some curl-pipe-shell security concerns and DIY alternatives.

## Comment pulse
- Playful UX as differentiator → whimsical, nostalgic touches make AI coding tools feel crafted and fun, not just functional — counterpoint: don’t forget security hygiene with install scripts.  
- Nostalgia hook → Warcraft / StarCraft “annoyed unit” lines and Easter eggs remind people of games that rewarded over-interaction, making this idea instantly appealing.  
- Custom and local options → some prefer OS speech (e.g., macOS `say` via hooks) or different franchises, asking for generic JSON/skill formats to plug in any voices.

## LLM perspective
- View: Treat agent notifications as a UX surface, not just system messages; playful sound packs are a low-cost engagement upgrade.  
- Impact: IDEs and AI coding agents may converge on shared event-notification standards, enabling a small ecosystem of pluggable “sound/feel” mods.  
- Watch next: Native support in major IDEs, formalization of CESP-like specs, plus audited installers or package-manager distributions to ease security worries.
