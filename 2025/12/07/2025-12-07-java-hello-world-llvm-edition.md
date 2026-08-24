# Java Hello World, LLVM Edition

- Score: 160 | [HN](https://news.ycombinator.com/item?id=46181076) | Link: https://www.javaadvent.com/2025/12/java-hello-world-llvm-edition.html

### TL;DR

A tutorial uses Java’s Foreign Function and Memory API, plus jextract-generated LLVM 20 bindings, to construct and run LLVM IR without JNI or handwritten C glue. Java builds a module containing main, a global message, and a libc puts call; the result first runs through LLVM’s interpreter, then through MCJIT for x86 Linux. A native function pointer becomes a Java MethodHandle and executes directly. Commenters distinguish this interoperability demo from GraalVM native images and debate native-access safeguards and the risk of executing downloaded installation scripts.

### Comment pulse

- FFM narrows native power versus JNI → it cannot inspect arbitrary private fields, though unsafe C behavior can still violate memory guarantees.
- GraalVM answers a different question → it compiles JVM bytecode ahead of time; FFM calls external C-ABI libraries from Java.
- Installer convenience divides readers → some reject fetched shell scripts; others note the installed executable ultimately receives comparable trust.

### LLM perspective

- View: The example demonstrates Java as a practical host for compiler construction and native libraries.
- Impact: Tool builders gain typed generated bindings and managed foreign-memory lifetimes without maintaining JNI glue.
- Watch next: More instructions, non-x86 targets, robust JIT error handling, and finer FFM-versus-JNI permissions.
