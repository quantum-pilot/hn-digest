# I Inspected My Take-Home Interview Project. It Was a Whole Operation

- Score: 233 | [HN](https://news.ycombinator.com/item?id=49013036) | Link: https://citizendot.github.io/articles/fake-job-interview-git-hook-malware/

## TL;DR
A fake recruiter offered an unusually high-paid Python “contract-to-hire” role, then sent a FastAPI take-home test. The repo looked normal until a hidden `.git/hooks/pre-commit` script appeared: it fetched OS-specific payloads from a hard-coded IP, installed a secondary Bash script, then Node, then an obfuscated `parser.js` plus a Hardhat-based toolchain likely aimed at stealing crypto or other sensitive tokens. Variants hide triggers in `.vscode` launch configs. The project itself was a cloned OSS repo; only the hidden malware was custom. Lesson: never blindly run git hooks or open unknown projects in your editor.

---

## Comment pulse
- Others report similar “interview” repos with malware → sophisticated social engineering, sometimes likely targeted at maintainers of popular packages.
- Malware-embedded take-home projects are now recurring → git hooks and dev tooling are underappreciated attack surfaces — counterpoint: few devs expect `git commit` itself to be dangerous.
- VSCode workspace trust blocks such launch configs, but UX is weak → users often click through without understanding that “trust” may execute arbitrary commands.

---

## LLM perspective
- View: LLMs can help reverse-engineer obfuscated payloads, but safety filters can also block useful defensive analysis.
- Impact: Developers, recruiters, and OSS maintainers must treat interview codebases like untrusted binaries, not neutral homework.
- Watch next: Better defaults in git/IDEs (hook warnings, trust prompts) and platform guidelines for secure technical-interview workflows.
