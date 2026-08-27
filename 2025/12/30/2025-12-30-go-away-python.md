# Go away Python

- Score: 321 | [HN](https://news.ycombinator.com/item?id=46431028) | Link: https://lorentz.app/blog-item.html?id=go-shebang

### TL;DR

The author makes an executable Go source file without a shebang by exploiting shell fallback after `execve` returns `ENOEXEC`. Its first line is simultaneously valid shell, invoking `go run` on itself, and a Go comment; `exit` prevents the shell parsing subsequent Go. A block-comment variant survives `gofmt`. The pitch is dependency-free scripts backed by Go’s standard library and compatibility promise. HN countered that `uv run` plus PEP 723 handles Python scripts, and questioned whether Go’s ergonomics suit throwaway work.

### Comment pulse

- Python already has a path → `uv` can provision interpreters and dependencies, but newcomers still face fragmented guidance.
- The technique is intentionally unofficial → Go rejected shebang support, while gorun, Yaegi, and other compiled languages offer alternatives.
- Scriptability is an ergonomic category → reliable compilation helps distribution—counterpoint: verbosity invites project-grade ceremony.

### LLM perspective

- View: The hack is educational, but explicit runners communicate intent better than shell fallback behavior.
- Impact: Teams gain durable single-file utilities only by constraining dependencies and standardizing Go installation paths.
- Watch next: Test portability across shells, executable launch contexts, formatter versions, Windows, and module-requiring scripts.
