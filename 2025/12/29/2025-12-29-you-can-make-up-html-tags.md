# You can make up HTML tags

- Score: 524 | [HN](https://news.ycombinator.com/item?id=46416945) | Link: https://maurycyz.com/misc/make-up-tags/

### TL;DR

Browsers allow authors to invent hyphenated HTML element names, style them directly, and later upgrade them through the Custom Elements API. Used carefully, names such as `main-article` can make nested markup easier to follow than repeated `div` elements and classes. HN clarified that hyphenated names are valid undefined custom elements, unlike arbitrary unhyphenated unknown tags, and emphasized caveats: prefer native semantic elements, explicitly choose display behavior, preserve expected attributes, and avoid creating a private vocabulary nobody else can read.

### Comment pulse

- Native semantics should come first → `article`, `header`, and `blockquote` often eliminate the supposed div soup without custom names.
- Custom tags suit component boundaries → extensive use obscures inline behavior, structure, and conventions for new contributors.
- Classes remain more composable → one element can carry multiple unordered roles, while nested element names impose hierarchy.

### LLM perspective

- View: Hyphenated elements are best treated as lightweight domain vocabulary, not substitutes for semantic HTML or every class.
- Impact: Small componentized pages gain readable structure, but teams must document styling, accessibility, and JavaScript upgrade expectations.
- Watch next: Test default behavior, hidden-state handling, accessibility trees, no-JavaScript rendering, and maintainability with unfamiliar contributors.
