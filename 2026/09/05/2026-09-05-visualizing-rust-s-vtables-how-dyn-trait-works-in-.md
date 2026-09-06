# Visualizing Rust's Vtables: How dyn Trait Works In Memory

- Score: 167 | [HN](https://news.ycombinator.com/item?id=49576343) | Link: https://sofiabelen.github.io/projects/visualizing-rusts-vtables-how-dyn-trait-works-in-memory/

### TL;DR

The tutorial contrasts Rust’s static and dynamic polymorphism. Generic trait bounds use monomorphization, generating type-specific code without runtime dispatch but increasing code size. A `dyn Trait` reference is a fat pointer containing a data pointer and vtable pointer; the vtable supports dispatch and carries metadata such as size and alignment. Unlike C++, Rust places no vtable pointer inside every object. Commenters clarify that “dyn compatibility” replaced “object safety,” dispute some C++ comparisons, and note that vtable identity is not necessarily unique.

### Comment pulse

- Terminology matters → current Rust calls the rules “dyn compatibility,” directly describing whether `dyn Trait` is permitted.
- Unified traits divide opinion → supporters value choosing dispatch at use sites; critics prefer separate static and dynamic mechanisms.
- Vtables contain subtleties → duplicate tables can make fat-pointer identity surprising, and metadata extends beyond method addresses.

### LLM perspective

- View: Memory diagrams make dispatch concrete, but language comparisons should separate guarantees from common implementations.
- Impact: Rust developers can choose code-size versus runtime-dispatch costs explicitly without changing underlying types.
- Watch next: Verify layouts experimentally across compiler versions and extend the analysis to vtable metadata and pointer equality.
