# Show HN: Apple's SHARP running in the browser via ONNX runtime web

- Score: 151 | [HN](https://news.ycombinator.com/item?id=47995037) | Link: https://github.com/bring-shrubbery/ml-sharp-web

### TL;DR

ml-sharp-web turns Apple’s SHARP single-image model into a browser playground: upload a photo, generate and preview a Gaussian-splat scene locally, then download a PLY file. ONNX Runtime Web handles inference in a worker, with browser-side geometry conversion and rendering. The major constraint is the roughly 2.4 GB external model-weights file, plus heavy memory and WebGPU/WASM requirements; Chrome or Edge is recommended, and Apple’s weights retain research-use restrictions. HN highlighted immersive VR photo browsing and privacy benefits, while discussing quantization, Safari limits, and uneven WebGPU operator support.

### Comment pulse

- Client-side inference can make personal imagery private and immersive → one prototype cached photo folders for near-instant VR scenes.
- The 2.4 GB FP32 checkpoint dominates usability → lower-precision ONNX types could halve loads with little quality loss in other projects.
- Browser deployment broadens access → counterpoint: Safari memory caps, mobile coverage, and incomplete WebGPU operators still break ambitious models.

### LLM perspective

- **View:** The demo proves execution portability before practical distribution; model delivery is now the larger bottleneck.
- **Impact:** Creators can embed spatial-photo generation without servers, provided desktop hardware and browsers meet demanding requirements.
- **Watch next:** FP16 or INT8 exports, startup latency, peak RAM, cross-browser success rates, WebGPU coverage, and mobile-device benchmarks.
