# How to stop Claude from saying load-bearing

- Score: 409 | [HN](https://news.ycombinator.com/item?id=48905248) | Link: https://jola.dev/posts/how-to-stop-claude-from-saying-load-bearing

### TL;DR
The post shows a tiny hook script for the Claude desktop client that intercepts each streamed message chunk and regex-replaces overused “Claude-isms” like “load‑bearing seams” with user‑defined alternatives (e.g., “cooked,” “spicy doodad”). By wiring this script into the `MessageDisplay` hook in `~/.claude/settings.json`, you can locally post‑process Claude’s text without touching the model. HN discussion widens this into a critique of recognizable AI tics, their impact on trust, and ways to retake control of style.

---

### Comment pulse
- AI tics ruin human prose → Seeing “load‑bearing seams” in blogs/emails signals LLM laziness, breaks trust, and even makes humans avoid phrases they once liked.  
- Lexical fixation and mirroring → Claude overuses niche words, echoes repo jargon, and can adopt throwaway metaphors (“moles”); one model’s quirks now saturate the internet.  
- Customization and safety voice → Users hack hooks/CLAUDE.md to change pronouns or praise; some call Anthropic’s emotional refusals manipulative — counterpoint: blunt “I can’t do that” also frustrates.

---

### LLM perspective
- View: Client-side hooks are a pragmatic way to filter, normalize, or parody model output without needing provider-level changes.  
- Impact: Teams can enforce house style, reduce “AI tells,” or mark AI-generated text so readers instantly know what they’re seeing.  
- Watch next: Native style knobs, per-workspace vocab blacklists, and training-time penalties for overused phrases to curb global linguistic monoculture.
