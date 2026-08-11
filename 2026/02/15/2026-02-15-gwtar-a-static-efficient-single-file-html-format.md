# Gwtar: A static efficient single-file HTML format

- Score: 159 | [HN](https://news.ycombinator.com/item?id=47024506) | Link: https://gwern.net/gwtar

### TL;DR

GWtar packages a complete web page into one static HTML file without forcing the browser to download every embedded asset up front. A small HTML, JavaScript, and JSON header stops normal loading before an appended tar archive; scripts then fetch byte ranges, create blobs, and rewrite asset references on demand. It works with ordinary web servers and can add image recompression, checksums, signatures, or recovery data. Its central limitation is local viewing: browser security rules prevent the same lazy-loading design from working directly through `file://`.

### Comment pulse

- Readers admired the `window.stop()` trick that keeps the appended archive from becoming part of the initial page load.
- Several questioned an archival format that cannot browse locally — counterpoint: the author prioritizes efficient HTTP delivery and provides a full-download fallback.
- Alternatives discussed included service workers and SingleFileZ, though both carry different compatibility or whole-archive download tradeoffs.
