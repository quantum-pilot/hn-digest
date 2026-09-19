# The scourge of x86 emulation

- Score: 274 | [HN](https://news.ycombinator.com/item?id=49750094) | Link: https://fex-emu.com/Scourge-of-emulation/

### TL;DR

FEX explains why translating x86 software to ARM is constrained by incompatible memory guarantees. ARM's LRCPC instructions improve ordinary x86 Total Store Ordering loads, and Apple's hardware TSO mode largely removes common overhead, but unaligned accesses, split-lock atomics, and write-combined GPU memory remain costly or imperfectly emulated. FEX reports up to 816× worse store bandwidth and sub-1-FPS games in a PCIe-GPU edge case. HN praised Apple's vertical integration while debating relaxed-memory benefits and noting that mixed native/emulated ARM64EC workloads complicate thread-wide TSO.

### Comment pulse

- Hardware support beats translator workarounds → Apple's TSO mode accelerates common accesses, while Qualcomm's coherent cachelines improve unaligned atomics within a cacheline.
- Important gaps remain → FEX's split-lock fallback can be slow and occasionally tear data; write-combined PCIe-GPU stores lack suitable TSO semantics.
- Thread-wide TSO has mixed-code costs → whole-process emulation contains the penalty, but ARM64EC may alternate frequently between native and translated execution.

### LLM perspective

- View: Compatibility depends on obscure architectural guarantees, so headline ARM performance cannot predict behavior for legacy multithreaded games.
- Impact: Emulator, kernel, CPU, and GPU-driver teams must coordinate; no software layer can efficiently reconstruct every missing atomic guarantee.
- Watch next: Cross-boundary CAS support, newer LRCPC extensions, vendor kernel patches, and benchmarks covering UMA versus PCIe graphics.
