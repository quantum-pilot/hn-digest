# Mysterious Intrigue Around an x86 "Corporate Entity Other Than Intel/AMD"

- Score: 149 | [HN](https://news.ycombinator.com/item?id=45608285) | Link: https://www.phoronix.com/news/x86-Opcodes-Not-AMD-Or-Intel

### TL;DR

x86 specialist Christian Ludloff asked Linux-kernel and Binutils developers to avoid several opcode encodings plus CPUID and MSR ranges that he says are actively used by an unnamed corporation other than Intel or AMD. The message supplies allocations but no processor, company, purpose, or licensing explanation. Phoronix notes Zhaoxin as one possibility yet questions why an established contributor would remain unnamed. Commenters proposed VIA-linked licensees or custom hyperscaler hardware, but the frozen material contains no evidence identifying the entity or confirming a new CPU implementation.

### Comment pulse

- Some readers connected the mystery to VIA and Cyrix licensing history; others guessed a hyperscaler receiving customized processors.
- A commenter wondered whether reserving encodings relates to kernel developers seeking a reliably undefined opcode for FineIBT.
- All proposed identities and purposes remained speculation.

### LLM perspective

- View: The actionable fact is an allocation-collision warning; the mystery-company narrative is inference layered onto a terse notice.
- Impact: Toolchain and kernel developers may need to preserve these encodings before their semantics become public.
- Watch next: Look for vendor patches, documentation, CPUID signatures, or licensing disclosures that independently identify the implementation.
