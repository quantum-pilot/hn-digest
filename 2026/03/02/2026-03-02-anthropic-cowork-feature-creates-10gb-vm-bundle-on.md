# Anthropic Cowork feature creates 10GB VM bundle on macOS without warning

- Score: 349 | [HN](https://news.ycombinator.com/item?id=47218288) | Link: https://github.com/anthropics/claude-code/issues/22543

### TL;DR

Claude Desktop’s Cowork feature provisions a Linux virtual-machine bundle whose root filesystem reached 10GB, regenerated after deletion, and appeared even for some people who had not knowingly used Cowork. The issue reporter also measured rising idle CPU and swap use; deleting the VM and caches briefly improved affected tasks by roughly 75%, suggesting a separate runtime leak or accumulating work. Anthropic says the VM gives its coding agent an isolated, configurable computer and stronger safety boundaries, while acknowledging demands for disclosure, opt-in provisioning, removal controls, and lower overhead.

### Comment pulse

- Sandboxing won broad support because hidden generated code needs hard boundaries — counterpoint: unexplained disk, memory, and DNS costs undermine user trust.
- Users wanted first-use warnings, an opt-in download, a disable-and-remove toggle, and host access limited to explicitly chosen folders.
- A sparse-image caveat could reduce apparent disk usage, but it would not explain sustained CPU, RAM, or responsiveness problems.

### LLM perspective

- **View:** The VM is defensible infrastructure; silent provisioning and weak lifecycle controls are the product failure.
- **Impact:** Resource surprises disproportionately punish low-storage, 8GB Macs and nontechnical users Cowork intends to protect.
- **Watch next:** Lazy downloads, clear size reporting, cleanup, disablement, idle-resource fixes, and whether VM isolation remains mandatory.
