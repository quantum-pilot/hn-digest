# Meta's Omnilingual MT for 1,600 Languages

- Score: 112 | [HN](https://news.ycombinator.com/item?id=47421749) | Link: https://ai.meta.com/research/publications/omnilingual-mt-machine-translation-for-1600-languages/?_fb_noscript=1

## TL;DR
Meta’s Omnilingual MT (OMT) extends machine translation to 1,600 languages using two LLaMA3-based systems: a decoder-only model with retrieval-augmented translation and an encoder–decoder built on OmniSONAR embeddings. A large, curated data mix and new evaluation suites (BLASER 3, OmniTOX, BOUQuET, Met-BOUQuET) let 1–8B-parameter models match or beat a 70B LLM baseline, especially on low-resource languages. Hacker News readers welcome the ambition but question actual quality, data cleanliness, and whether the translation models themselves will be released.

## Comment pulse
- LLMs outperform mainstream MT for some low-resource languages → better context handling; users in Cambodia find Khmer LLM translations richer, though often overly formal/robotic.  
- Meta’s 1,600-language claim doesn’t ensure quality → commenters report weak results in Khmer and Chinese. — counterpoint: others see Facebook beating Google on Khmer posts.  
- Low-resource progress hinges on data, not just models → founders and researchers stress better mining and language ID; others ask whether Meta will release weights.

## LLM perspective
- View: Specializing modest LLaMA3 models for translation suggests domain-tuned 1–8B systems can outcompete giant general-purpose LLMs.  
- Impact: Stronger long-tail MT could empower education, public services, and local content moderation for speakers of hundreds of currently under-served languages.  
- Watch next: Independent benchmarks against Google, DeepL, Gemini, and open models, plus clarity on licensing and any production deployment inside Meta products.
