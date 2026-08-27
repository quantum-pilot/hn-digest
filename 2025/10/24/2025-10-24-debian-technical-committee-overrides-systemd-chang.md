# Debian Technical Committee overrides systemd change

- Score: 148 | [HN](https://news.ycombinator.com/item?id=45692915) | Link: https://lwn.net/Articles/1041316/

### TL;DR

Systemd 258 made `/run/lock` root-only and planned its removal, conflicting with Debian’s policy and `/var/lock` compatibility while breaking UUCP-related software in unstable. After the systemd package maintainer declined to revert the change, citing denial-of-service risks and obsolete standards, Debian’s Technical Committee required sufficiently permissive access until affected packages migrate and policy is updated. Debian 13 stable was unaffected. Commenters argued over systemd’s influence, but the core dispute was how a distribution should sequence security-driven modernization without breaking documented interfaces.

### Comment pulse

- Compatibility-first view → Debian packages must follow current policy until coordinated migration replaces the interface.
- Modernization view → world-writable lock storage carries risks, while the underlying filesystem standard is effectively abandoned.
- Responsibility dispute → some blamed systemd upstream; others saw a Debian packaging and policy-maintenance failure.

### LLM perspective

- View: The committee chose transition discipline without declaring the old locking model desirable.
- Impact: Maintainers gain time to migrate software while users avoid sudden regressions in established workflows.
- Watch next: Debian policy updates, package migrations to safer locks, and systemd’s planned directory removal.
