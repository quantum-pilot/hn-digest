# Hosting a website on an 8-bit microcontroller

- Score: 229 | [HN](https://news.ycombinator.com/item?id=48165295) | Link: https://maurycyz.com/projects/mcusite/

### TL;DR

A deliberately tiny project serves a webpage from an 8-bit AVR microcontroller mounted on perfboard; the captured article offers little implementation detail beyond the hardware and its live, visibly slow delivery. HN treated it as playful constraint engineering rather than a new category: embedded devices have long hosted web interfaces, and a 25-year-old ACE1101 implementation reportedly fit networking, bit-banged I²C, and UDP EEPROM uploads into under 1,024 bytes. Discussion also explored AVR peripherals, 10BASE-T Manchester timing, SLIP correctness, and the nostalgic effect of HTML streaming onscreen.

### Comment pulse

- Minimal web servers have deep precedent → commenters recalled an ACE1101 contest build and an artistic “webserver on a fly” from roughly 2000.

- Peripherals may outlive the architecture → AVR EB’s ADC, programmable gain, event system, and low-power operation remain compelling despite newer Cortex-M0+ alternatives.

- Slow delivery became part of the charm → viewers enjoyed watching HTML stream visibly, recalling dial-up pages and progressive image rendering.

### LLM perspective

- **View:** Constraints expose protocol fundamentals modern stacks conceal, turning memory, timing, framing, and omitted features into explicit design choices.

- **Impact:** Such experiments teach embedded networking and hardware limits, but production IoT already offers far easier integrated Ethernet.

- **Watch next:** Inspect source-size breakdowns, RAM use, throughput, concurrent connections, IPv6 behavior, SLIP errata compliance, and possible header compression.
