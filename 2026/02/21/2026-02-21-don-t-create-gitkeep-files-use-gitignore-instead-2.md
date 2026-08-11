# Don't create .gitkeep files, use .gitignore instead (2023)

- Score: 122 | [HN](https://news.ycombinator.com/item?id=47094877) | Link: https://adamj.eu/tech/2023/09/18/git-dont-create-gitkeep/

### TL;DR

Because Git tracks files rather than empty directories, projects commonly commit a `.gitkeep` placeholder and maintain root ignore rules. The author instead recommends placing a two-line `.gitignore` inside the required directory that ignores everything except itself, keeping intent and rename behavior local. HN disputed whether this is simpler: critics prefer one centralized ignore file, build systems that create output directories, or a README explaining the directory. Others noted the article’s shell command mishandles newlines and debated whether explicitly un-ignoring a tracked `.gitignore` is necessary.

### Comment pulse

- Local `.gitignore` survives directory renames → centralized rules are easier to audit when many generated directories exist.
- Build directories can be artifacts → creating them during builds avoids tracking placeholders and eliminates status noise.
- A README preserves the directory while documenting purpose → counterpoint: packaging may accidentally include it.

### LLM perspective

- **View:** Choose the convention that makes intent discoverable; Git assigns no special meaning to `.gitkeep`.
- **Impact:** Templates benefit from self-contained rules, while mature repositories may favor centralized policy.
- **Watch next:** Correct newline-safe setup examples and behavior under renames, clean commands, and packaging.
