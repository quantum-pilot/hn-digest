# CharlotteOS – An Experimental Modern Operating System

- Score: 145 | [HN](https://news.ycombinator.com/item?id=45781397) | Link: https://github.com/charlotte-os/Catten

### TL;DR

CharlotteOS, also called Catten, is an early-stage experimental monolithic operating system written primarily in Rust with architecture-specific assembly. Its design borrows from exokernels, Plan 9, and Fuchsia, combining a low-level syscall layer with a type-safe URI-based namespace, granular capabilities, and persistent mandatory access controls. The project currently targets x86-64 and documents UEFI, ACPI, and hardware requirements. Its ambitions are substantial, but the supplied material presents a developing system rather than a production-ready alternative.

### Comment pulse

- Readers welcomed non-Linux experimentation but disputed whether a monolithic kernel and in-kernel graphics qualify as “modern.”
- Several questioned URI parsing complexity, driver isolation, security boundaries, and the practical cost of rebuilding kernel components.

### LLM perspective

- View: The project is most valuable as a testbed for namespace and capability ideas, not yet as an operating-system replacement.
- Impact: Early architectural choices will determine whether its convenience features preserve understandable security boundaries.
- Watch next: Look for working isolation demonstrations, driver lifecycle documentation, and measurements beyond the design claims.
