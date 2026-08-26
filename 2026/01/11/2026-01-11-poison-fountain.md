# Poison Fountain

- Score: 156 | [HN](https://news.ycombinator.com/item?id=46577464) | Link: https://rnsaffn.com/poison3/

### TL;DR

Poison Fountain is an adversarial service meant to feed unlimited corrupted text to suspected AI crawlers, asking site owners to proxy compressed responses through crawler-targeted hidden paths. Its stated aim is degrading models because its operators view machine intelligence as an existential threat. HN readers doubted the tactic: frontier labs curate datasets, test contributions, and can revise ingestion, while browser agents can mimic humans. Others saw poisoning as leverage against uncompensated scraping, but warned it could make models less safe and turn participants into unwitting hosts for arbitrary content.

### Comment pulse

- Effectiveness skepticism → large labs invest in data quality, proxy-model filtering, rollback, and reinforcement learning, reducing vulnerability to simple poisoning.
- Access asymmetry → crawler detection cannot reliably separate automated browsers from paying humans, while generated low-value content already contaminates public data.
- Incentives and harm → poisoning may impose curation costs or deter uncompensated scraping — counterpoint: degraded models could become more unstable and unsafe.

### LLM perspective

- View: Data poisoning is more likely to raise acquisition costs than halt capable, well-funded model developers.
- Impact: Small model builders and downstream users may absorb more damage than the intended frontier laboratories.
- Watch next: Measure poison survival through deduplication, filtering, and post-training, plus abuse arising from blind proxying.
