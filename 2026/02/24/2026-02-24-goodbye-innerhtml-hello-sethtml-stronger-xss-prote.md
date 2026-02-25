# Goodbye InnerHTML, Hello SetHTML: Stronger XSS Protection in Firefox 148

- Score: 325 | [HN](https://news.ycombinator.com/item?id=47136611) | Link: https://hacks.mozilla.org/2026/02/goodbye-innerhtml-hello-sethtml-stronger-xss-protection-in-firefox-148/

## TL;DR
Firefox 148 ships the standardized Sanitizer API and `Element.setHTML()`, which sanitizes untrusted HTML in the browser before it hits the DOM, aiming to prevent XSS by default. It’s intended as a mostly drop-in, configurable successor to `innerHTML`, and combines well with Trusted Types and CSP for stronger defense-in-depth. HN discussion is positive about native XSS hardening, but flags confusing safe/unsafe APIs, non-script abuse (markup/CSS), limited browser support, and the danger of over-trusting sanitization.

## Comment pulse
- Sanitizer and `setHTML` blur safe/unsafe boundaries → developers may misidentify dangerous calls; critics argue HTML sanitization is unsolvable and prefer stricter deprecation/Trusted Types.  
- Limited browser support limits immediate adoption; production apps must feature-detect or polyfill, reducing the security advantages of a native, standardized sanitizer.  
- API blocks script execution but can allow disruptive markup/CSS; skeptics see footguns, supporters emphasize strict allowlists and backend escaping as layered defense.

## LLM perspective
- View: Treat `setHTML` as safer `innerHTML`, not a substitute for contextual encoding; reserve it for controlled rich-text features.  
- Impact: Biggest beneficiaries are medium-sized teams lacking dedicated security experts; they gain a default XSS barrier without rewriting templating systems.  
- Watch next: Track Chrome/Safari adoption, framework wrappers around `setHTML`, and real-world audits comparing Sanitizer-based defenses to existing library and CSP approaches.
