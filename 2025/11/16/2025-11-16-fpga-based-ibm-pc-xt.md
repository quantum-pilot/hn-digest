# FPGA Based IBM-PC-XT

- Score: 129 | [HN](https://news.ycombinator.com/item?id=45945784) | Link: https://bit-hack.net/2025/11/10/fpga-based-ibm-pc-xt/

### TL;DR

A hobbyist recreated an IBM PC/XT-style system around a real NEC V20 processor and SRAM, using an FPGA for bus control, graphics, storage, peripherals, and glue logic. The design boots an XT BIOS, maps an SD card through a custom INT 13h option ROM, translates PS/2 mouse events into a serial-like interface, and reproduces AdLib audio with an open YM3812 core plus authentic DAC. Commenters praised its hybrid authenticity, especially emulated disk sounds, while clarifying that it is not an entirely FPGA-implemented PC.

### Comment pulse

- Hybrid hardware made the project distinctive → real CPU, memory, and DAC parts interact with FPGA-implemented chipset functions.
- Simulated drive noises mattered emotionally → silent SD storage otherwise removes a memorable part of vintage computing.
- Separate SRAM favored tractability → the author chose a simple interface over learning a DRAM controller during the build.

### LLM perspective

- View: The build treats authenticity as selected interfaces and sensations, not literal component-for-component reproduction.
- Impact: Open schematics and gateware give hobbyists a practical bridge between retro hardware and modern programmable logic.
- Watch next: Explore higher V20 clocks, SDRAM integration, compatibility testing, and preservation use with original storage devices.
