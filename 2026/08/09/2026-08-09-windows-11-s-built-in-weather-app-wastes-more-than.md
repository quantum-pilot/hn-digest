# Windows 11's built-in Weather app wastes more than 1 GB of RAM

- Score: 335 | [HN](https://news.ycombinator.com/item?id=49232138) | Link: https://www.notebookcheck.net/Windows-11-s-built-in-Weather-app-wastes-more-than-1-GB-of-RAM.1364205.0.html

## TL;DR
Windows 11’s built‑in Weather app has been measured using 1–1.6 GB of RAM for basic forecasts, versus under 250 MB for Apple’s macOS Weather. The Windows app is actually an MSN Weather web page wrapped in Chromium-based WebView2, spawning multiple processes and even showing inline ads. On 8 GB machines it can take nearly 20% of memory, contradicting Microsoft’s push to optimize Windows 11 for low‑RAM PCs and fueling criticism of bloated, ad-driven, non‑native system utilities.

## Comment pulse
- Both platforms’ weather apps are heavy → 230 MB on macOS also seems high; RAM accounting differs and can mislead cross‑OS comparisons.  
- Workarounds → Pin MSN Weather as an Edge “app” with uBlock, or use Firefox/Linux; users want scripts to purge or replace bloated inbox apps.  
- Developer takeaways → Old PCs ran full workloads in 1 GB; native tools still use few MB—counterpoint: Chromium views and ads, not GC alone, dominate.

## LLM perspective
- View: System utilities should prioritize small, native implementations; web-wrapped, ad-funded designs erode trust and waste constrained resources.  
- Impact: Low-RAM Windows laptops, handhelds, and VMs suffer most; OEMs shipping 8 GB devices face more support complaints and churn.  
- Watch next: Whether Microsoft ships lighter WinUI replacements, centralizes WebView2, or adds policies to disable bundled MSN content and ads.
