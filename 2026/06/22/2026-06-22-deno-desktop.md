# Deno Desktop

- Score: 1009 | [HN](https://news.ycombinator.com/item?id=48626137) | Link: https://docs.deno.com/runtime/desktop/

### TL;DR
Deno Desktop is a new Deno 2.9 feature that turns TypeScript or existing SSR web apps (Next, SvelteKit, etc.) into cross‑platform desktop binaries. It bundles your code, Deno runtime, and either the OS webview or Chromium (CEF), offers in‑process bindings instead of IPC, cross‑compilation, and built‑in delta updates. HN commenters debate CEF sharing, versioning, and Google login blocks, discuss how Deno permissions should surface to end users, and broadly welcome another Electron/Tauri alternative.

### Comment pulse
- CEF sharing sounds great → Shared Chromium runtime shrinks binaries, but mismatches and Google blocking CEF logins worry devs — counterpoint: others favor evergreen CEF.  
- Desktop permissions feel unclear → Compile-time Deno rights bake into binaries; commenters want user-visible permission prompts, but note binaries can’t guarantee Deno-level sandbox integrity.  
- Backend mix excites devs → CEF plus webview and raw modes beat Tauri’s Linux story; some also want “open in browser” flow; overall Deno praise.  

### LLM perspective
- View: Bridges web and native by reusing Deno’s server strengths for desktop, lowering friction for JS-heavy teams.  
- Impact: Most useful for small to mid teams wanting one TypeScript codebase across browser, server, and desktop without deep native expertise.  
- Watch next: Watch binary size, startup time, Linux stability, permission sandboxing, and whether shared CEF plus auto-update work reliably in production apps.
