# A new spam policy for “back button hijacking”

- Score: 818 | [HN](https://news.ycombinator.com/item?id=47760764) | Link: https://developers.google.com/search/blog/2026/04/back-button-hijacking

- TL;DR  
  Google is introducing a spam policy against “back button hijacking”: pages that manipulate browser history or redirects so users can’t easily return to search results or the previous site. Such behavior will now be treated as deceptive, potentially reducing visibility in Google Search and triggering browser-side protections. HN commenters welcome the move but argue browsers should also give users more control over keyboard shortcuts and history APIs, and note that dark patterns remain rampant in apps like LinkedIn, Reddit, TikTok, and Android clients.

- Comment pulse  
  Browser should own navigation and shortcuts → Sites hijack Ctrl+F, Ctrl+click, and Back, so users want opt‑in permissions or extensions (Vimium, user scripts) to override them.  
  Google Search quality feels worse → Pages mysteriously “visited, not indexed”; engagement-heavy content surfaces instead of niche docs—counterpoint: this policy targets Chrome/back behavior, not indexing rules directly.  
  Big platforms abuse history tricks → LinkedIn, Reddit, Facebook replace/push history so Back reloads feeds; users workaround by always opening links in new tabs and closing tabs instead of navigating back.

- LLM perspective  
  View → Formalizing this as “spam” aligns UX expectations: Back should always feel predictable, regardless of site implementation details.  
  Impact → Social networks, ad funnels, and some SPAs must audit history.pushState/redirect flows or risk demotion and user backlash.  
  Watch next → Look for Chrome/other browsers adding UI to skip “trapped” pages, devtools warnings, and Search Console reports flagging back-hijack patterns.
