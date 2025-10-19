# The Unix Executable as a Smalltalk Method [pdf]

- Score: 134 | [HN](https://news.ycombinator.com/item?id=45623917) | Link: https://programmingmadecomplicated.wordpress.com/wp-content/uploads/2025/10/onward25-jakubovic.pdf

- TL;DR
    - The paper proposes a concrete Unix–Smalltalk unification: treat a Unix executable as a Smalltalk method, a process as its activation, and a directory as a generic object. Building “Smalltix” (apps made of many tiny executables/processes and object-directories) could bring Smalltalk’s defaults—persistence, dynamic updates, uniform representation, GUI openness—without a VM. The catch is process overhead; the author sketches workarounds. HN highlights prior art (PARC ports, NeXTSTEP), related work (Stephen Kell, liballocs), and renewed interest in malleable, component-based OS designs.

- Comment pulse
    - Builders want malleable, component OSes → Smalltalk/Lisp machines, Plan 9, exokernels, and Opal inspire projects like MallowOS and Etoile.
    - PARC-to-Unix history matters → Interlisp-D and Cedar ports, with NeXTSTEP/macOS as enduring Unix–PARC hybrids.
    - Resource pointers consolidate the thread → Stephen Kell’s talk/liballocs and SPLASH/ICFP recordings for deeper Unix–Smalltalk convergence.

- LLM perspective
    - View: Prototype Smalltix with ultra-light execs (clone3, vfork, unikernel-style) and object-as-directory via 9p/FUSE to validate ergonomics.
    - Impact: Standardized persistence/DSU across languages; IDEs/GUI toolkits align on object-directory conventions; simpler polyglot tooling.
    - Watch next: Microbenchmarks of exec-per-method; GUI addressability demos; compare against Squeak/GemStone and Plan 9 patterns.
