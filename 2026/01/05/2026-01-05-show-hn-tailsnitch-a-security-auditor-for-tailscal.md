# Show HN: Tailsnitch – A security auditor for Tailscale

- Score: 235 | [HN](https://news.ycombinator.com/item?id=46501137) | Link: https://github.com/Adversis/tailsnitch

- TL;DR  
Tailsnitch is a CLI security auditor for Tailscale tailnets that scans ACLs, devices, auth keys, DNS and SSH settings for 50+ misconfigurations, ranks them by severity, and can optionally fix some via the Tailscale API. It exports JSON and SOC 2–mapped reports, supports ignore files, and runs well in CI/CD. HN readers like it for taming large ACLs but also wish for complementary live session/traffic visibility and clearer guidance around tagging user devices and non-Tailscale (Headscale) support.

- Comment pulse  
  - Config linter is useful, but some want structured, real-time SSH and tailnet logs—Teleport-style observability, not just static checks — counterpoint: different tool category.  
  - Tailscale advice against tagging user devices conflicts with practical needs to differentiate phone vs laptop access, raising usability vs security trade-off questions.  
  - Growing tailnets with huge ACL files create anxiety; automating checks in CI/CD complements Tailscale’s policy tests, which some find harder to write.

- LLM perspective  
  - View: This brings familiar "infrastructure as code" linting to Tailscale, closing a gap between hobby and audited environments.  
  - Impact: Helps small teams avoid silent overexposure while giving compliance-heavy orgs quick SOC 2 evidence without bespoke scripts.  
  - Watch next: Headscale support, customizable rule sets, and deeper export into SIEMs for correlating config drift with incident timelines.
