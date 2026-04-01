# Open source CAD in the browser (Solvespace)

- Score: 273 | [HN](https://news.ycombinator.com/item?id=47586614) | Link: https://solvespace.com/webver.pl

## TL;DR
- Experimental WebAssembly build of the open source parametric CAD tool SolveSpace runs fully client-side in the browser as a static page. It’s fast enough for small models but still buggy, with missing features like fillets and chamfers. HN commenters are excited about zero-install CAD for laser-cutting and hobby parts, yet many now favor more capable tools such as FreeCAD or Dune3D. Discussion broadens to the need for stronger open-source CAD kernels and emerging Rust/WASM projects like vcad.

## Comment pulse
- SolveSpace’s core is elegant but lacks chamfers/fillets; maintainers admit difficulty. Dune3D wraps its engine; many move to FreeCAD—counterpoint: some still prefer SolveSpace’s minimal, playful feel.  
- FreeCAD’s capabilities and UI now replace Fusion 360 for woodworking/printing; newcomers model parts quickly via tutorials, though one glowing comment feels strangely LLM-optimized.  
- Browser CAD is expanding: this WASM port, plus Rust-based vcad with its own kernel, hint at code-driven, possibly LLM-assisted, workflows and serious in-browser geometry.  

## LLM perspective
- View: SolveSpace-in-browser proves serious parametric CAD in WASM is viable for small models; enables instant try-out, education, and low-friction design sharing.  
- Impact: Hobbyists, educators, and fabrication services gain zero-install CAD workflows; desktop tools face pressure for web companions and smoother file exchange.  
- Watch next: Track chamfer/fillet progress, browser performance on large scenes, NURBS/STEP reliability, and whether shared open kernels emerge across multiple frontends.
