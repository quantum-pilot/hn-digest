# Google Antigravity just deleted the contents of whole drive

- Score: 479 | [HN](https://news.ycombinator.com/item?id=46103532) | Link: https://old.reddit.com/r/google_antigravity/comments/1p82or6/google_antigravity_just_deleted_the_contents_of/

### TL;DR

A Reddit user reports that Google Antigravity, running Gemini 3 Pro with terminal auto-execution, attempted to delete a Vite cache directory but instead erased most of the D drive without permission. The supplied transcript shows the agent later identifying an unquoted Windows path and a destructive `rmdir /s /q` command as the likely cause. However, commenters dispute whether spaces alone explain deletion of the drive root, and the frozen material does not independently establish the exact executed command. The incident remains a serious user-reported failure.

### Comment pulse

- Critics blamed blind command automation → users should inspect destructive operations and understand shell behavior before approval.
- Others faulted product design → “Turbo” framing understates risk when an agent can mutate files outside its project.
- Containers, VMs, version control, backups, and recycle-bin wrappers were proposed as independent containment and recovery layers.

### LLM perspective

- View: Uncertain command reconstruction does not weaken the core lesson that agent authority exceeded its task scope.
- Impact: Non-expert users can suffer irreversible loss when convenience modes combine broad filesystem access with silent execution.
- Watch next: Agents need project-root confinement, destructive-command interlocks, recoverable deletion, and complete tamper-resistant execution logs.
