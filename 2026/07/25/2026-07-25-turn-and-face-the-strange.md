# Turn And Face The Strange

- Score: 126 | [HN](https://news.ycombinator.com/item?id=49051369) | Link: https://fly.io/blog/kurt-scott-money-sprites/

### TL;DR

Fly.io is refocusing around Sprites, persistent but semi-disposable cloud computers for coding agents, after new funding and naming ex-Docker CEO Scott Johnston as CEO; founder Kurt Mackey becomes an adviser and remains on the board. The new version adds a rebuilt block device with instant checkpointing and mass cloning, plus connectors that authenticate external requests without exposing reusable secrets. Fly Machines and its PaaS remain. HN questioned the pivot sharply: users reported data loss, zombie instances, outages, and support failures, while strategists called agent sandboxes crowded and easily commoditized.

### Comment pulse

- Reliability threatens the thesis → multiple users reported frequent data loss and unreachable instances — counterpoint: one operator saw substantial improvement over two recent months.
- Operations remain a longstanding concern → customers described recurring regional outages, stale status pages, and paid-support responses arriving after incidents ended.
- Strategic differentiation looks uncertain → critics said agent sandboxes are easy to recreate atop commodity compute and AWS becomes easier when agents handle infrastructure.

### LLM perspective

- **View:** The bet is that durability, cloning, and credential isolation beat raw compute; reliability determines whether those abstractions have value.
- **Impact:** Existing Fly customers retain their platform, but capital attention shifts toward agent companies with bursty, stateful workloads.
- **Watch next:** Track data loss, restore success, support latency, Sprite utilization, customer retention, margins, and connector credential leaks.
