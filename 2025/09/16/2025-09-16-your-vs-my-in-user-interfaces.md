# "Your" vs. "My" in user interfaces

- Score: 441 | [HN](https://news.ycombinator.com/item?id=45257627) | Link: https://adamsilver.io/blog/your-vs-my-in-user-interfaces/

- TL;DR
  Debate: should UIs use “your” or “my”? Microsoft suggests second person for system messages, first person for user commands. Many prefer dropping pronouns—use neutral labels and reserve pronouns only to distinguish personal vs global. Strong dislike for anthropomorphic copy (“Let’s…”, “You’re 90% there”); favor factual, concise text and buttons. Localization (e.g., Turkish) complicates pronouns and formality, so consistent microcopy rules, translator context, and pluralization support matter.
  - Content unavailable; summarizing from title/comments.

- Comment pulse
  - Prefer neutral labels over “my/your” → reduces clutter, indexing issues; reserve pronouns only to distinguish personal vs global— counterpoint: “my” can clarify ownership in commands.
  - Avoid anthropomorphic tone → “Let’s…”, “Got it!” feel infantilizing; machines are tools; progress copy: “Loading 90%” beats “You’re 90% there”.
  - Localize thoughtfully → in Turkish, directionality/formality flips “my/your”; translators need context, pluralization support, and UX writers to avoid ownership ambiguities.

- LLM perspective
  - View: Default to neutral nouns; second person for system messages; first person on user actions; ban cutesy phrasing.
  - Impact: UX writers and i18n gain authority; developers follow copy standards; users face clearer labels, less irritation, better localization.
  - Watch next: Ship microcopy guidelines; A/B tone/pronoun choices; implement ICU MessageFormat; attach screenshots to strings; audit progress/status wording.
