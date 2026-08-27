# Assorted less(1) tips

- Score: 164 | [HN](https://news.ycombinator.com/item?id=46464120) | Link: https://blog.thechases.com/posts/assorted-less-tips/

### TL;DR

The guide treats `less` as an interactive workspace rather than merely a pipeline terminator. It covers opening and managing multiple files, percentage and line jumps, cross-file searches, regex filtering with `&`, global bookmarks, bracket matching, runtime option toggles, external commands, editor handoff, and saving piped input. HN readers added follow mode with `F`, screen-preserving and quick-exit options, literal searches, preprocessing bypasses, and `lesspipe`, while warning that interrupting follow mode inside pipelines can terminate upstream producers.

### Comment pulse

- Follow mode can replace many `tail` sessions → pause with an interrupt, inspect history, then resume using `F`.
- Interactive filtering shines during debugging → operators can discover useful exclusions without restarting expensive pipelines.
- Defaults materially change usability → screen preservation, short-output exit, colors, numbering, and preprocessing deserve deliberate configuration.

### LLM perspective

- View: `less` is most powerful when treated as a stateful terminal viewer with reversible transformations.
- Impact: Operators can inspect large or live outputs faster while avoiding reruns of costly commands.
- Watch next: Test pipeline interrupt behavior, distro-specific preprocessors, and portable `$LESS` settings before standardizing workflows.
