# Alibaba cloud FPGA: the $200 Kintex UltraScale+

- Score: 238 | [HN](https://news.ycombinator.com/item?id=45471136) | Link: https://essenceia.github.io/projects/alibaba_cloud_fpga/

### TL;DR

The author turned a $200 decommissioned Alibaba AS02MC04 accelerator into a usable Kintex UltraScale+ development board despite missing documentation. A Raspberry Pi 5 confirmed its surviving PCIe design; reverse engineering located JTAG, clocks, PCIe and SFP connections, while OpenOCD and an automated Vivado flow enabled configuration without an official Xilinx programmer. The resulting pinout and constraint information reportedly deliver at least fivefold savings over commercial alternatives. Later updates warn of faulty SFP modules, voltage corrections, hidden GPIO pads, and hardware modifications, so buyers inherit meaningful uncertainty.

### Comment pulse

- FPGA developers shared PCIe reconfiguration tricks, inexpensive FT2232H debugging adapters, and other secondhand accelerator boards.
- Readers highlighted open Corundum support and prior database acceleration as promising uses beyond basic experimentation.

### LLM perspective

- View: The bargain exists because the author converted undocumented hardware risk into reusable community documentation.
- Impact: Retired cloud accelerators can broaden access to capable FPGAs, but only for users comfortable with board-level investigation.
- Watch next: Seller variability, SFP condition, correct I/O voltages, and maintained constraint files determine whether savings persist.
