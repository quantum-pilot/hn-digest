# I hate: Programming Wayland applications

- Score: 159 | [HN](https://news.ycombinator.com/item?id=47478298) | Link: https://www.p4m.dev/posts/29/index.html

### TL;DR
Wayland, successor to X11, is pleasant to use but miserable to program against directly, argues the author. Opening a trivial window demands hundreds of lines of callback-driven, object-oriented boilerplate, XML-generated protocol bindings, and compositor-specific extensions. Common tasks—input handling, software rendering, clipboard, monitor layouts, hotplugging, automation—are fragile, underspecified, or fragmented. Commenters split between blaming “pure” but impractical protocol design and noting that low-level display protocols are inherently verbose and should usually be hidden behind higher-level toolkits or libraries.

---

### Comment pulse
- Wayland's “pure” OO protocol → callback-heavy XML-described objects, fragmented extensions, and missing globals make trivial tasks like windows, input, automation absurdly hard — counterpoint: flexibility first.  
- Others: you never target Wayland/X11/Win32 directly → use GTK/Qt/SDL; complaining about raw protocol ergonomics misplaces responsibility.  
- Security-driven omissions (global window lists, remote control) → break tools like xdotool, force compositor-specific hacks, and still lack a common privileged interface.  

---

### LLM perspective
- View: Treat Wayland like Vulkan—only a target for libraries/toolkits; write a slim, blessed libwayland-gui to cover 90% use cases.  
- Impact: A standardized mid-level client API would stabilize automation, clipboard, window management semantics across compositors and finally let small apps escape X11.  
- Watch next: community proposals around “Wayland 2” features, portal unification, and cross-desktop agreements on automation and observability capabilities.
