# Dissecting the Apple M1 GPU, the end

- Score: 845 | [HN](https://news.ycombinator.com/item?id=45034537) | Link: https://rosenzweig.io/blog/asahi-gpu-part-n.html

### TL;DR

Alyssa Rosenzweig closes a five-year M1 GPU reverse-engineering chapter after helping make accelerated Linux practical on Apple silicon. Starting with shader experiments and a triangle, the work grew into upstream Mesa drivers with conformant OpenGL 4.6, OpenGL ES 3.2, OpenCL 3.0, Vulkan 1.4, and Direct3D 12 support through Proton. With those goals met and others continuing Asahi development, she is moving to another graphics challenge. Commenters celebrated the rare combination of technical depth, persistence, upstreaming, and usable results.

### Comment pulse

- The achievement exceeds a demo → conformance, upstream drivers, and Proton turned undocumented hardware into a maintained platform.
- Community continuity matters → Rosenzweig is departing Apple work, but Asahi contributors will carry the stack forward.

### LLM perspective

- View: The decisive accomplishment is converting reverse engineering into standards-conformant infrastructure others can maintain.
- Impact: Apple-silicon Linux users gain durable graphics support, while related Vulkan-on-Apple efforts inherit proven work.
- Watch next: Follow performance maintenance, newer-chip support, Proton compatibility, and Rosenzweig’s next open-source graphics target.
