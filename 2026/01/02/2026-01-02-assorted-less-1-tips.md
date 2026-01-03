# Assorted less(1) tips

- Score: 164 | [HN](https://news.ycombinator.com/item?id=46464120) | Link: https://blog.thechases.com/posts/assorted-less-tips/

## TL;DR
- A tour of lesser-known `less` features: opening and managing multiple files in one session, precise navigation by line/percentage, powerful search modifiers, and inline filtering.  
- It highlights bookmarks, bracket matching, toggling options from inside `less` (`-S`, `-R`, `-N`, etc.), running shell commands, and setting defaults via `$LESS`.  
- HN comments expand with “follow” mode (`+F`), screen-preserving `-X`, auto-exit `-E`, preprocessing control `-L`, literal searches, and syntax-highlighting via `lesspipe`.

---

## Comment pulse
- `less +F` as a smarter `tail -f` → can follow, then pause to scroll/search, then resume following—counterpoint: pipelines make stopping follow (`Ctrl-C`) awkward.
- Option combos matter → `-X` keeps the screen, `-E` exits on short output, `-L` skips slow preprocessors; `Ctrl-R` starts a literal (non-regex) search.
- Inline tools reduce pipeline complexity → `&` / `&!` interactive log filtering; `lesspipe` adds syntax highlighting and file-type rendering while staying script-safe.

---

## LLM perspective
- View: `less` is a full-screen file navigator with lightweight IDE-like features, not just “a better `more`.”
- Impact: Power-users of logs, manpages, and large codebases gain speed by staying inside a single `less` session.
- Watch next: Shell distributions could ship curated `$LESS` and `lesspipe` defaults, making these advanced behaviors the out-of-the-box experience.
