# Native all the way, until you need text

- Score: 374 | [HN](https://news.ycombinator.com/item?id=48168058) | Link: https://justsitandgrin.im/posts/native-all-the-way-until-you-need-text/

### TL;DR
An experienced macOS/iOS dev describes failing to build a smooth, selectable markdown chat view using SwiftUI, AppKit, and TextKit 2: selection limits, jittery scrolling, CPU spikes while streaming, and months of work to replicate basic system behaviors. WebKit, and then Electron, deliver better typography, streaming, and interactions almost immediately. HN discussion splits between those calling this a skill/framework-choice problem and those agreeing that Apple’s text stack lags modern web engines, making web views the pragmatic default.

### Comment pulse
- Native text is viable → commenters cite fast TextKit 2 editors and SwiftUI markdown libraries, dismissing OP as skill issue and demanding code as proof.  
- Large, streaming markdown surfaces remain hard → OP and others see jank, CPU spikes, beachballs; WebKit views handle complex tables/code blocks more smoothly.  
- Performance debate splits → some say browsers now rival SwiftUI, others show Qt/C++ apps vastly outpacing Electron—counterpoint: web engines are uniquely optimized for rich text.  

### LLM perspective
- View: Apple’s modern UI stack underinvests in rich-text primitives; developers naturally gravitate to web engines that encode decades of layout work.  
- Impact: Complex text-heavy apps will keep shipping as Electron/WebView hybrids, while SwiftUI becomes mostly a shell around embedded web content.  
- Watch next: Meaningful change needs Apple to unify TextKit, SwiftUI, and WebKit into a coherent, composable text system with first-class streaming support.
