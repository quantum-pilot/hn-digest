# Rebasing in Magit

- Score: 177 | [HN](https://news.ycombinator.com/item?id=47323105) | Link: https://entropicthoughts.com/rebasing-in-magit

- TL;DR  
Magit, the Emacs interface to Git, turns the git log into an interactive “command center” where you compose complex operations like rebases through discoverable key hints, fuzzy menus, and live feedback. The article walks through rebasing one branch onto another directly from the log and shows how Magit exposes the exact underlying git commands, teaching features like --autostash and --force-with-lease. HN commenters praise Magit’s UX, debate Emacs’ performance, and compare alternatives such as LazyGit, jj/jjui, neogit, and majutsu.

- Comment pulse  
  - Magit users call it the best Git UI: rebases, subset rebases, and fine-grained staging feel effortless—counterpoint: many avoid it rather than learn Emacs, preferring LazyGit/neogit.  
  - Some lament Emacs’ sluggish startup and Magit load times versus Neovim; others argue Emacs is a long-lived “shell-like” environment, so startup barely matters.  
  - Jujutsu gains traction via Emacs’ majutsu and the jjui TUI, letting Magit fans try a new VCS without losing familiar workflows.

- LLM perspective  
  - View: Magit exemplifies “transparent power tools”: rich interaction layered over CLI commands while explicitly showing the exact operations executed.  
  - Impact: Such tooling can lower risk of complex history edits and train users in advanced Git concepts and flags.  
  - Watch next: Watch for Magit-like interfaces in other editors and VCSs; consistent key-driven logs could become a standard pattern for safe refactoring.
