# Jujutsu for everyone

- Score: 442 | [HN](https://news.ycombinator.com/item?id=45083952) | Link: https://jj-for-everyone.github.io/

### TL;DR

This tutorial teaches Jujutsu version control to people with no Git or version-control experience, including terminal basics. Its pitch is that Jujutsu works with Git repositories, presents a simpler interface, and still offers advanced history-editing capabilities. The author acknowledges tradeoffs: peers use Git terminology, some Git features still require fallback commands, and Jujutsu’s command-line interface can change. Commenters supplied the missing practical contrast, praising automatic rebasing, revsets, deferred conflict resolution, and stash-free workflows while reporting limitations or problems involving LFS, remote bookmarks, ignored files, and lost changes.

### Comment pulse

- One commenter reported an ignored credential becoming tracked after editing older history; another described unexplained lost changes and stale-workspace messages.
- Experienced users praised composable primitives but asked the introduction to substantiate its “more powerful than Git” claim.

### LLM perspective

- View: Teaching Jujutsu first is credible only if beginner simplicity includes honest coverage of immature edges.
- Impact: Git compatibility lowers adoption cost, but trust failures around file tracking can outweigh ergonomic gains.
- Watch next: LFS support, ignore semantics, workspace reliability, and stable collaboration patterns remain decisive.
