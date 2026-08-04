# Azure Linux 4.0 is Microsoft's first general-purpose Linux

- Score: 192 | [HN](https://news.ycombinator.com/item?id=48407499) | Link: https://www.boxofcables.dev/azure-linux-4-0-is-microsofts-first-general-purpose-linux/

### TL;DR

Azure Linux 4.0 entered public preview as an image for any Azure VM, expanding beyond its AKS-host role; WSL support is planned. Based on a Fedora 43 snapshot with documented declarative overlays, it adds dnf5, kernel 6.18 LTS, SELinux, signed repositories, SBOMs, container and distroless images, and planned FIPS 140-3 certification. The author frames this as its transition from appliance distro to selectable server OS. HN disputed the general-purpose label because Microsoft positions it for Azure, not arbitrary desktops or hardware, while valuing its auditable Fedora-to-image supply chain for compliance.

### Comment pulse

- Scope → Critics reserve general-purpose for desktop-capable, broadly supported hardware — counterpoint: defenders mean any application across VMs, containers, and selected bare metal.
- Assurance → SBOMs and documented Fedora overlays could simplify audit evidence by tracing deployed components and Microsoft-specific changes back toward source.
- Upstream → Some saw a Fedora snapshot as risky appropriation; others noted Amazon Linux and historical CentOS users similarly build on Red Hat work.

### LLM perspective

- **View:** The naming dispute masks the practical product boundary: broad workload support inside Microsoft’s estate, not universal device support.
- **Impact:** Platform teams could standardize patching and attestations across Microsoft-hosted deployments, while mixed-cloud estates retain another distribution-specific baseline.
- **Watch next:** General availability, WSL release, FIPS 140-3 completion, ISV certifications, support lifecycle, and documented non-Azure installation results.
