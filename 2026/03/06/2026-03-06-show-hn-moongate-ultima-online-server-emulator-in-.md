# Show HN: Moongate – Ultima Online server emulator in .NET 10 with Lua scripting

- Score: 216 | [HN](https://news.ycombinator.com/item?id=47275236) | Link: https://github.com/moongate-community/moongatev2

## TL;DR

Moongate v2 is a modern, from-scratch Ultima Online server emulator written in C# on .NET 10 with NativeAOT support, Lua scripting, and heavy use of source generators instead of reflection. It features a timestamp-driven game loop, sector-based world streaming, MessagePack snapshot+journal persistence, HTTP admin/metrics, Docker images, and a data-driven template system for items/mobs/UI. Core login/movement/items/chat are working; combat, skills, and full AI are still in progress. The author is actively seeking contributors and technical reviewers.

## Comment pulse

- UO’s magic was social hierarchy and “commoner” roles → sandbox economy, real status gaps, fun without best gear—counterpoint: later MMOs briefly had similar inequality via hardcore raiding.  
- Engineering effort impresses people → largely one developer leveraging earlier Moongate attempts, prior Lua engine work, and data imports from ModernUO/POL, plus AI-assisted tests and frontend.  
- Several veterans reminisce about UO emulators like UOX3 and propose LLM-powered NPCs → Lua bridge could drive dynamic dialog, quests, even world changes from conversations.

## LLM perspective

- View: Cleanly separated networking, domain events, and Lua scripting make this a rare “modern MMO emulator” architecture, not just a nostalgia hack.  
- Impact: UO shard admins, .NET game developers, and emulator authors gain a performant reference for AOT-friendly, scriptable server design.  
- Watch next: Completion of combat/skills, real-world shard deployments, and experiments integrating constrained LLM NPCs through the existing Lua/event system.
