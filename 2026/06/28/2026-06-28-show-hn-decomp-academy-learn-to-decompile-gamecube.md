# Show HN: Decomp Academy – Learn to decompile GameCube games into matching C

- Score: 187 | [HN](https://news.ycombinator.com/item?id=48703412) | Link: https://decomp-academy.dev

### TL;DR

Decomp Academy is a browser-first, 267-lesson course that teaches beginners to turn GameCube and Game Boy Advance assembly into C with byte-identical compiler output. Its curriculum moves from registers and arithmetic through pointers, control flow, ABI details, optimization, and real Star Fox Adventures functions, with live grading by original compilers. HN praised removing fragile toolchain setup, but wanted a path from lessons into real project contributions and new-project bootstrapping. Discussion also highlighted function-by-function workflows and LLMs’ difficulty closing the final gap from plausible code to exact assembly.

### Comment pulse

- Browser delivery removes the largest onboarding cost → learners can experiment without installing old compilers, SDKs, linkers, or platform-specific patches.
- Byte equality is not source truth → alternative C, including fake matches, can reproduce target instructions without representing original intent.
- Exact matching exposes automation’s tail problem → AI may reach roughly 95%, then struggle with scheduling, compiler quirks, and source-shape details.

### LLM perspective

- **View:** The course turns reverse engineering from environment archaeology into deliberate practice with immediate, objective feedback.
- **Impact:** Preservation projects gain trained contributors; learners acquire assembly, ABI, optimization, and debugging intuition transferable beyond games.
- **Watch next:** Add project setup, authentic unmatched-function queues, anti-fake-match checks, and measurements of learner contributions to upstream decomps.
