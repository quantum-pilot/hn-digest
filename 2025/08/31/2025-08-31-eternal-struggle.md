# Eternal Struggle

- Score: 680 | [HN](https://news.ycombinator.com/item?id=45086020) | Link: https://yoavg.github.io/eternal/

- TL;DR
  - An interactive “two balls paint a circle” toy: each ball bounces within its colored region; hits expand its color, creating a self-balancing, often yin/yang-like split. HN noticed negative feedback (smaller side bounces more, catching up), occasional non-50/50 equilibria, and visual parallels to pressure equalization or a normal curve. A popular speed-slider fork is buggy, and rare collision/precision glitches let one ball “tunnel” across, turning the whole circle one color. Source code was shared.
  - *Content unavailable; summarizing from title/comments.*

- Comment pulse
  - Self-balancing claim → smaller region forces more collisions, raising its expansion rate — counterpoint: a circle split by a straight line is similarly stable.
  - Observed topologies → yin/yang and donut-with-hole equilibria; some runs resemble a normal curve’s area fill.
  - Implementation notes → speed-slider fork fails to slow after high rates; collision bugs occasionally let a ball cross and dominate.

- LLM perspective
  - View: Simple stochastic system with negative feedback; emergent equilibria reveal boundary-dependent dynamics and numerical fragility.
  - Impact: Good teaching aid for feedback, conservation intuitions, and how small physics bugs cascade in sims.
  - Watch next: Add deterministic integrator, robust collision resolution, invariants logging; test speed scaling and topology transitions.
