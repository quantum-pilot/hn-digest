# On caring for user data: NeoVim caused Vim undo files to be deleted

- Score: 384 | [HN](https://news.ycombinator.com/item?id=49867067) | Link: https://unsung.aresluna.org/they-had-no-concept-of-a-duty-of-care-to-their-users/

### TL;DR

An essay amplifies David Chisnall’s account that trying early Neovim destroyed persistent Vim undo history by replacing incompatible files without migration or warning. For him, the decisive failure was not merely format breakage but maintainers’ alleged dismissal of a feature explicitly promising persistence. Discussion added crucial nuance: Vim and Neovim shared a user-configured undo directory, not a common default. Commenters still disputed whether deleting unrecognized history violated the feature contract, or whether shared cache-like storage weakened that expectation.

### Comment pulse

- Silent deletion breached user trust → critics argued incompatible history should be ignored, preserved, or migrated rather than overwritten.
- Shared configuration changes responsibility → both editors used the same explicitly configured directory, complicating claims that Neovim automatically targeted Vim data.
- Persistent undo is not backup → some recommended version control — counterpoint: undo preserves intermediate states that saved commits may not capture.

### LLM perspective

- View: The disputed setup reduces Neovim’s blame but does not erase the case for non-destructive format handling.
- Impact: One destructive migration can permanently outweigh years of feature improvements for users who depend on editor state.
- Watch next: Projects should document compatibility, separate namespaces, warn before deletion, and test upgrades against real user configurations.
