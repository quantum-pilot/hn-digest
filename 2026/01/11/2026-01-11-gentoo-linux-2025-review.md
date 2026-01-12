# Gentoo Linux 2025 Review

- Score: 287 | [HN](https://news.ycombinator.com/item?id=46574769) | Link: https://www.gentoo.org/news/2026/01/05/new-year.html

## TL;DR
Gentoo’s 2025 recap shows a highly active, shoestring-budget meta‑distribution doubling down on portability, toolchains, and flexibility. Contributions and bug activity dipped slightly but remain high; four new devs joined. Big changes include planning a GitHub mirror/pull-request migration to Codeberg, finalizing EAPI 9, better RISC‑V and WSL images, dropping stable for hppa/sparc, a system‑wide build jobserver, cleaner Rust/Ada/D bootstraps, BLAS switching via FlexiBLAS, and multiple GPG providers. Financials highlight huge volunteer labor riding on surprisingly small donations.

---

## Comment pulse
- Gentoo as DIY meta‑distro → users automate container-based builds, NAS build hosts, and binpkg fleets, effectively rolling custom distros from source.
- RISC‑V and new ISAs → some argue Gentoo’s source-first model scales best to new architectures — counterpoint: other distros already ship RISC‑V and embedded uses Yocto/Buildroot.
- Funding vs impact → Gentoo runs critical infra (Portage under ChromeOS, even NASDAQ) on tiny cash, with millions in implied volunteer labor costs.

---

## LLM perspective
- View: Gentoo’s focus on bootstrapping, jobserver coordination, and crypto/BLAS indirection future‑proofs it as a “toolchain lab” for the ecosystem.
- Impact: Particularly valuable for custom silicon, HPC, and distros leveraging Portage, which gain flexibility without reinventing low-level plumbing.
- Watch next: Whether Codeberg migration, WSL presence, and improved binaries attract more users, contributors, and institutional funding.
