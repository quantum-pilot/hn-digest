# Why xor eax, eax?

- Score: 460 | [HN](https://news.ycombinator.com/item?id=46106556) | Link: https://xania.org/202512/01-xor-eax-eax

### TL;DR

On x86, `xor eax, eax` is a compact way to zero a register: its encoding takes two bytes, versus five for `mov eax, 0`, and writing `eax` also clears the upper half of `rax`. Modern processors recognize this zeroing idiom, break the prior register dependency, and can eliminate it from execution while it still retires normally. Commenters added historical examples from older architectures, noted that shellcode benefits from avoiding zero bytes, and emphasized that flag effects distinguish XOR from MOV.

### Comment pulse

- Encoding size matters beyond instruction count → fewer bytes reduce code footprint and instruction-cache pressure.
- Zeroing idioms receive special hardware treatment → dependency breaking makes XOR unlike a normal read-modify-write operation.
- Equivalent-looking instructions differ semantically → flags, legacy processors, and extended-register encodings can affect the choice.

### LLM perspective

- View: The idiom survives because one encoding aligns compactness, register semantics, and modern dependency handling.
- Impact: Compiler backends gain a cheap zero value without consuming ordinary execution resources on supported processors.
- Watch next: Check target microarchitecture, required flags, and code-size constraints before generalizing the optimization.
