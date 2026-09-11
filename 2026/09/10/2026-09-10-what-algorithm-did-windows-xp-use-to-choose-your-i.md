# What algorithm did Windows XP use to choose your initial user picture?

- Score: 351 | [HN](https://news.ycombinator.com/item?id=49640646) | Link: https://devblogs.microsoft.com/oldnewthing/20260909-00/?p=112683

### TL;DR

Windows XP selected an account’s initial picture with a one-pass form of reservoir sampling. It seeded RtlRandomEx from GetTickCount, then gave each newly encountered file a one-in-current-count chance to replace the existing winner, producing an equal final probability without counting or traversing the directory twice. The implementation stopped after 100 pictures to bound pathological directories. Commenters admire the algorithm’s elegance and filesystem awareness, while debating whether such optimization mattered for a tiny default-picture set and reflecting on how constraints shape programming discipline.

### Comment pulse

- Reservoir sampling avoids a second filesystem pass → it selects uniformly from an iterator without knowing its size in advance.
- The optimization may exceed the feature’s needs → default-picture directories are small, making a naïve approach arguably sufficient.
- Historical hardware rewarded careful I/O → commenters recall disk seeks being audible and visibly slow on older systems.

### LLM perspective

- View: The example shows how modest features can encode robust handling of mutation, unknown size, and pathological input.
- Impact: Engineers gain a memorable pattern for uniform streaming selection when materializing or recounting data is undesirable.
- Watch next: Verify seeding quality and enumeration behavior if adapting the pattern for security-sensitive or concurrent systems.
