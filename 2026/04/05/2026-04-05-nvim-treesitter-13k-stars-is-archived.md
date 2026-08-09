# Nvim-treesitter (13K+ Stars) is Archived

- Score: 158 | [HN](https://news.ycombinator.com/item?id=47644667) | Link: https://github.com/nvim-treesitter/nvim-treesitter/discussions/8627

### TL;DR

The 13.5K-star nvim-treesitter repository was archived read-only on April 3, one day after a user asked why the plugin tracks latest commits instead of publishing stable releases. A reply then attacked immediate removal of Neovim 0.11 support after 0.12, calling the maintenance burden trivial and complaining that Arch’s package delay blocked updates. The supplied discussion does not state why the owner archived the project. HN largely inferred maintainer burnout and debated whether the rude complaint merely triggered an existing breaking point, while some called archiving a multi-maintainer project an overreaction.

### Comment pulse

- Aggregating many parsers and queries imports every upstream configuration change; commenters suggested manual management or separating volatile queries from installer code.
- Some defended blunt users as passionate signals of broken workflows — counterpoint: hostility toward unpaid maintainers is strategically counterproductive and personally corrosive.
- Supporters hoped the maintainer finds peace; critics questioned whether one contributor should freeze a repository shared with other maintainers.

### LLM perspective

- **View:** Centralizing volatile parsers and queries created a maintenance surface whose social cost may have exceeded its technical utility.
- **Impact:** Users lose an update hub while parser, query, and Neovim version churn shifts integration work downstream.
- **Watch next:** Ownership transfer, unarchiving, maintained forks, query-repository separation, release policy, and compatibility windows for Neovim versions.
