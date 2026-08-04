# How to stop Claude from saying load-bearing

- Score: 409 | [HN](https://news.ycombinator.com/item?id=48905248) | Link: https://jola.dev/posts/how-to-stop-claude-from-saying-load-bearing

### TL;DR

A parody tutorial uses Claude Code’s `MessageDisplay` hook to pipe each displayed text delta through a Python regex filter, replacing recurring phrases such as “load-bearing,” “honest take,” and “you’re absolutely right” with absurd alternatives. The executable hook takes effect in new sessions. The technique changes rendered wording, not the model’s underlying output or behavior. HN readers catalogued broader “Claudisms,” noting that repetition is tolerable inside an agent but jarring in supposedly human prose. Debate ranged from custom style instructions to whether model-scale verbal habits are reshaping human language.

### Comment pulse

- Context changes tolerance → familiar tics are harmless during tool use but signal laziness or undisclosed generation when they appear in authored prose.
- Scale amplifies stylistic bias → one person’s verbal habit is minor; billions of similarly phrased tokens make model preferences culturally conspicuous.
- Customization helps, imperfectly → hooks and instruction files can suppress praise or pronouns — counterpoint: post-processing may mask symptoms without improving reasoning or source prose.

### LLM perspective

- **View:** Repeated phrases are not merely aesthetic; they become provenance cues that alter trust before readers evaluate substance.
- **Impact:** Large-volume model prose can stigmatize ordinary human vocabulary, narrowing expressive choices and making writers police harmless phrases.
- **Watch next:** Style variation, training-time repetition penalties, stronger user controls, and evaluations separating fluency from sustained coherence.
