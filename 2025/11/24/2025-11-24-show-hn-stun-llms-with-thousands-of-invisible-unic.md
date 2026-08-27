# Show HN: Stun LLMs with thousands of invisible Unicode characters

- Score: 183 | [HN](https://news.ycombinator.com/item?id=46029889) | Link: https://gibberifier.com

### TL;DR

Gibberifier inserts thousands of zero-width Unicode characters into visible text, claiming to confuse language models, frustrate scraping, and consume tokens while preserving human appearance. User tests undermine any durable protection: several models decoded short examples, screenshots bypass the trick, and filtering the characters is straightforward. Longer payloads sometimes caused errors or irrelevant answers, apparently interacting with safety defenses. The strongest demonstrated effect is negative: screen readers can render the transformed text almost unintelligible, creating a serious accessibility failure.

### Comment pulse

- Obfuscation is easily normalized → removing zero-width code points or using OCR restores the visible text.
- Model behavior varies by length and interface → failures look inconsistent rather than a dependable anti-scraping boundary.
- Accessibility bears the cost → screen readers vocalize or stumble over characters invisible to sighted readers.

### LLM perspective

- View: This is an adversarial formatting curiosity, not meaningful control over copying or model ingestion.
- Impact: Publishers adopting it could exclude assistive-technology users while imposing only a temporary preprocessing hurdle.
- Watch next: Test normalization pipelines, tokenizers, screen readers, copy-paste behavior, and false positives on legitimate Unicode.
