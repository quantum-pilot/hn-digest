# Show HN: Moongate – Ultima Online server emulator in .NET 10 with Lua scripting

- Score: 216 | [HN](https://news.ycombinator.com/item?id=47275236) | Link: https://github.com/moongate-community/moongatev2

### TL;DR

Moongate v2 is an actively developed, GPL-licensed Ultima Online server built from scratch in C# on .NET 10. Its architecture emphasizes NativeAOT, source-generated registration, explicit packet and event boundaries, a deterministic game loop, sector-based world streaming, MessagePack snapshot-and-journal persistence, and Lua-driven commands and behavior. Login, movement, item interaction, scripting, HTTP administration, and basic pathfinding work today; combat, skills, richer NPCs, economy, housing, and broader protocol support remain incomplete. Commenters praised the solo scope and recalled UO’s unusually social, player-defined world.

### Comment pulse

- Fans miss UO’s commoner roles → crafting, trade, and unequal power made the world meaningful without requiring everyone to become a hero.
- The creator reused earlier infrastructure and imported ModernUO/POL data → Codex helped implement tests and the React frontend.
- An LLM-backed NPC proposal attracted interest → contextual dialogue might create rumors or events, though no implementation exists yet.
