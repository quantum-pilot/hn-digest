# Show HN: Witr – Explain why a process is running on your Linux system

- Score: 491 | [HN](https://news.ycombinator.com/item?id=46392910) | Link: https://github.com/pranshuparmar/witr

### TL;DR

Witr is a read-only command-line tool that traces why a Linux or macOS process exists. Given a name, PID, or port, it maps the target to a PID, follows its ancestry, identifies a primary supervisor such as systemd, launchd, Docker, PM2, cron, or a shell, and adds context and warnings. HN readers welcomed its incident-debugging focus, while noting systemctl and lsof already expose parts of the answer and requesting signed Debian or RPM packages instead of curl installation.

### Comment pulse

- Consolidation is useful → one causal narrative replaces manual correlation across process, service, container, and network tools.
- Scope can confuse → it explains how a process started, not what unknown software actually does.
- Distribution limits adoption → production users want managed packages, update provenance, and security-patch visibility.

### LLM perspective

- View: Witr's value is normalization and explanation, not novel access to process metadata.
- Impact: Operators can reduce diagnosis time during incidents, especially across unfamiliar supervision layers.
- Watch next: Add trusted distro packages and test causal accuracy for containers, ambiguous names, and restricted processes.
