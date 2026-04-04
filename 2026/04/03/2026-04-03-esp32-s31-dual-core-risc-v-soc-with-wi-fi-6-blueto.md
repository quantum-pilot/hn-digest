# ESP32-S31: Dual-Core RISC-V SoC with Wi-Fi 6, Bluetooth 5.4, and Advanced HMI

- Score: 200 | [HN](https://news.ycombinator.com/item?id=47561678) | Link: https://www.espressif.com/en/news/ESP32_S31_Release

- TL;DR  
    - Espressif’s ESP32‑S31 is a dual‑core 320 MHz RISC‑V SoC combining 2.4 GHz Wi‑Fi 6, Bluetooth 5.4 (LE + BR/EDR), IEEE 802.15.4, and GbE MAC, plus strong HMI (camera, LCD, touch), audio, and security (PUF, TEE, crypto) for smart appliances and hubs. It adds LE Audio and rich multimedia accelerators but lacks a full RISC‑V MMU, disappointing some hoping for process isolation. Commenters debate naming, low‑power Bluetooth audio viability, Ethernet/PoE support, and alternatives like pairing a P4 CPU with separate radios.

- Comment pulse  
    - Naming and architecture confusion → “S31” suggests S3 variant; MMU only covers SPI/PSRAM, so no standard RISC‑V paging or isolation — counterpoint: branding continuity.  
    - Wireless integration tradeoffs → BLE+BR/EDR and LE Audio please audio users, but some prefer decoupled P4 CPU plus C3 radio for flexibility and simpler certification.  
    - Ethernet expectations → Not first Ethernet‑capable ESP; S31’s GbE MAC and many GPIOs help, while commenters still want affordable PoE and single‑pair Ethernet boards.

- LLM perspective  
    - View: S31 targets “do‑everything” IoT hubs—radio, HMI, audio, and security—in one part, reducing BOM for midrange products.  
    - Impact: Benefits small OEMs most; fewer chips, mature ESP-IDF stack, and built‑in Matter/Thread simplify certification-heavy consumer devices.  
    - Watch next: Real-world power numbers, ADC2 behavior, radio coexistence benchmarks, and whether Espressif exposes enough low-level MMU features for tooling.
