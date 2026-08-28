# We found a division by zero bug in FFmpeg with a vibecoded fuzzer

- Score: 228 | [HN](https://news.ycombinator.com/item?id=49468642) | Link: https://code.ffmpeg.org/FFmpeg/FFmpeg/issues/24290

### TL;DR

A fuzzer-generated malformed VPK input reportedly reaches FFmpeg’s `vpk_read_packet` with a zero audio-channel count, causing integer division by zero and a deterministic SIGFPE crash. The reporter rates it a medium-severity denial of service affecting applications that automatically open untrusted VPK data, while finding no adjacent memory corruption or direct code-execution primitive. A proposed guard would return invalid-data instead. An FFmpeg member linked the report to a 2024 discussion, and commenters identified an April patch that was submitted but apparently not merged.

### Comment pulse

- Commenters valued cheap automated bug hunts but stressed that human review and integration remain the difficult work.
- Static warnings for every division would create excessive false positives; fuzzing demonstrates a concrete triggering input.
- Some considered the crash minor, while others argued malformed media should never terminate host applications.

### LLM perspective

- View: The discovery is useful, but its novelty is weaker because maintainers had already discussed the defect.
- Impact: A small validation gap can crash every downstream application sharing the vulnerable demuxer path.
- Watch next: Track patch merging, add regression coverage, and test whether ordinary file paths reproduce the custom-AVIO trigger.
