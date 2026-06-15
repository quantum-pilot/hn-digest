# Phoenix LiveView 1.2

- Score: 200 | [HN](https://news.ycombinator.com/item?id=48524293) | Link: https://phoenixframework.org/blog/phoenix-liveview-1-2-released

## TL;DR
Phoenix LiveView 1.2 adds colocated CSS to HEEx templates, mirroring colocated JS: styles are extracted at compile time and wired into your existing bundler. Component-local styling is enabled via configurable root-tag attributes and optional `@scope`-based or custom scoping strategies, built on a revamped HEEx compilation pipeline (tokenization + parsing). Smaller improvements include pluggable formatting for `<style>/<script>`, smoother `Phoenix.LiveView.JS` encoding, more granular debug/test configuration, and dedicated JS client docs. HN commenters laud LiveView’s server-driven SPA model and fit with LLM-assisted development over heavier JS stacks.

## Comment pulse
- LiveView is viewed as productive and “chill” → devs report shipping production apps and even Etsy-like clones comfortably, leveraging BEAM reliability and Phoenix batteries-included design.  
- Elixir/Phoenix pair well with LLM coding → functional style and compilation feedback help models iterate; teams claim higher throughput and fewer errors than Python/Django stacks.  
- Server-driven SPAs seen as fast/simple for modest apps → critics ask why some sites aren’t static HTML. — counterpoint: highly-interactive UIs still justify richer frontends.  

## LLM perspective
- View: Colocated CSS plus refined HEEx compilation pushes Phoenix further toward component-centric ergonomics, competing with React-style DX while staying server-first.  
- Impact: Frameworks offering server-rendered interactivity will attract teams tired of JS complexity, especially where SEO, latency, and ops simplicity matter most.  
- Watch next: Watch browser adoption of CSS @scope and community scoping behaviours; standardized support could make component-local styling the default in Phoenix.
