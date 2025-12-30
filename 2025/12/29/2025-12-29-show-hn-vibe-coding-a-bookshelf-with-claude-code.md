# Show HN: Vibe coding a bookshelf with Claude Code

- Score: 250 | [HN](https://news.ycombinator.com/item?id=46420453) | Link: https://balajmarius.com/writings/vibe-coding-a-bookshelf-with-claude-code/

## TL;DR
The author finally catalogs ~460 books after years of procrastination by “vibe coding” a custom bookshelf app with Claude Code. They photograph 470 spines, use an LLM-written script to call OpenAI’s vision API, normalize metadata, fetch or synthesize covers via Open Library and Google Images, and style spines based on page counts and dominant colors. The human’s real work is decisions—acceptable error rates, visual style, deleting infinite scroll—while Claude rapidly iterates code. The core claim: execution is now cheap; taste and judgment aren’t.

## Comment pulse
- Vibe coding shines on small, self-contained projects → once codebases grow, context limits and coupling push you back to deliberate architecture and close code review.
- Critics want AI to produce novel algorithms → others reply that 90% of useful software is recombination, and LLMs already 10x that kind of work.
- Experiences vary → some report Claude failures (hallucinated URLs, awkward image segmentation), while others built similar personal libraries they’d never have finished unaided.

## LLM perspective
- View: This is a realistic pattern: humans set constraints, aesthetics, and cut features; models grind through glue code and iteration.
- Impact: Non-professional developers and solo tinkerers can now feasibly build bespoke “perfect-for-me” tools instead of settling for generic apps.
- Watch next: Better long-context coding workflows, tooling for interface-driven prompting, and shared patterns for safe partial automation in larger codebases.
