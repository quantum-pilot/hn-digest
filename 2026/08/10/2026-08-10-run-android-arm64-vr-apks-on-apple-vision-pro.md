# Run Android ARM64 VR APKs on Apple Vision Pro

- Score: 166 | [HN](https://news.ycombinator.com/item?id=49238818) | Link: https://github.com/shinyquagsire23/Klepton

### TL;DR

Klepton translates Android ARM64 shared libraries into Apple-loadable Mach-O libraries, then supplies compatibility layers for Bionic, NDK, JNI, Oculus APIs, graphics, audio, input, and Vision Pro services. Most guest instructions remain unchanged; reserved-register uses are patched, GLES routes through ANGLE to Metal, and Vulkan through MoltenVK. The project currently targets Java-thin apps without ART or a JVM. Beat Saber runs on macOS and visionOS with minor graphical defects, while scripting runtimes may still require JIT and Steam VR Link support remains unfinished.

### Comment pulse

- Readers celebrated a rare Vision Pro tinkering project amid frustration with Apple’s platform restrictions.
- Technical discussion highlighted Darwin clearing register x18 on exception returns, validating Klepton’s patching strategy.
- Requests centered on screenshots and disclosure of LLM assistance.

### LLM perspective

- **View:** Preserving ARM64 instructions while translating ABIs and platform services is an elegant compatibility strategy.
- **Impact:** Existing standalone VR software could broaden Vision Pro’s limited native catalog without source ports.
- **Watch next:** Compatibility beyond Java-thin Unity apps, graphics fixes, build automation, and JIT-dependent runtimes.
