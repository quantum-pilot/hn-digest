# ZCode, the GLM coding agent, silently uploads your Git history

- Score: 258 | [HN](https://news.ycombinator.com/item?id=49752422) | Link: https://tokenstead.ai/guides/zcode-silent-git-history-upload

### TL;DR

Tokenstead's paraphrase of ferstar's reverse engineering alleges that logged-in ZCode silently archives entire workspaces—including Git objects, LFS data, reflogs, and configuration—then encrypts them with a server-provided public key and uploads them to Aliyun OSS. In one reported case, Git data formed 86.6% of a 313 MB archive; privacy toggles changed training authorization or indexing, not capture. HN commenters criticized the derivative article's terminology and presentation, but agreed the claimed payload extends far beyond ordinary commit logs and warrants examining the original forensics.

### Comment pulse

- Repository history expands exposure → objects can retain deleted secrets, private branches, internal paths, and years of code absent from the current working tree.
- User controls allegedly miss the capture path → the article says a host sidecar uploads outside agent tools and continues despite indexing or training settings.
- Source quality weakened trust → commenters called the piece AI-paraphrased and confused about Git terminology — counterpoint: they said the underlying reported payload remains serious.

### LLM perspective

- View: Open weights do not make a proprietary harness local; runtime telemetry and encryption ownership define the trust boundary.
- Impact: Developers risk disclosing historical commercial code and credentials even when they expect only prompt-relevant files to leave their machines.
- Watch next: Verify ferstar's original evidence, Z.ai's response, a true upload opt-out, retention rules, and independently tested remediation.
