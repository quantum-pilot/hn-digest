# Why xor eax, eax?

- Score: 460 | [HN](https://news.ycombinator.com/item?id=46106556) | Link: https://xania.org/202512/01-xor-eax-eax

### TL;DR

Compilers often zero a register with `xor eax, eax` because its two-byte encoding is three bytes shorter than `mov eax, 0`. Modern out-of-order x86 processors also recognize this dependency-breaking idiom during renaming, supply a fresh zeroed physical register, and remove it from the execution queue, though it still retires. Writing EAX automatically clears RAX’s upper 32 bits, so the short form produces a full 64-bit zero. Discussion broadened the lesson across processor generations, security constraints, and architectural side effects.

### Comment pulse

- Shellcode gains another benefit → the self-XOR opcode contains no zero bytes, unlike loading an immediate zero into EAX.
- Historical CPUs complicate blanket advice → Z80 variants saved bytes and cycles, while Pentium Pro reportedly lacked the modern zero-idiom optimization.
- Flags distinguish equivalent-looking instructions → direct loads preserve them, whereas XOR updates condition flags and may deliberately establish known state.

### LLM perspective

- View: This tiny idiom succeeds because code density, dependency tracking, and architectural zero-extension align.
- Impact: Compiler writers save instruction-cache capacity and execution resources in one of the most frequent operations.
- Watch next: Microarchitecture-specific zero-idiom handling, APX encodings, flag dependencies, and cases where preserving flags requires a move.
