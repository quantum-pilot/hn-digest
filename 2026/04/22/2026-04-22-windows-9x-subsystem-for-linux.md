# Windows 9x Subsystem for Linux

- Score: 871 | [HN](https://news.ycombinator.com/item?id=47861270) | Link: https://social.hails.org/@hailey/116446826733136456

- TL;DR  
WSL9x is a wild retro-hack: a modern Linux kernel running cooperatively in ring 0 under Windows 95/98/ME, no hardware virtualization, so it even works on a 486. Linux and Win9x apps run side‑by‑side, similar in spirit to coLinux but targeting the pre‑NT Windows line. HN discussion compares it to coLinux, flinux, Cygwin, WSL1/2, unpacks how Win9x’s thin kernel leaves room for Linux to “be the OS”, and praises the painstaking, non‑AI craftsmanship.

- Comment pulse  
  - Early Windows–Linux coexistence → coLinux/flinux side-loading kernels, Cygwin/MSYS2 POSIX layer; Cygwin gave native binaries but caused DLL hell, hacks like fake fork(), performance issues.  
  - How this works → Win9x barely used CPU protection; Linux kernel can grab ring‑0, memory management, run alongside, talking to Windows via VMM driver APIs.  
  - Hacker appeal → six‑year solo deep dive into obscure Win9x internals, README stresses “written without AI”, contrasted with 20‑minute promptware Show HN projects.

- LLM perspective  
  - View: Showcases value of understanding old platforms deeply instead of discarding them; retro systems become experimental sandboxes for new OS ideas.  
  - Impact: Inspires low-level developers, retrocomputing fans, and toolchain authors to revisit cooperative-kernel approaches instead of heavyweight virtualization for niche use cases.  
  - Watch next: Useful follow‑ups: performance benchmarks vs coLinux/WSL1, documentation of Win9x driver tricks, and ports to other non‑NT or embedded Windows variants.
