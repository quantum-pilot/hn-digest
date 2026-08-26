# I built a low-latency AI companion that plays Skyrim with me

- Score: 386 | [HN](https://news.ycombinator.com/item?id=49413561) | Link: https://pantel.is/projects/ai-gaming-companion/

### TL;DR

Varkos is a voice-controlled Skyrim companion that grounds commands in game state, executes multi-step plans, fights, fetches objects, and evolves a reversible personality. Its low-latency stack combines streaming local speech recognition, a 2–20 millisecond hybrid action encoder, a fine-tuned local language model, and fast speech synthesis; responses can begin within 500 milliseconds. Large cloud models handle slow personality updates. Commenters praised the comic, agentic experience while questioning long-term reliability, hardware demands, game-specific adaptation, and whether upcoming live models will supersede the custom pipeline.

### Comment pulse

- Hybrid control beats unrestricted prompting → constrained actions and world JSON make small local models useful without asking them to reason globally.
- The jagged frontier may shrink experimentation → one unpredictable bark or failed stealth plan can teach players to prefer rigid commands.
- Local inference protects immersion and privacy → commenters welcomed low latency — counterpoint: roughly 12 GB of GPU memory limits accessibility.

### LLM perspective

- View: Embodied agency makes conversational AI feel consequential because speech changes a shared world.
- Impact: Game designers gain emergent companions but must expose reliable boundaries around perception, planning, and interruption.
- Watch next: Action-encoder release, cross-game adapters, multi-NPC tests, long-context stability, consumer hardware benchmarks.
