# Show HN: ChartGPU – WebGPU-powered charting library (1M points at 60fps)

- Score: 467 | [HN](https://news.ycombinator.com/item?id=46706528) | Link: https://github.com/ChartGPU/ChartGPU

### TL;DR

ChartGPU is an MIT-licensed TypeScript library that renders interactive line, area, bar, scatter, pie, and candlestick charts through WebGPU, with streaming updates, zoom, synchronized crosshairs, and React bindings. Its launch claimed one million points at 60 fps; HN feedback quickly exposed idle rendering waste and benchmark ambiguities, prompting render-on-demand fixes and a benchmark toggle. Commenters also urged columnar data, peak-preserving downsampling, density maps, and clearer boundaries between conventional charts and large network-graph visualization.

### Comment pulse

- Benchmark rigor → compare unsampled data and visible fidelity, because LTTB can erase peaks and nested arrays inflate allocation costs.
- Visualization quality → density or logarithmic intensity can reveal overplotting that raw point rendering conceals.
- Responsiveness → maintainers patched idle CPU use and reported 5 million streaming candles at 104 fps, while a timeframe bug remained.

### LLM perspective

- View: GPU throughput matters only when data representation, decimation, and perceptual fidelity are measured together.
- Impact: Browser dashboards gain headroom, but teams must budget for WebGPU compatibility and specialized interaction design.
- Watch next: Independent uPlot comparisons, idle-power measurements, multi-chart limits, accessibility, and correctness at extreme scales.
