# GLM 5.2 is nearly as accurate as a human book keeper

- Score: 165 | [HN](https://news.ycombinator.com/item?id=48850414) | Link: https://toot-books.pages.dev/blog/glm-5-2-vat-benchmark

### TL;DR

Vineyard Finance tested open-weight GLM 5.2 on 59 transactions from one quarterly UK VAT return. Using supplied bank data, PDFs, two notes, and an accounting CLI, it finished in 68 minutes for $2.73; VAT Box 5 differed from human books by seven pence. Yet it failed 20 of 354 checks across 18 transactions, including a legally consequential £10,000 founder-share misclassification, repeated zero-rated-versus-exempt errors, and split-payment mistakes. Humans had found invoices and supplied missing context. HN saw strong automation potential but insisted on human review, audit controls, security, and clear liability.

### Comment pulse

- Benchmark scope excluded messy intake → humans located invoices and supplied contextual notes, leaving the model a cleaner reconciliation task than full bookkeeping.
- Headline accuracy hides asymmetric risk → seven-pence VAT agreement coexisted with a £10,000 share-capital classification carrying legal and filing consequences.
- Automation can cut preparation effort → retain deterministic checks and accountant review — counterpoint: the signer still bears compliance risk when outputs fail.

### LLM perspective

- **View:** This is evidence for supervised transaction processing, not proof that autonomous bookkeeping is solved or human-equivalent.
- **Impact:** Separating machine preparation from accountable human review could reduce cost while preserving judgment for ambiguity, fraud, and statutory classification.
- **Watch next:** Replicate across firms, include invoice retrieval and adversarial fraud, measure run variance, and publish review-time and liability outcomes.
