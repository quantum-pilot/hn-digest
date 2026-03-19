# Death to Scroll Fade

- Score: 343 | [HN](https://news.ycombinator.com/item?id=47426932) | Link: https://dbushell.com/2026/01/09/death-to-scroll-fade/

- TL;DR  
  Bushell argues that “scroll fade” animations—elements fading/sliding into view as you scroll—are mostly a tacky, late-stage client request that hurts usability, accessibility, and performance. He calls out vestibular issues, cognitive overload, Core Web Vitals and SEO risks, and the fact that nobody budgets proper testing, so it’s not a “quick win” but a fragile architectural choice. Commenters broaden the rant to sticky headers, iOS/Safari scroll effects, and wish for default “reader mode” or truly static page rendering.

- Comment pulse  
  - Sticky headers that hide/show on scroll are loathed → they distract, obscure text, and resist ad-block removal—counterpoint: some prefer “reappear on scroll up” as compromise.  
  - Reader mode is baseline → people want clutter-free, static pages, even full-page prerendered images; current “Clown Mode” defaults persist to stop sites sabotaging reader mode.  
  - Some barely notice scroll fade, others say SaaS marketing sites and LLM-designed pages overuse it; one theory traces it to smoothing lazy-loading “blips” into animations.

- LLM perspective  
  - View: Treat motion like typography—intentional, sparse, and testable; default to no scroll-linked animation unless it clearly aids comprehension or orientation.  
  - Impact: Overuse of scroll effects harms accessibility and conversion on marketing sites, where stakeholders chase “pop” instead of measurable outcomes.  
  - Watch next: Browser-level “strict static” modes, richer motion preferences, and design systems that flag scroll-triggered animation as high-cost, opt-in components.
