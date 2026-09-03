# Paint.net 5.2 alpha now runs on Linux

- Score: 193 | [HN](https://news.ycombinator.com/item?id=49539389) | Link: https://forums.paint.net/topic/134562-paintnet-52-alpha-build-9739/

### TL;DR

Paint.NET’s developer announced that version 5.2 alpha build 9739 adds “extremely experimental” Wine/Linux support rather than a native Linux port. The build also moves to .NET 11 Preview, adopts composite crossgen compilation, changes elevation behavior, refreshes translations, and expands Mosaic tiling modes. Commenters welcome broader access but debate whether replacing Windows-specific APIs with cross-platform graphics and UI frameworks would be harder than maintaining Wine compatibility. Discussion also clarifies that Paint.NET has been closed source for many years and compares Pinta, Krita, and GIMP.

### Comment pulse

- Wine offers an incremental path → compatibility work can preserve a mature Windows codebase without replacing its UI and graphics stack.
- Native portability carries legacy cost → cross-platform frameworks may help new editors more than applications deeply tied to Windows APIs.
- Alternatives trade simplicity and openness → commenters describe Pinta as less polished, Krita as heavier, and GIMP as less intuitive.

### LLM perspective

- View: Experimental Wine support tests Linux demand cheaply before committing to a disruptive native architecture rewrite.
- Impact: Linux users may gain a familiar lightweight editor while retaining dependence on compatibility-layer behavior.
- Watch next: Track runtime stability, input and rendering bugs, plugin support, performance, installation friction, and maintainer commitment beyond alpha.
