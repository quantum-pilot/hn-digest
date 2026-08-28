# Making Minecraft Spherical

- Score: 900 | [HN](https://news.ycombinator.com/item?id=45055205) | Link: https://www.bowerbyte.com/posts/blocky-planet/

### TL;DR

Blocky Planet is a Unity 6 voxel demo that maps destructible, Minecraft-like terrain onto a sphere. Its quad-sphere surface reduces projection distortion, while concentric shells periodically quadruple block counts to balance width consistency against aligned seams. The world is organized into sectors, shells, and fixed 16³ chunks; crossing shell and sector boundaries makes neighbors and pasted structures unusually complex. Custom radial gravity, three-dimensional noise, and latitude-based biomes complete the prototype, though its core remains hollow and boundary structures can visibly deform.

### Comment pulse

- Readers compared the approach with Space Engineers, Eco, and spherical Minecraft shaders.
- Several preferred limiting excavation depth, while others considered reaching a zero-gravity core essential fun.

### LLM perspective

- View: The demo succeeds by making geometric compromises explicit rather than hiding unavoidable distortion.
- Impact: Its address and neighbor model offers a practical blueprint for spherical voxel experiments.
- Watch next: Test edge cases at sector corners, shell transitions, and the currently unsupported inner core.
