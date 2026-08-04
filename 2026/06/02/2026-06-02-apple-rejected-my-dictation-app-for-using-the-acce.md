# Apple rejected my dictation app for using the accessibility API

- Score: 286 | [HN](https://news.ycombinator.com/item?id=48369088) | Link: https://www.mitmllc.com/blog/apple-rejected-my-dictation-app/

### TL;DR

After a hand injury, Rene Zelaya built WhisperPad to transcribe speech locally and insert text at the cursor. Apple rejected a paid update because cross-app insertion used macOS’s broadly privileged Accessibility API, despite approving the same behavior earlier. Zelaya split the product: the App Store edition copies text for manual pasting, adding two steps, while the directly distributed edition preserves auto-paste. HN saw a genuine privacy risk but criticized inconsistent review and coarse permissions, debating whether granular capabilities or powerful accessibility control better serve disabled users.

### Comment pulse

- Granular permissions are the structural fix → apps could inject text without receiving screenshot, listening, pointer, and full-device control capabilities.
- Full accessibility control remains necessary → users without hand function need semantic access to buttons and text, not lossy vision-based workarounds.
- Platform openness divides users → Mac permits direct distribution, while iOS isolation protects cross-app privacy — counterpoint: it blocks capable dictation tools.

### LLM perspective

- **View:** The rejection exposes a mismatch between binary trust decisions and assistive workflows spanning multiple applications.
- **Impact:** Independent Mac distribution preserves functionality but shifts payments, updates, licensing, discovery, and trust onto small developers.
- **Watch next:** Apple appeal times, repeat-review consistency, and whether direct editions convert App Store discovery into sustainable sales.
