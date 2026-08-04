# Decoding the obfuscated bash script on a Uniqlo t-shirt

- Score: 1269 | [HN](https://news.ycombinator.com/item?id=48829312) | Link: https://tris.sherliker.net/blog/obfuscated-self-evaluating-bash-script-by-cdn-akamai-being-supplied-to-consumers-via-retail-stores/

### TL;DR

An Akamai-designed Uniqlo “Peace for All” shirt prints a shebang and Base64 payload that decodes into a real Bash Easter egg. Triangulating Android, Tesseract, and Claude OCR output, the author recovered a script that hides the cursor and endlessly animates “PEACE FOR ALL” along a colored sine-wave path in the terminal. The shirt pipes decoded text into `eval`, resembling unsafe malware delivery despite its harmless message. A correction identifies Roboto Mono, though proportional-looking typesetting complicated transcription. HN traded shell jokes, compared OCR results, and disputed whether extraction was difficult.

### Comment pulse

- The payload is benign but the pattern is not → decoding arbitrary text directly into `eval` is exactly the execution chain defenders discourage.
- OCR difficulty was device-dependent → the author needed multi-engine reconciliation, while several readers reported near-perfect extraction from a single photo.
- Typography carried a second puzzle → Roboto Mono was set with apparent proportional spacing — counterpoint: some thought standard glyphs made recognition straightforward.

### LLM perspective

- **View:** The shirt succeeds as participatory design: executable code turns a campaign slogan into a decoding exercise and animated reward.
- **Impact:** It demonstrates both modern OCR capability and why opaque, self-evaluating shell payloads demand skepticism outside a controlled novelty context.
- **Watch next:** Preserve the source, document dependencies and terminal behavior, and compare OCR accuracy across crops, cameras, spacing, and models.
