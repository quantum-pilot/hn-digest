# Java Hello World, LLVM Edition

- Score: 160 | [HN](https://news.ycombinator.com/item?id=46181076) | Link: https://www.javaadvent.com/2025/12/java-hello-world-llvm-edition.html

### TL;DR
- Java uses the new Foreign Function & Memory (FFM) API plus jextract-generated bindings to drive LLVM’s C API: building LLVM IR for a Hello World, printing it, then JIT-compiling and executing native x86 code entirely from Java without JNI. Along the way it explains MemorySegment, arenas, builders, globals, function types, and linking to libc’s puts. HN discussion focuses on FFM’s safety vs JNI and on installation trust issues and how this differs from GraalVM native image.

### Comment pulse
- FFM under --enable-native-access fits OpenJDK’s Integrity by Default: it can cause C-style UB but cannot freely violate Java module encapsulation like JNI.  
- Install script practice splits opinion: some see curl|sh as reckless RCE risk; others note you already trust the downloaded binary just as much.  
- GraalVM vs this demo: GraalVM AOT-compiles Java bytecode to binaries; FFM is a disciplined C-ABI bridge, like .NET’s DllImport, here driving LLVM.

### LLM perspective
- This pattern generalizes to dynamic plugin systems, DSL runtimes, or numerical kernels written in C/C++ and orchestrated from Java.  
- As FFM matures and JNI fades, Java shops can adopt safer native interop without rewriting existing C libraries or toolchains.  
- Benchmarks comparing FFM+LLVM JIT vs HotSpot and GraalVM, plus finer-grained native-access flags, will clarify when this approach is worthwhile.
