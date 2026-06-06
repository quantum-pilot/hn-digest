# VS Code inserting 'Co-Authored-by Copilot' into commits regardless of usage

- Score: 584 | [HN](https://news.ycombinator.com/item?id=47989883) | Link: https://github.com/microsoft/vscode/pull/310226

### TL;DR
VS Code quietly flipped the `git.addAICoAuthor` setting from `off` to `all`, causing a hidden `Co-authored-by: Copilot` trailer to be appended to many commits—even when users weren’t using Copilot or had AI features disabled. Developers discovered this only after seeing bogus attribution in public repos, sparking backlash over trust, legal implications, and Microsoft’s AI‑at‑all‑costs product strategy. A later change narrowed the default to `chatAndAgent`, but the incident badly damaged confidence in VS Code’s stewardship and telemetry/AI agenda.

---

### Comment pulse
- AI over standards → Big vendors keep breaking long‑standing UX norms to push LLM features, showing management prioritizes AI metrics and lock‑in over user expectations.  
- Commits as records → Auto‑adding hidden co‑authors corrupts legal/technical history, may affect copyright status, and mimics “Sent from my iPhone” but on an invisible, immutable audit trail.  
- Trust in Microsoft → Change went from `off`→`all`→`chatAndAgent`, reviewed/merged by its author; commenters see either willful growth hacking or worrying incompetence—counterpoint: at least they partially rolled it back.

---

### LLM perspective
- View: Anything that silently mutates commit metadata crosses a red line; this should always be explicit, opt‑in, and visible in the editor.
- Impact: Enterprises, compliance teams, and open‑source maintainers will revisit VS Code defaults, AI policies, and allowed tooling in regulated repos.
- Watch next: Clearer AI‑attribution standards in Git tools, org‑wide policies disabling such tags, and rival editors advertising “no hidden AI in your commits.”
