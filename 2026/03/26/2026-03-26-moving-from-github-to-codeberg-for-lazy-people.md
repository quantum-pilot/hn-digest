# Moving from GitHub to Codeberg, for lazy people

- Score: 501 | [HN](https://news.ycombinator.com/item?id=47530330) | Link: https://unterwaditzer.net/2025/codeberg.html

### TL;DR

Codeberg’s importer can carry GitHub repositories, issues, pull requests, releases, labels, authorship, and numbering with little friction; Codeberg Pages covers static sites similarly. CI is the hard part: public projects lose GitHub’s abundant hosted capacity and free macOS runners. The author suggests cross-compilation plus a self-hosted Forgejo Actions runner, whose workflow syntax largely resembles GitHub Actions. Projects needing macOS can retain a GitHub mirror for builds, while archiving the old repository and redirecting contributors to Codeberg.

### Comment pulse

- GitHub’s community and free CI remain powerful network effects — counterpoint: defaulting there forever prevents alternatives from reaching critical mass.
- Codeberg suits public FOSS better than miscellaneous private work; commenters corrected claims that it lacks a Pages service.
- Self-hosters praised Forgejo as lightweight, reliable, extensible, and capable of running CI and package registries on modest hardware.

### LLM perspective

- **View:** Repository migration is mature; hosted compute and contributor gravity are the real lock-in.
- **Impact:** Small projects can diversify cheaply, but broad-platform testing may require hybrid infrastructure.
- **Watch next:** Private-repository policy, runner availability, Actions compatibility, and whether contributors follow projects off GitHub.
