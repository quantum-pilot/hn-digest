# Linux Kernel Explorer

- Score: 519 | [HN](https://news.ycombinator.com/item?id=46066280) | Link: https://reverser.dev/linux-kernel-explorer

### TL;DR

Linux Kernel Explorer presents the v6.1 source tree beside a nine-chapter guided tour of kernel concepts, starting with the distinction between kernel execution and ordinary processes. It links explanations directly to files and symbols such as `start_kernel`, `task_struct`, `current`, `kernel_clone`, kernel threads, and `getdents`, aiming to show newcomers where important mechanisms live. Commenters liked the layered annotations and curated entry points, but compared it with established source browsers offering stronger search, requested dependency or AI explanations, and reported GitHub API rate limits plus directory-navigation bugs.

### Comment pulse

- Guided-entry value → curated chapters help outsiders find foundational code that an undifferentiated source tree obscures.
- Feature comparison → existing browsers already provide cross-references and search; commenters wanted clearer differentiation.
- Implementation weakness → direct GitHub API dependence causes shared-IP rate limits and incorrect directory handling.

### LLM perspective

- View: Editorial sequencing is the product’s distinctive value, while raw source navigation is already well served.
- Impact: Learners gain a conceptual map but may hit reliability limits before developing browsing fluency.
- Watch next: Add caching, symbol cross-references, tested directory navigation, version choice, and explicit comparison with mature explorers.
