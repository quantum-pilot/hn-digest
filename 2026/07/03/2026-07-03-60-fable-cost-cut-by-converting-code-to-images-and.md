# 60% Fable cost cut by converting code to images and having the model OCR it

- Score: 225 | [HN](https://news.ycombinator.com/item?id=48776464) | Link: https://github.com/teamchong/pxpipe

### TL;DR

pxpipe is a local proxy that renders token-dense Claude Code inputs—system prompts, tool documentation, large tool results, and older history—as PNG pages while leaving recent turns and outputs untouched. It reports 59–70% lower end-to-end Fable costs and roughly 60–65% smaller requests on coding evaluations, but image reading is lossy: exact identifiers can be silently corrupted, and Opus performs poorly. HN debated whether this exploits temporary billing economics or genuine visual-token efficiency; one prior experiment found extra completion tokens and latency erased savings.

### Comment pulse

- Vision encoding may provide real compression → commenters described image patches becoming compact model tokens without reconstructing billed text.
- Total economics remain unsettled → an earlier OpenAI test reduced prompt tokens but required slower, costlier completions.
- Resource impact is disputed → some called it a pricing loophole — counterpoint: others argued optical tokens remove a fundamental encoding inefficiency.

### LLM perspective

- **View:** This is lossy context compression, not a safe tokenization replacement where byte fidelity matters.
- **Impact:** Agents may gain cheaper long histories while introducing hard-to-detect identifier errors.
- **Watch next:** Compare total cost, latency, task accuracy, and silent-error rates after pricing changes.
