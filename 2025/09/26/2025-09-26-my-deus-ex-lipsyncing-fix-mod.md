# My Deus Ex lipsyncing fix mod

- Score: 259 | [HN](https://news.ycombinator.com/item?id=45382397) | Link: https://www.joewintergreen.com/my-deus-ex-lipsyncing-fix-mod-making-of/

- TL;DR
    - Joe Wintergreen’s Deus Ex mod restores believable lip-sync and blinking by fixing a flipped framerate check, lengthening blend “tweentime,” allowing end-of-line mouth closure blends, and slowing blinks. Smooth viseme transitions return, but perfect sync is impossible without source access: phonemes update irregularly from C++ code. He contrasts this with Valve’s offline phoneme tagging approach. HN discusses Deus Ex’s janky hit detection, applauds extensive community restorations, and doubts Aspyr’s remaster compared to fan projects.

- Comment pulse
    - DX combat collision is cylinder-based; headshots register only in cardinal octants, explaining misses and melee oddities — counterpoint: some mods claim fixes.
    - Community restorations are extensive: female JC voiceover, co-op, and polish; modders often outshine official efforts.
    - Aspyr’s remaster draws skepticism; many prefer fan-made Revision and note remasters’ mixed quality despite modern QoL.

- LLM perspective
    - View: Small script fixes can dramatically raise perceived quality, but engine-level phoneme cadence caps the ceiling.
    - Impact: Mod gives smoother dialogue across NPCs with negligible perf cost; a useful baseline for remasters and community patches.
    - Watch next: Measure phoneme update intervals; explore hooking the audio system; prototype offline phoneme tags appended to assets, HL2-style.
