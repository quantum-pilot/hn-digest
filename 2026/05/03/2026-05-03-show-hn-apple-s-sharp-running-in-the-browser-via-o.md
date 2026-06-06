# Show HN: Apple's SHARP running in the browser via ONNX runtime web

- Score: 151 | [HN](https://news.ycombinator.com/item?id=47995037) | Link: https://github.com/bring-shrubbery/ml-sharp-web

## TL;DR
This project runs Apple’s SHARP model entirely in the browser via ONNX Runtime Web to turn a single 2D image into an interactive 3D Gaussian splat, downloadable as a PLY file. It uses React/TypeScript, Bun, WebAssembly workers, and a 2.4 GB ONNX+sidecar model, so performance and memory needs are high and currently desktop‑oriented. The repo also ships an ONNX exporter script for SHARP and highlights Apple’s research‑only model license, which constrains real‑world commercial use.

## Comment pulse
- SHARP + quick preprocessing yields mesmerizing “almost volumetric” VR photo galleries from regular folders, hinting at casual personal 3D memories.
- ONNX handles huge fp32 models cleanly, and can use fp16/int8/fp8 to shrink size—counterpoint: iOS Safari memory caps still make big models fragile.
- In‑browser ML is now practical and privacy‑friendly via ONNX Web/WebGPU, but ops support is patchy and large models still strain mobile hardware.

## LLM perspective
- View: Browsers are quietly becoming general ML runtimes, with ONNX/WebGPU bridging native models and zero‑install experiences.
- Impact: Web devs gain powerful local-first 3D/vision tools; ML authors must think more about export paths, quantization, and licensing.
- Watch next: Better ONNX Web/WebGPU kernels, standardized quantized exports, and browser memory/SharedArrayBuffer policies will determine which models realistically run client‑side.
