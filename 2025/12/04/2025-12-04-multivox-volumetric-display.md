# Multivox: Volumetric Display

- Score: 204 | [HN](https://news.ycombinator.com/item?id=46149813) | Link: https://github.com/AncientJames/multivox

### TL;DR

Multivox is software for two Raspberry Pi 4-powered volumetric displays that spin paired HUB75 LED panels around a vertical axis. A rotation-synchronized driver scans a shared-memory voxel buffer, while client programs render games, models, point clouds, and demos. Rotovox favors vertical resolution and density; Vortex favors brightness and refresh rate, with printable Vortex parts available. The project includes hardware profiles, calibration tools, a launcher styled as a cartridge console, and an X11 simulator exposing the same voxel interface for development without the physical display.

### Comment pulse

- Viewers noted that lacking a known viewing position limits backface culling, making cutaway-style scenes especially suitable.
- Suggested uses included cockpit radar, while links highlighted contrasting static and physically touchable volumetric techniques.

### LLM perspective

- View: A shared voxel buffer cleanly separates timing-critical mechanics from experiments in volumetric content.
- Impact: The simulator lowers the development barrier even though reproducing the physical hardware remains specialized.
- Watch next: New content should exploit all-angle visibility instead of importing assumptions from conventional perspective displays.
