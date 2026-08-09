# macOS 26 breaks custom DNS settings including .internal

- Score: 309 | [HN](https://news.ycombinator.com/item?id=47440759) | Link: https://gist.github.com/adamamyl/81b78eced40feae50eae7c4f3bec1f5a

### TL;DR

A bug report says macOS 26.3.1 silently ignores `/etc/resolver` supplemental DNS for non-IANA suffixes, including `.internal`, `.test`, `.home.arpa`, and arbitrary private TLDs. Although `scutil --dns` registers the configuration and direct `dig` queries reach dnsmasq, system `getaddrinfo` calls fail because `mDNSResponder` returns an internal mDNS miss without sending unicast traffic. `/etc/hosts` is the only reported reliable workaround. HN readers shared other macOS 26 regressions but questioned this report’s accuracy because its AI-assisted text repeatedly cites nonexistent macOS 25.

### Comment pulse

- `*.localhost` works automatically in modern browsers and supports nested subdomains, but not arbitrary services or remote targets.
- Some said `/etc/resolver` was already deprecated and suggested `scutil` — counterpoint: others report mDNSResponder can still override that configuration.
- Developers contrasted Apple’s willingness to break workflows with Linux rollback options, while acknowledging every operating system has comparable papercuts.

### LLM perspective

- **View:** Silent configuration acceptance is worse than explicit deprecation because diagnostics affirm a path the resolver ignores.
- **Impact:** Local development, VPN, Docker, and Kubernetes tooling may require per-version DNS workarounds.
- **Watch next:** Apple’s response, clean-system reproduction, and whether 26.3.0 versus 26.3.1 isolates the regression.
