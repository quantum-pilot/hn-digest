# Nothing Ever Happens: Polymarket bot that always buys No on non-sports markets

- Score: 344 | [HN](https://news.ycombinator.com/item?id=47753472) | Link: https://github.com/sterlingcrispin/nothing-ever-happens

### TL;DR

“Nothing Ever Happens” is an asynchronous Python Polymarket bot that scans standalone non-sports yes/no markets and buys NO shares below a configurable price cap. It tracks positions, persists recovery state, and defaults to paper trading unless three explicit live flags plus wallet, database, and Polygon configuration are supplied. Its creator calls it a meme with zero risk management and reports no returns. Commenters note that 73% of markets resolving NO does not establish profit: prices, correlated multi-outcome markets, liquidity, spreads, resolution timing, and rare losses determine expected value.

### Comment pulse

- Dramatic outcomes may be overpriced because excitement attracts buyers. — counterpoint: efficient traders can erase that edge once observable.
- Naive backtests can leak resolution timing; real returns depend on capital lockup, market selection, and enough volume.
- One unlikely YES can erase 10–20 wins, making diversification and risk limits essential despite a high NO base rate.

### LLM perspective

- **View:** Outcome frequency is not mispricing; the purchase price already encodes probability.
- **Impact:** Thin books and uncertain settlement can dominate the strategy’s apparent statistical advantage.
- **Watch next:** Live, fee-adjusted P&L versus calibrated baselines, including drawdowns and time-weighted capital usage.
