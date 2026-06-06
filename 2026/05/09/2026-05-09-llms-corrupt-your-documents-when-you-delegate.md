# LLMs corrupt your documents when you delegate

- Score: 336 | [HN](https://news.ycombinator.com/item?id=48073246) | Link: https://arxiv.org/abs/2604.15597

### TL;DR
The paper introduces DELEGATE-52, a benchmark where LLMs are asked to iteratively edit complex documents across 52 professional domains. Evaluating 19 models, the authors find that even top systems corrupt about 25% of document content over long workflows, with larger files, more steps, and distractor files worsening degradation. A simple “agentic” setup with read/write/code tools doesn’t help much. HN commenters argue this mostly reflects poor tool design, yet agree that naive “AI-washing” of documents is dangerously common in practice.

---

### Comment pulse
- Core finding is unsurprising: round-tripping whole documents through an LLM inevitably corrupts them → real issue is that many organizations are doing exactly this.  
- Harness critique: using only read_file/write_file forces risky full rewrites → proper agents use surgical edit tools and diffs — counterpoint: non-expert users rarely do.  
- LLMs cause “semantic ablation” / mean reversion → each pass removes nuance and specificity, like repeated JPEG compression or the telephone game.

---

### LLM perspective
- View: Treat LLMs as planners and diff-generators, not as faithful document copiers or authoritative summarizers over many iterative passes.  
- Impact: High-stakes writing, codebases, and knowledge repositories are at risk if teams rely on naive “paste-all, rewrite-all” workflows.  
- Watch next: Benchmarks comparing rich edit-tool agents vs naive round-trip setups, plus standardized validation and diff-review protocols for LLM-assisted editing.
