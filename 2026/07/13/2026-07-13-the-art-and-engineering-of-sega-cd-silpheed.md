# The art and engineering of Sega CD Silpheed

- Score: 208 | [HN](https://news.ycombinator.com/item?id=48893639) | Link: https://fabiensanglard.net/silpheed/index.html

### TL;DR

Fabien Sanglard reverse-engineers how Silpheed made the Sega CD’s 12.5 MHz processor, 16-color display, and 150 KiB/s drive resemble real-time 3D. Rather than compress live-action footage, Game Arts designed flat-shaded scenes around the hardware: mostly 15 fps, self-contained frames, reusable solid-color tiles, ASIC-expanded two-color tiles, compact auto-incrementing tilemaps, double buffering, and palette cycling for lasers. At 16-bit, 16 kHz audio, video sometimes had only 8 KiB per frame. HN veterans remembered presentation so convincing that its simple shooter mechanics felt secondary.

### Comment pulse

- Constraints drove style → artists made aliasing, flat polygons, and limited palettes look intentional, outperforming live-action FMV squeezed into unsuitable hardware.
- Spectacle was the product → players recall fleet-scale debris and soundtrack impact more than depth, comparing gameplay to early arcade shooters.
- Audio routing deserved correction → Model 1’s expansion port lacked output pins, so the mixing cable routed stereo through Sega CD’s cleaner RCA path.

### LLM perspective

- **View:** Silpheed is an argument for co-design: codecs become better when art direction is shaped around the decoder’s cheapest operations.
- **Impact:** Modern constrained platforms can gain more from authoring rules and asset discipline than from increasingly complex general-purpose compression.
- **Watch next:** Release the generated analysis tools, verify cutscene variants, and quantify CPU, bandwidth, and palette costs per technique.
