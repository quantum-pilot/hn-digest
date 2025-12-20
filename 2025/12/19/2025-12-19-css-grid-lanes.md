# CSS Grid Lanes

- Score: 150 | [HN](https://news.ycombinator.com/item?id=46331586) | Link: https://webkit.org/blog/17660/introducing-css-grid-lanes/

## TL;DR
CSS Grid Lanes introduces `display: grid-lanes`, a native way to do masonry-style layouts using standard Grid tools (`grid-template-*`, spanning, explicit placement). You define columns or rows as “lanes,” and the browser packs items into the shortest lane, supporting both vertical “waterfall” and horizontal “brick” layouts. A new `item-tolerance` property controls how eagerly items switch lanes, trading off compactness vs predictable tab and screen-reader order. It’s in Safari Technology Preview; naming and flow-orientation details are still being finalized. HN is excited to drop JS hacks but divided on masonry UX.

## Comment pulse
- Native masonry in CSS → devs can avoid JS libraries like Masonry; Safari/WebKit praised for interop progress and delivering an experimental implementation first.  
- Lane layouts harm scanability → irregular “lines” make left‑to‑right reading and checking hard, increasing cognitive load and encouraging endless scrolling.— counterpoint: keyboard tab order improves.  
- Better as constraints? → some imagine general constraint solvers for layout; others note you can just append items and Grid Lanes repacks automatically on scroll.

## LLM perspective
- View: Grid Lanes smartly folds masonry into CSS Grid, but designers must resist overusing it where linear lists are clearer.  
- Impact: reduces custom JS, simplifies infinite-scroll galleries, news layouts, mega-menus, and improves baseline accessibility compared with ad‑hoc DOM reordering.  
- Watch next: cross‑browser implementation, property names and flow controls, plus DevTools and design-tool support for visualizing lane placement and tolerance.
