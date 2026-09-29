# Parley: Federated, decentralised chat that speaks plain IRC

- Score: 322 | [HN](https://news.ycombinator.com/item?id=49875913) | Link: https://git.mills.io/prologic/parley

### TL;DR

*Content unavailable; summarizing from title/comments.*

Based only on HN discussion, Parley is described by one commenter as a centreless chat network where small domain instances discover peers through DNS and identity documents, exchange signed HTTPS messages, and expose federation to ordinary IRC clients. Other commenters focused on absent channel ownership and operators, per-server blocking, fragmented room visibility, spam, hostile instances, and persistent netsplits. Some proposed shared reputation filters, but critics argued those mechanisms merely redistribute ecosystem-wide moderation and namespace governance to administrators.

### Comment pulse

- Operator-free global rooms alarmed commenters → removing local moderation leaves abuse decisions to every instance administrator or shared blocklists.
- Federation creates availability ambiguity → rooms persist without an owner, but each instance may see a different network after disconnections.
- Open instance creation invites abuse → commenters questioned spam and hostile-server defenses, while proposed unknown-server filtering seemed operationally critical.

### LLM perspective

- View: The comments describe an elegant transport idea whose unresolved governance may dominate its user experience.
- Impact: IRC users could gain federation without plugins, while instance operators inherit difficult moderation, discovery, and abuse responsibilities.
- Watch next: Usable documentation must specify trust bootstrapping, identity, room discovery, moderation, spam resistance, and partition recovery.
