# Show HN: Terminal UI for AWS

- Score: 152 | [HN](https://news.ycombinator.com/item?id=46491749) | Link: https://github.com/huseyinbabal/taws

### TL;DR

taws is an MIT-licensed Rust terminal interface for browsing and managing AWS across profiles and regions. It advertises 94-plus resource types, one-key refresh, Vim-style navigation, filtering, fuzzy selection, JSON or YAML detail views, and direct EC2 start, stop, and terminate actions. HN saw value in fast SSH-friendly exploration without the console, especially under read-only roles. Others worried that another mutable layer could misinterpret commands against stateful production resources and preferred infrastructure-as-code, explicit plans, or the AWS CLI.

### Comment pulse

- TUI fans value keyboard speed and discoverability → the interface works over SSH without browser exposure, heavy JavaScript, or memorized flags.
- Operators mainly want unified observation → rapid resource and log inspection can complement infrastructure-as-code without replacing it.
- Mutation divides opinion → read-only permissions bound failures, while destructive actions need plan previews and unmistakable confirmation.

### LLM perspective

- View: The strongest niche is observational; write operations demand safeguards proportionate to AWS blast radius.
- Impact: Operators may inspect multi-account estates faster, but teams inherit another credentialed client and trust boundary.
- Watch next: Test read-only roles, action confirmations, audit logs, cost visibility, pagination correctness, and failure handling.
