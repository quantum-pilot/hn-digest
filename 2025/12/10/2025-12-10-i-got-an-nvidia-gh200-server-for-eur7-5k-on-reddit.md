# I got an Nvidia GH200 server for €7.5k on Reddit and converted it to a desktop

- Score: 159 | [HN](https://news.ycombinator.com/item?id=46222237) | Link: https://dnhkng.github.io/posts/hopper/

### TL;DR

David Noel Ng bought a dusty dual-GH200 prototype server for €7,500 and rebuilt it as an open-frame, water-cooled home system costing €8,930 overall. The machine combines two Grace CPUs, two H100-class GPUs, and a claimed 1,152 GB of fast-access memory. Conversion required custom copper adapters, four AIO coolers, disabling fan monitoring, repairing damaged surface-mount components after impossible temperature readings, and disabling NVLink so each GPU initialized over PCIe. Preliminary llama.cpp tests ran quantized models up to 235 billion parameters.

### Comment pulse

- Readers call it an extraordinary bargain → the seller’s hardware provenance and reason for the unfinished configuration remain unclear.
- Enterprise accelerators are poor gaming substitutes → missing display outputs, drivers, and workload tuning favor AI rather than consumer graphics.

### LLM perspective

- View: The value came from rare hardware and expert recovery work, not a repeatable consumer purchasing strategy.
- Impact: Skilled hobbyists can repurpose datacenter systems, accepting substantial cooling, firmware, safety, and support burdens.
- Watch next: Sustained thermals, power draw, reliability, NVLink restoration, and reproducible benchmarks will determine whether the conversion endures.
