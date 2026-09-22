# AI coding has made CI a bottleneck, so we reworked ours to keep up

- Score: 305 | [HN](https://news.ycombinator.com/item?id=49792067) | Link: https://linear.app/now/ci-bottleneck-reworked

### TL;DR

Linear says agent-written code and tests made continuous integration a bottleneck, even as its suite nearly quadrupled. By changing runners and compilers, shrinking critical-path work, eliminating repeated setup, and carefully sharing test-module state, it cut pull-request waiting from over six minutes to just above five while roughly halving runner time per test. HN readers questioned whether higher code throughput improves products, warning that human review, product judgment, and the usefulness of generated tests may now be harder constraints.

### Comment pulse

- Faster coding has not guaranteed better products → organizational dysfunction and low-impact output can absorb additional implementation capacity.
- Human validation is becoming the bottleneck → passing CI cannot establish that customers understand, value, or enjoy a change.
- Generated tests deserve close review → they can enable large refactors — counterpoint: trivial coverage may only increase cost and false confidence.

### LLM perspective

- View: CI optimization compounds, but validating intent matters more as agents make implementation cheaper.
- Impact: Engineering teams must budget review, product testing, and infrastructure together instead of maximizing merged code.
- Watch next: Track escaped defects, useful coverage, review time, and customer outcomes alongside CI latency and runner-minutes.
