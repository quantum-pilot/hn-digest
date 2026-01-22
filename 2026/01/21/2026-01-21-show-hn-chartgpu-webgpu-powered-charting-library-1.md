# Show HN: ChartGPU – WebGPU-powered charting library (1M points at 60fps)

- Score: 467 | [HN](https://news.ycombinator.com/item?id=46706528) | Link: https://github.com/ChartGPU/ChartGPU

### TL;DR
ChartGPU is an open-source TypeScript charting library that uses WebGPU for high-FPS, highly interactive charts on very large datasets (e.g., 1M points at 60fps). It supports common series types (line, area, bar, scatter, pie, candlestick), streaming updates, zooming, theming, and React bindings. Internally, a render coordinator manages scales, GPU buffers, and WGSL-based renderers. HN discussion focuses on downsampling accuracy, idle CPU usage (since patched via render-on-demand), and advanced techniques like density/heatmap rendering for overplotted data.

### Comment pulse
- Sampling/downsampling is tricky → LTTB and naive sampling can hide peaks; experts suggest adaptive or min/max aggregation per pixel for correctness.  
- Idle performance matters → continuous GPU redraw wastes CPU/GPU; render-on-demand with dirty flags matches canvas libraries’ zero-CPU idle behavior.  
- Beyond basic charts → users want drawing/annotations and potentially graph/network visualizations; heavy datasets favor density/heatmap or “digital phosphor” styles over literal point plotting.

### LLM perspective
- View: WebGPU-native charting narrows the gap between browser dashboards and native/desktop visualization in both scale and interactivity.  
- Impact: Data-heavy apps in finance, observability, and scientific tools gain smoother UX without custom GL/WebGPU plumbing.  
- Watch next: Benchmarks vs uPlot/Plotly, Firefox WebGPU maturity, and higher-level patterns like density modes and multi-chart dashboards.
