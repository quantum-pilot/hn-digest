# macOS dotfiles should not go in –/Library/Application Support

- Score: 273 | [HN](https://news.ycombinator.com/item?id=45022383) | Link: https://becca.ooo/blog/macos-dotfiles/

### TL;DR

The author argues that hand-edited configuration for macOS command-line tools belongs under `$XDG_CONFIG_HOME`, normally `~/.config`, rather than `~/Library/Application Support`. Their case rests on cross-platform CLI expectations, dotfile-manager behavior, and a reading of Apple documentation that reserves Application Support for bundled GUI apps managing files on users’ behalf. Popular directory libraries can therefore produce surprising defaults. Commenters strongly dispute the interpretation, noting that XDG targets Linux userspace, macOS has native conventions, and several Apple-supplied tools use traditional home-directory dotfiles rather than `~/.config`.

### Comment pulse

- Supporters prioritized portable, user-edited configuration and consistency across Unix-like systems.
- Opponents said CLI programs remain applications and should follow each host platform’s native directories.
- Readers corrected the article’s broad claim about Apple tools uniformly using `~/.config`.

### LLM perspective

- View: The real distinction is user-authored portable configuration versus app-managed state, not CLI versus GUI alone.
- Impact: Library defaults silently turn a contested convention into ecosystem-wide behavior.
- Watch next: Document precedence, honor explicit XDG variables, and provide migrations without duplicating or losing configuration.
