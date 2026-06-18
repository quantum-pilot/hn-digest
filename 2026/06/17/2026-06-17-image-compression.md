# Image Compression

- Score: 153 | [HN](https://news.ycombinator.com/item?id=48522927) | Link: https://www.makingsoftware.com/chapters/image-compression

- TL;DR  
Hollick’s piece introduces image compression as the art of exploiting human visual quirks—like tolerance for color loss and detail smoothing—to shrink files without visible degradation. Hacker News discussion pivots to practical codecs: niche but extremely simple lossless formats, modern general-purpose contenders integrated into RAW-photo pipelines, and newer web-ready options vying to replace JPEG/PNG. Commenters weigh compression ratio, speed, metadata handling, and browser/OS support, and debate whether these fundamentals should already be standard CS knowledge.

- Comment pulse  
  - Simple formats like QOI show PNG-level lossless compression with tiny specs and fast C code; others LZ4 raw bitmaps or explore progressive multi-image thumbnails.  
  - JPEG XL ships inside DNG/ProRAW workflows and major photo tools, with emerging browser flags—counterpoint: complexity and JPEG 2000’s history still make adoption uncertain.  
  - Web developers note AVIF’s strong lossy compression and now-universal browser support, but also that WebP can outperform it for lossless images in some cases.

- LLM perspective  
  - View: Most teams only need a pragmatic decision tree, not codec theory—pick formats per asset type, automate via build tools.  
  - Impact: Standardizing on modern formats in CMSs, CDNs, and design pipelines can quietly cut bandwidth and storage without app-level changes.  
  - Watch next: When browsers enable codecs by default, OS image APIs expose them seamlessly, and camera vendors expand support.
