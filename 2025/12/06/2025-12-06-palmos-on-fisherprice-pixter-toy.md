# PalmOS on FisherPrice Pixter Toy

- Score: 184 | [HN](https://news.ycombinator.com/item?id=46170309) | Link: https://dmitry.gr/?r=05.Projects&proj=27.%20rePalm#pixter

## TL;DR
A hobbyist ports PalmOS 5 to Fisher-Price’s early‑2000s Pixter Color toy, whose 160×160 touchscreen and ARM7 SoC barely qualify as a PDA. The SoC is almost comically stripped-down: no cache, MMU, MPU, or alignment checking, so external RAM on the cartridge bus must be 8‑bit and wait‑state heavy. He stacks PSRAM chips with clever byte-lane wiring, adds flash, builds custom IrDA via a tiny MCU and quirky UART protocol, bit-bangs SD over GPIO, and polishes everything into a surprisingly usable, if slow, PalmOS handheld.

---

## Comment pulse
- Toy-side view → Former Fisher-Price intern recalls Pixter Color QA: UV-erasable EPROM carts, offshore devs, Walmart-dictated costs, and aggressive cost-cutting teardowns.  
- Perspective → Readers love the “two dead techs meet” energy: obsessive detail and passion make a niche, almost-unusable artifact compelling.  
- Economics → Comparison with Palm PDAs sparks speculation on how cheap PDAs could’ve been under toy-style cost pressure—counterpoint: this build still needed added RAM.

---

## LLM perspective
- View → This is reverse-engineering as craftsmanship: exploiting every marginal hardware quirk instead of throwing modern silicon at the problem.  
- Impact → Inspires hardware hackers and preservationists to re-evaluate “junk” toys as serious platforms once you understand their buses and constraints.  
- Watch next → More open ROMs, reusable tiny-MCU UART/IrDA bridges, and generalized carts could turn other forgotten toys into oddball retro-computers.
