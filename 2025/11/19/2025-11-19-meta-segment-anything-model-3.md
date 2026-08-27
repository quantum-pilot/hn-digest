# Meta Segment Anything Model 3

- Score: 200 | [HN](https://news.ycombinator.com/item?id=45982073) | Link: https://ai.meta.com/sam3/

### TL;DR

Meta's SAM 3 adds open-vocabulary text and exemplar prompts to image and video segmentation: users can name a category, box one example, click objects, refine mistakes and track matching instances. Meta claims state-of-the-art results while preserving SAM 2's capabilities, and offers model downloads and a playground. Early commenters found zero-shot labeling unusually strong and potentially valuable for reducing annotation work, but reported weaker performance on circuit boards, children's drawings, low-contrast objects and high-instance scenes.

### Comment pulse

- Practitioners saw a capable teacher model → one climbing-labeling test approached a custom model trained on 10,000 annotations.
- Specialized edges remain difficult → industrial traces, sharp corners and unusual visual domains still need refinement or fine-tuning.

### LLM perspective

- View: SAM 3's practical leap is category-level prompting, not merely better masks from clicks.
- Impact: Data teams may shift from drawing labels to reviewing model-generated annotations.
- Watch next: Independent domain benchmarks, commodity-hardware latency and fine-tuning performance on industrial imagery.
