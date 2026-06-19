# Microsoft new Outlook takes 10 seconds to do what Outlook Classic does instantly

- Score: 587 | [HN](https://news.ycombinator.com/item?id=48584207) | Link: https://www.windowslatest.com/2026/06/15/microsofts-new-outlook-takes-10-seconds-to-do-what-outlook-classic-does-instantly-on-windows/

- TL;DR  
  Microsoft’s “new Outlook” for Windows, a WebView2-based wrapper around Outlook.com, now launches about as fast as Outlook Classic—but falls apart on notifications. Clicking a new‑mail toast takes ~10 seconds to display the specific message, versus essentially instant in Classic; bizarrely, manually opening Outlook and finding the mail yourself is faster. The article blames structural WebView2 overhead (many processes, 4× RAM, higher idle CPU) and argues these constraints are hard to fix without a future native/WinUI client, so Classic remains the better choice for now.

- Comment pulse  
  - Windows decay → Multiple users report abandoning Windows for Linux once UX and bloat crossed a threshold; Linux now “good enough” unless you need specific enterprise workflows.  
  - Web tech ≠ inherently slow → Fastmail and Outlook-on-the-web are snappy; the desktop wrapper’s load ordering and rendering strategy are what make new Outlook feel terrible.  
  - Corporate stack kills UX → Heavy EDR, app whitelisting, slow DNS, auto-updaters, and cheap hardware make even trivial apps (Outlook, Notepad) sluggish and frustrating.

- LLM perspective  
  - View: This is a textbook case of “platform unification” trumping interaction latency and offline robustness in a core productivity app.  
  - Impact: IT departments face rising support costs and user frustration; many power users quietly defect to web, Linux, or alternate clients.  
  - Watch next: Whether Microsoft actually delivers native WinUI replacements, and if enterprises push back hard enough to delay or avoid forced migration.
