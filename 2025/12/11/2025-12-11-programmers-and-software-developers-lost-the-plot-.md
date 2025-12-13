# Programmers and software developers lost the plot on naming their tools

- Score: 416 | [HN](https://news.ycombinator.com/item?id=46234806) | Link: https://larr.net/p/namings.html

### TL;DR
The author argues that programmers have abandoned clear, descriptive naming for libraries and tools in favor of random animals, acronyms, and in-jokes, imposing a constant “cognitive tax” on anyone reading code or infrastructure diagrams. They contrast older, purpose-revealing names (FORTRAN, diff, directory editor) with modern stacks full of Vipers, Cobras, and Melodies that say nothing about function. HN commenters largely dispute the nostalgia and absolutes: other sciences also use whimsical names, old Unix names weren’t obvious either, and descriptiveness has its own costs.

---

### Comment pulse
- Naming was never purely sensible → classic tools (dd, Bison, Emacs, Perl, Java, Git) are as opaque as today’s; author cherry-picks history.  
- Descriptive names age badly → projects evolve beyond “X Validator/Manager,” and generic names harm searchability; unique whimsical names become easier to find. — counterpoint: boring, scoped names encourage “do one thing well.”
- Cognitive load stems from domain complexity → dense acronym systems in cars, telecom, biology are exhausting even when perfectly “technical”; arbitrary vs descriptive helps less than claimed.

---

### LLM perspective
- View: Treat internal/infrastructure naming as UX; balance memorability with at-a-glance category hints (e.g., “ZephyrDB,” “Cobra-CLI”).
- Impact: Teams maintaining large systems, onboarding juniors, and SREs doing incident response gain most from slightly more semantic names.
- Watch next: Style guides and tooling that flag opaque names in public APIs; empirical studies on error rates vs naming styles in large codebases.
