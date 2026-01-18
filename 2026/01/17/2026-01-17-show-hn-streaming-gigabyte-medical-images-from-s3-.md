# Show HN: Streaming gigabyte medical images from S3 without downloading them

- Score: 131 | [HN](https://news.ycombinator.com/item?id=46656358) | Link: https://github.com/PABannier/WSIStreamer

### TL;DR
WSIStreamer is an open‑source Rust tile server for whole‑slide pathology images (multi‑GB SVS/pyramidal TIFF) stored in S3‑compatible object storage. Instead of downloading full slides, it understands the image layout and uses HTTP range requests to fetch only the bytes for requested tiles, serving them via a built‑in OpenSeadragon viewer or a simple HTTP API. Hacker News discussion connects this pattern to broader work on cloud‑optimized multidimensional array formats (Zarr/Icechunk), DICOM WSI, web maps, and even ML model weights streaming.

---

### Comment pulse
- Scientific data pattern → Many formats (HDF5, COG TIFF, GRIB, etc.) are chunked tensors plus metadata; tools like Zarr/VirtualiZarr generalize efficient cloud chunk access.  
- Cross‑domain parallels → Digital pathology, satellite imagery, geospatial maps, and mining “core logging” share huge 2D+ datasets and benefit from tiled, range‑request‑based streaming.  
- Standards and tooling → DICOM WSI, Arrow/DuckDB dreams, seekable S3 streams, and map libraries (Leaflet/Protomaps) all hint at converging infrastructure for large remote images.

---

### LLM perspective
- View: This is a practical, domain‑specific instance of a general “cloud‑native tensor/image” access pattern becoming standard infrastructure.  
- Impact: Pathology, radiology‑adjacent workflows, and research labs can avoid heavy storage, simplify viewers, and plug slides directly into web tools or pipelines.  
- Watch next: Benchmarks vs existing WSI servers, support for more vendor formats, and experiments streaming ML model weights or embeddings via similar range‑based schemes.
