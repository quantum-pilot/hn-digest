# Half-Life 2 running natively on HaikuOS

- Score: 249 | [HN](https://news.ycombinator.com/item?id=49034868) | Link: https://discuss.haiku-os.org/t/haiku-nvidia-porting-nvidia-driver-for-turing-gpus/16520?page=18

### TL;DR

A community demo shows Half-Life 2 running at 4K/60 fps on HaikuOS with an RTX 2080, using Haiku’s developing accelerated Nvidia driver and apparently the nillerusr Source-engine port. Current support covers Turing and Ampere firmware blobs, excluding newer cards such as RTX 5090; DisplayPort support is reportedly implemented but awaits a cleaned-up release, while HDMI/DisplayPort audio needs a driver workaround. HN readers celebrate the milestone and prolific contributor X512, but note the engine derives from leaked 2020 Source code and debate whether efficient ARM/Linux runs are more impressive.

### Comment pulse

- X512’s breadth earns admiration → commenters credit Nvidia acceleration alongside RISC-V, HDMI/DisplayPort audio, AMD Vulkan, and many other porting breakthroughs.
- The port’s provenance complicates celebration → nillerusr reportedly builds on leaked Source code; readers wish Valve would release Source or GoldSrc openly.
- Platform appeal remains subjective → BeOS veterans celebrate continued Haiku and ARM progress — counterpoint: others prefer Linux ergonomics or 5W ARM gaming.

### LLM perspective

- View: A demanding native game is a useful integration test for graphics, audio, input, compatibility, and system stability.
- Impact: Working acceleration can move Haiku from historical curiosity toward daily use on supported secondhand GPUs.
- Watch next: Track driver licensing, Source-code provenance, DisplayPort release, audio restoration, newer-GPU firmware, ARM support, and reproducible installation instructions.
