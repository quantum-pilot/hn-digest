# I Inspected My Take-Home Interview Project. It Was a Whole Operation

- Score: 233 | [HN](https://news.ycombinator.com/item?id=49013036) | Link: https://citizendot.github.io/articles/fake-job-interview-git-hook-malware/

### TL;DR

A supposed recruiter offered a lucrative Python role and sent a polished take-home project based on an innocent public FastAPI repository. Its visible dependencies were clean, but the included `.git` directory contained hooks that silently fetched OS-specific remote payloads when candidates ran Git commands. Later stages installed tooling and launched an obfuscated Node script with candidate-specific identifiers, apparently targeting tokens or cryptocurrency assets; related campaigns hide execution commands in `.vscode`. HN readers reported similar compromises and focused on workspace trust, overlooked hidden files, and the limits of safety-filtered malware analysis.

### Comment pulse

- The campaign may target high-value developers → one commenter found malware after a credible CTO interview and suspected selection through a 43-million-download NPM package.
- Trust prompts help only when noticed → VS Code blocks workspace execution after rejection — counterpoint: commenters said the warning rarely communicates the exact command.
- Automated analysis was inconsistent → Claude refused the obfuscated script while Gemini explained it, frustrating readers who needed defensive inspection.

### LLM perspective

- **View:** The assessment was the exploit delivery mechanism: plausible work requirements ensured victims executed repository-controlled behavior themselves.
- **Impact:** Developers handling unfamiliar interview code need the same isolation and provenance checks used for untrusted production dependencies.
- **Watch next:** Track recruiter identities, payload infrastructure, credential theft, wallet indicators, and IDE or Git warnings exposing automatic execution.
