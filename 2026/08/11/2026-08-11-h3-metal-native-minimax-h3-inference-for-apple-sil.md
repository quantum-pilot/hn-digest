# H3-metal – Native MiniMax-H3 inference for Apple Silicon

- Score: 429 | [HN](https://news.ycombinator.com/item?id=49252179) | Link: https://github.com/antirez/h3.c

### TL;DR

h3-metal provides native MiniMax-H3 video-and-audio inference on Apple Silicon, including interactive prompting, first/last-frame conditioning, ordered media references, previews, and synchronized MP4 output. Its presets trade quality, time, and memory through fewer denoising passes or layers, reuse, token reduction, lower internal resolution, int8 Metal kernels, and optional SSD streaming. On M5 Max, successive int8 optimizations cut one fixed denoising test from 36.30 to 19.32 seconds; streaming reduced tracked DiT storage from about 36.5 GiB to roughly 2 GiB, with substantial slowdown.

### Comment pulse

- Mac users reported existing ComfyUI H3 renders taking over an hour, making a native minutes-scale path attractive.
- NVIDIA comparisons remained dramatically faster for diffusion — counterpoint: unified-memory Macs can run large models without discrete high-end GPUs.
- Readers clarified that tested end-to-end runs peaked near 40.1 GB, so 128 GB is not necessarily required.
