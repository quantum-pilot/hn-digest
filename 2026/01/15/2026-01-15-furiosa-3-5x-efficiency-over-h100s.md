# Furiosa: 3.5x efficiency over H100s

- Score: 206 | [HN](https://news.ycombinator.com/item?id=46626410) | Link: https://furiosa.ai/blog/introducing-rngd-server-efficient-ai-inference-at-data-center-scale

### TL;DR

FuriosaAI’s NXT RNGD Server packages eight inference accelerators, 384 GB HBM3, and preinstalled serving software into a 3 kW, air-cooled PCIe system. Its headline comparison fits five servers into a 15 kW rack, producing 49,412 tokens/second on Llama 3.1 8B FP8—3.5 times one H100 SXM system and ahead of three H100 PCIe systems. Commenters welcomed efficiency-focused competition but challenged the comparison, requesting direct eight-H100, newer-model, memory-capacity, price, and real deployment evidence before accepting the economic case.

### Comment pulse

- Power and cooling limits could open space beyond Nvidia → its software, HBM, foundry, and networking advantages remain formidable.
- The 15 kW rack comparison feels artificial → counterpoint: purchase and cooling costs could make fixed-power comparisons economically relevant.
- Llama 3.1 8B and 48 GB per card raise workload questions → readers requested larger-model, batching, and direct eight-H100 benchmarks.

### LLM perspective

- View: Fixed-power throughput helps facility planning, but buyers still need total-cost and workload-coverage data.
- Impact: Existing air-cooled data centers could add inference capacity without retrofits demanded by denser GPU installations.
- Watch next: Independent tests of price, latency, batching, model compatibility, and production reliability in customer deployments.
