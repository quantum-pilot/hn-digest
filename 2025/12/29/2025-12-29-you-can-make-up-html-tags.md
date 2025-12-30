# You can make up HTML tags

- Score: 524 | [HN](https://news.ycombinator.com/item?id=46416945) | Link: https://maurycyz.com/misc/make-up-tags/

- TL;DR  
  HTML lets you invent tags like `<cool-thing>`; browsers treat them as generic elements that you can fully style with CSS. Using hyphenated names avoids collisions with future HTML elements. The article suggests these custom tags can reduce “div soup” and make nested structures easier to read. HN commenters clarify the difference between unknown elements and proper custom elements, stress using native semantic tags first, and share mixed experiences about readability, semantics, and Web Components vs JavaScript frameworks.

- Comment pulse  
  - Custom elements with a dash are valid HTMLElements; bare `<tagname>` becomes HTMLUnknownElement. You must define display and behaviors; browser defaults don’t apply automatically.  
  - Many prefer semantic tags over custom ones; “div soup” is usually avoidable, and classes encode multiple meanings — counterpoint: custom tags can clarify tricky nesting.  
  - Practitioners report success using a few component-like custom tags (`<x-card>`, `<yes-script>`) while keeping most markup native; overuse hurts readability and onboarding.

- LLM perspective  
  - View: Treat hyphenated custom tags as lightweight, semantic-ish building blocks, but reserve them for components, not wholesale HTML replacement.  
  - Impact: Clean component tags plus classes can simplify design systems in static sites, CMS templates, and framework-free projects.  
  - Watch next: Linters, validators, and accessibility tools that understand project-specific tag vocabularies without requiring full Web Components registration.
