# Mistral OCR 4

- Score: 423 | [HN](https://news.ycombinator.com/item?id=48645152) | Link: https://mistral.ai/news/ocr-4/

### TL;DR

Mistral OCR 4 extracts text plus bounding boxes, typed blocks, and page- and word-level confidence from common document formats in 170 languages. The compact model can run in one self-hosted container or via API at $4 per 1,000 pages, falling to $2 in batch; Document AI adds schema-shaped output for $5. Mistral reports 72% average preference in blind human comparisons and leading public/internal scores while acknowledging scoring artifacts. HN focused less on features than benchmark credibility, citing truncated axes, internally reproduced competitors, disappointing earlier versions, and limited anecdotal improvements.

### Comment pulse

- Published comparisons need stronger trust signals → readers criticized truncated axes, internally reproduced competitor scores, and reliance on Mistral’s own multilingual evaluation.
- Past accuracy claims created skepticism → one evaluator said earlier versions lagged rivals — counterpoint: another saw real gains in a few samples.
- Postal sorting illustrates OCR’s boundary → machines route standardized fragments, while local workers historically resolved ambiguous names and irregular addresses through context.

### LLM perspective

- **View:** Structure and calibrated confidence may matter more than marginal character accuracy because they enable citation, redaction, and human review.
- **Impact:** Privacy-sensitive organizations gain an on-premises ingestion option; developers can choose raw control or schema-generating convenience from one endpoint.
- **Watch next:** Run document-specific evaluations against Baidu and incumbents, publishing error distributions, calibration curves, latency, hardware, and total pipeline cost.
