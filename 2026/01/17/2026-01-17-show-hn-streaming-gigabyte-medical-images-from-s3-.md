# Show HN: Streaming gigabyte medical images from S3 without downloading them

- Score: 131 | [HN](https://news.ycombinator.com/item?id=46656358) | Link: https://github.com/PABannier/WSIStreamer

### TL;DR

WSI Streamer is an MIT-licensed Rust tile server that displays 1–3GB-plus whole-slide pathology images directly from S3 or compatible storage. Native SVS and pyramidal-TIFF parsers locate requested tiles, issue HTTP range reads for only their bytes, encode JPEG responses, and supply an OpenSeadragon viewer; signed URLs and multi-level caches support deployment. Files must be tiled and pyramidal. HN connected the design to web maps, VirtualiZarr, climate data, mining imagery, and seekable archives, emphasizing a general pattern: read metadata first, then retrieve only addressed chunks from object storage.

### Comment pulse

- Range reads generalize beyond pathology → commenters cited scientific tensors, map tiles, core logs, model weights, and nested archives.
- Metadata-aware virtual stores could unify access → Zarr-style chunk references may bridge proprietary source files without copying them.
- Format fragmentation remains difficult → scanner vendors use SVS, NDPI, MRXS, and related layouts that require specialized parsers.

### LLM perspective

- View: The key product is format-aware byte addressing; the viewer is one useful interface over that capability.
- Impact: Pathology teams can inspect enormous slides sooner while avoiding full downloads and local storage duplication.
- Watch next: Independent latency and cache benchmarks, more scanner formats, access-control audits, and interoperability with Zarr or map clients.
