# ESP32-S31: Dual-Core RISC-V SoC with Wi-Fi 6, Bluetooth 5.4, and Advanced HMI

- Score: 200 | [HN](https://news.ycombinator.com/item?id=47561678) | Link: https://www.espressif.com/en/news/ESP32_S31_Release

### TL;DR

Espressif announced the upcoming ESP32-S31, a dual-core 320MHz 32-bit RISC-V SoC combining 2.4GHz Wi-Fi 6, Bluetooth 5.4 LE and Classic, IEEE 802.15.4 for Thread and Zigbee, and a gigabit Ethernet MAC. It adds 512KB SRAM, external DDR PSRAM support, a 128-bit SIMD path, camera/display/touch interfaces, multimedia accelerators, and hardware security including PUF keys, secure boot, encryption, and a TEE. Commenters welcomed the integrated connectivity but questioned naming, low-power behavior, and whether its advertised MMU provides true process isolation.

### Comment pulse

- The MMU may only map SPI flash and PSRAM, not implement Sv32 paging or page-fault isolation.
- Restored Bluetooth Classic plus LE Audio interests audio builders, contingent on credible low-power results.
- Some prefer a radio-free ESP32-P4 plus replaceable coprocessor; others value an integrated gigabit MAC and reclaimed GPIO.

### LLM perspective

- **View:** S31 prioritizes integration across radios, HMI, multimedia, and security more than maximal CPU or memory.
- **Impact:** Device makers can consolidate smart-display, audio, Matter, and wired-network designs around one SoC.
- **Watch next:** Samples, pricing, power benchmarks, ADC2 behavior, MMU documentation, Ethernet PHY requirements, and ESP-IDF maturity.
