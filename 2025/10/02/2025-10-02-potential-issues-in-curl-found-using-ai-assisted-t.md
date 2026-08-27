# Potential issues in curl found using AI assisted tools

- Score: 412 | [HN](https://news.ycombinator.com/item?id=45449348) | Link: https://mastodon.social/@bagder/115241241075258997

### TL;DR

curl maintainer Daniel Stenberg reported receiving a very large set of potential issues produced with Joshua Rogers's AI-assisted analysis tools. Stenberg said the results contained many analyzer-style nits and mostly small bugs, but could include one or two security flaws. He had already landed 22 fixes and still had more than twice as many reports to review, crediting changes to “Joshua's sarif data.” The brief post does not identify the models, workflow, false-positive rate, or confirmed security impact.

### Comment pulse

- Commenters preferred AI as a suspicious-code finder that supports human review rather than an autonomous code author.
- The positive result stood out after curl's maintainer had previously criticized low-quality AI-generated vulnerability reports.

### LLM perspective

- View: The valuable artifact is a triageable findings set, not an AI label or an unverified vulnerability count.
- Impact: High-recall analysis can help mature projects only when maintainers can cheaply validate and prioritize results.
- Watch next: Rogers's promised retrospective should quantify tooling, review effort, duplicates, false positives, fixes, and security findings.
