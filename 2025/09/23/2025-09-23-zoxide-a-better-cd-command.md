# Zoxide: A Better CD Command

- Score: 295 | [HN](https://news.ycombinator.com/item?id=45342943) | Link: https://github.com/ajeetdsouza/zoxide

### TL;DR

The frozen repository capture identifies Zoxide only as a smarter cd command supporting major shells, so operational detail comes from discussion. Users describe it as learning frequently visited directories and accepting partial, fuzzy queries to jump across directory trees. Enthusiasts call it a major command-line productivity improvement and mention scoping searches with a base directory. Skeptics prefer shell history, tab completion, or explicit aliases because rankings can shift or similar names can resolve unexpectedly; one deletion anecdote illustrates why navigation mistakes can become destructive.

### Comment pulse

- Learned jumps reduce repetitive traversal → frequent projects become reachable with short fragments from anywhere.
- Fuzzy ranking trades predictability for speed → similar or changing paths require users to verify their current directory.
- Existing shell tools cover many workflows → history search, fzf completion, aliases, and previous-directory switching remain simpler alternatives.

### LLM perspective

- View: Zoxide is valuable when directory breadth exceeds what stable aliases and history handle comfortably.
- Impact: Faster navigation helps frequent shell users, while ambiguous matches increase command-context risk.
- Watch next: Test collision handling, basedir scoping, interactive selection, database aging, and safe prompt visibility.
