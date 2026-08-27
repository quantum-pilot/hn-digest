# Notes on switching to Helix from Vim

- Score: 255 | [HN](https://news.ycombinator.com/item?id=45539609) | Link: https://jvns.ca/blog/2025/10/10/notes-on-switching-to-helix-from-vim/

### TL;DR

After twenty years with Vim and Neovim, Julia Evans used Helix for three months to obtain working language servers, contextual shortcut help, repository search with surrounding context, and multiple-cursor editing without maintaining a large configuration. Learning Helix's selection-first model took only a week or two when she stopped imitating Vim. Missing persistent undo, weak Markdown list handling and reflow, manual file reloads, absent tabs, and roughly weekly crashes remain drawbacks. HN users split between praising batteries-included ergonomics and questioning those reliability and feature gaps.

### Comment pulse

- Integrated defaults reduce maintenance → users value portable LSPs, search, contextual help, and fewer third-party plugins or supply-chain dependencies.
- Reliability concerns are material → crashes combine badly with absent persistent undo, though some HEAD users report almost none.
- Mature Vim workflows remain competitive → lightweight configurations and newer Neovim distributions make switching less compelling for satisfied users.

### LLM perspective

- View: Helix trades ecosystem breadth and mature edge cases for coherent defaults that lower configuration ownership.
- Impact: Developers frustrated by editor maintenance can gain modern navigation while relearning modal semantics and accepting gaps.
- Watch next: Follow persistent undo, automatic reloads, plugin support, Markdown editing, crash rates, and file-explorer releases.
