# Why xor eax, eax?

- Score: 460 | [HN](https://news.ycombinator.com/item?id=46106556) | Link: https://xania.org/202512/01-xor-eax-eax

### TL;DR
Compilers often emit `xor eax, eax` instead of `mov eax, 0` to zero a register because it’s both shorter and faster on modern x86. The XOR form uses only 2 bytes vs. 5 for MOV, improving instruction-cache usage. CPUs additionally recognize `xor reg, reg` as a “zeroing idiom,” breaking dependency chains and often eliminating the actual execution, just renaming in a pre-zeroed physical register. Using the 32-bit form (`eax`) also implicitly clears the full 64-bit `rax`.

---

### Comment pulse
- Old 8‑bit and early x86 coders also used `xor reg,reg` for speed and size over `mov reg,0`—counterpoint: Pentium Pro actually preferred `mov` per Intel docs.  
- Shellcode writers favor `xor eax,eax` because its opcode contains no 0x00 bytes, unlike `mov eax,0`, avoiding premature string termination.  
- x86‑64 adds zero‑extension on 32‑bit writes and REX/REX2 prefixes; `xor eax,eax` saves a REX byte while still zeroing the full 64‑bit register.

---

### LLM perspective
- View: This illustrates how “weird” instruction choices encode deep microarchitectural knowledge, not premature optimization.  
- Impact: Matters for compiler authors, performance engineers, and low‑level security or game devs hand‑tuning hot paths.  
- Watch next: Benchmark zeroing idioms across APX/REX2-era CPUs and see if new encodings change best practices.
