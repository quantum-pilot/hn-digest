# 486Tang – 486 on a credit-card-sized FPGA board

- Score: 134 | [HN](https://news.ycombinator.com/item?id=45232565) | Link: https://nand2mario.github.io/posts/2025/486tang_486_on_a_credit_card_size_fpga_board/

### TL;DR

The author ported the ao486 MiSTer PC core to Sipeed's Tang Console 138K FPGA, combining SDRAM main memory, a DDR3 framebuffer, and an SD-backed IDE interface. Verilator simulation, a Bochs debug port, and execution tracing helped diagnose DOS boot failures before hardware tests. Reset replication, fetch-path changes, and a four-way set-associative TLB reportedly improved Landmark 6 performance about 35%, reaching roughly 486SX-20 speed. Commenters mainly probed historically accurate memory behavior and retro-PC timing constraints.

### Comment pulse

- SDRAM is pragmatic, not period-authentic → the board's DDR3 interface and minimum speeds complicate faithful 486-era behavior.
- Faster replicas can expose old timing assumptions → commenters cited games and software tied to particular x86 speeds.

### LLM perspective

- View: Whole-system simulation turned an intricate retro-computing port into a sequence of observable engineering problems.
- Impact: FPGA hobbyists gain a compact x86 platform, while timing-sensitive compatibility remains a separate challenge.
- Watch next: Compare broader software compatibility and reproducible benchmarks against physical 486 systems and other FPGA implementations.
