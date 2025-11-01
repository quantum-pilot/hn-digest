# Minecraft removing obfuscation in Java Edition

- Score: 989 | [HN](https://news.ycombinator.com/item?id=45748879) | Link: https://www.minecraft.net/en-us/article/removing-obfuscation-in-java-edition

- TL;DR
  - Mojang will stop obfuscating Minecraft: Java Edition after the Mounts of Mayhem release, shipping jars with original class/field/method/variable names. Transitional snapshots will include both obfuscated and clear builds so mod tools can adapt. Expect no EULA change, a LICENSE inside jars, and removal of mapping files in version metadata. HN cheers easier modding, debugging, and readable crash logs; notes the community’s decade of decompilation; raises mod security/sandbox worries; and rekindles debate over open-sourcing versus legal/business constraints.

- Comment pulse
  - Huge win for modders → Removes ProGuard name-mangling; crash logs and APIs readable; ends decade-long deobfuscate–reobfuscate toolchains.
  - Security worries → Mods often from sketchy sites, no sandbox; full system access risks persist — counterpoint: easier audits when names are intact.
  - Open-sourcing debate → Some want a Doom-like engine release; others cite legal/IP entanglements, legacy tooling, and little commercial upside.

- LLM perspective
  - View: Dropping obfuscation formalizes what decompilers already revealed and aligns Mojang with its mod-centric identity.
  - Impact: Mod loaders (Forge, Fabric, Quilt) must adapt; documentation and crash triage speed up; reverse-engineering talent barrier drops.
  - Watch next: Timeline for full cutover; security posture (signing, sandboxing); any movement toward stable public APIs or open-sourcing.
