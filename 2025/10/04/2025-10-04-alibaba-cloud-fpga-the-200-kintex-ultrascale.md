# Alibaba cloud FPGA: the $200 Kintex UltraScale+

- Score: 238 | [HN](https://news.ycombinator.com/item?id=45471136) | Link: https://essenceia.github.io/projects/alibaba_cloud_fpga/

- TL;DR
    - A hacker turns a $200 decommissioned Alibaba Cloud card into a usable Kintex UltraScale+ dev board. With no docs, they confirm liveness via a Raspberry Pi 5 PCIe link (enumerates as Gen2 x1), locate JTAG, and program by exporting SVF from Vivado WebPack and replaying it through OpenOCD using a J‑Link. They script SYSMON4 reads over JTAG for temps/voltages and, aided by a leaked pin map, identify clocks and I/O. HN highlights Pi-based PCIe bring‑up, FT2232H as a low‑cost programmer, and real‑world FPGA acceleration.

- Comment pulse
    - Pi 5 suits PCIe bring-up → cheap, runs desktop tools; RC-disable or partial reconfiguration enables reflash — counterpoint: Broadcom docs lacking; Intel NDA yields control.
    - FT2232H adapters serve as Vivado-compatible probes → flash FTDI EEPROM per UG908; versatile for GPIO/I2C/SPI with pyFTDI.
    - FPGA acceleration has precedent (Alibaba LSM, AWS Redshift AQA) → big latency/throughput wins but service longevity uncertain; hobbyists can repurpose surplus boards cheaply.

- LLM perspective
    - View: Open toolchain plus commodity probes makes decommissioned accelerator boards practical; custom JTAG scripting substitutes for vendor debug features.
    - Impact: Hobbyists and labs gain affordable KU3P-class PCIe/SFP hardware under WebPack; fewer proprietary probes, faster iteration.
    - Watch next: Publish pin map/XDC, automate SVF flow, validate PCIe/SFP throughput, compare FT2232H vs J‑Link reliability and max TCK.
