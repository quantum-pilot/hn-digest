# “You should never build a CMS”

- Score: 128 | [HN](https://news.ycombinator.com/item?id=46261020) | Link: https://www.sanity.io/blog/you-should-never-build-a-cms

### TL;DR
- Sanity replies to Lee Robinson’s migration of cursor.com from Sanity to markdown-in-git. They agree traditional/headless CMSs have painful complexity and bad UIs, but argue Lee effectively rebuilt a lightweight CMS using git, markdown, and custom tools. That model works for a small, dev-only team with a single website, but breaks down when you need structured, reusable content, rich querying, collaboration, and governance. Sanity’s pitch: don’t delete the CMS—make it AI-native, queryable, and agent-accessible so you can often skip the UI.

### Comment pulse
- Both posts are marketing: Cursor selling AI-centric workflows, Sanity defending proprietary CMS—but commenters note good developer marketing can still be genuinely educational.
- Skeptics argue git-as-CMS is unusable for marketers; proponents say GUIs or WYSIWYG layers atop git can work, though adoption and training vary by company.
- Discussion highlights tradeoffs: robust, general tools like git with complex workflows versus simpler, CMS-specific versioning that may lack merges but better matches content teams.

### LLM perspective
- View: Architecture choice should follow org shape—team skills, channels, compliance—rather than ideology about “no CMS” or “pure headless”.
- Impact: As agents mature, content systems will bifurcate into agent-first structured stores and minimal markdown stacks for small, developer-only sites.
- Watch next: benchmarks of authoring speed, errors, and maintenance cost between git-based sites, traditional CMSs, and AI-augmented structured platforms.
