# My audio interface has SSH enabled by default

- Score: 135 | [HN](https://news.ycombinator.com/item?id=47894747) | Link: https://hhh.hn/rodecaster-duo-fw/

### TL;DR

A Rodecaster Duo firmware update revealed an unusually open embedded Linux system: the image was a gzipped tarball protected only by an MD5 file, with no signature verification, and SSH was already listening over Ethernet with two unknown public keys authorized. By inspecting USB traffic, the author found single-character HID commands that expose the update disk and trigger flashing, then modified the archive to add his key and obtained a root shell. He reported the default SSH access to RØDE but received no response, while appreciating the device’s owner-modifiable design.

### Comment pulse

- Readers celebrated simple tarball updates and feared publicity might push RØDE toward locked firmware.
- Several said AI removes tedious packet-capture work — counterpoint: this lightly protected target never required elite exploitation skills.
- The original audio setup also drew interest: local mixing sends both microphones through one Discord client, preventing echo.

### LLM perspective

- Treat the bundled authorized keys as a security boundary requiring documented ownership, rotation, and removal controls.
- Preserve modifiability through an explicit developer mode rather than silent network access or universally trusted keys.
- Publish reproducible update tooling and recovery steps for both partitions before experimenting with custom images.
