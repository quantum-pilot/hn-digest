# Spaghettifying DRAM

- Score: 484 | [HN](https://news.ycombinator.com/item?id=49286341) | Link: https://github.com/xoreaxeaxeax/skitter-creek-bath-salts

### TL;DR

On AMD Family 16h processors, a writable DRAM-controller swizzle bit can temporarily remap physical addresses to different DRAM cells, bypassing protections expressed only in the normal address view. The tool keeps the machine alive through cache, TLB, interrupt, and multicore preparation, collects sentinel alias pairs, then uses Z3 to reconstruct the controller’s linear transform. It can read or write PSP memory, SMRAM, C6-saved CPU state, and a stashed microcode patch. Commenters praised the work but stressed that applicability to newer CPUs remains unproven.

### Comment pulse

- Later AMD documentation omits translation details; commenters expect modern firmware may lock registers, while Zen uses a different controller.
- Console implications are uncertain because modern systems may encrypt external DRAM or deny guest code the necessary hardware access.
- Increasingly complex DRAM initialization and proprietary blobs create broad attack surface, even when specific exploits remain difficult.

### LLM perspective

- View: Memory isolation fails when mutable translation sits beneath every component’s shared physical-address assumptions.
- Impact: Ring-0 access on affected hardware can cross firmware boundaries previously treated as stronger trust zones.
- Watch next: The Black Hat talk, tests beyond Family 16h, vendor lock confirmation, and integrity protections tied to memory translation.
