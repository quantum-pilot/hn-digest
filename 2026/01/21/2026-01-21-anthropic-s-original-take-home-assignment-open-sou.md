# Anthropic's original take home assignment open sourced

- Score: 597 | [HN](https://news.ycombinator.com/item?id=46700594) | Link: https://github.com/anthropics/original_performance_takehome

### TL;DR

This repository releases Anthropic’s original performance take-home: optimize a benchmark that began as a four-hour exercise, then shifted to a two-hour 18,532-cycle baseline as Claude improved. Listed results put Opus 4.5 near strong human performance, with longer runs and an improved harness reaching lower cycle counts; the best human score remains undisclosed. Commenters compared model runs, explored memory-bandwidth bottlenecks, and split over whether the challenge is a useful skills signal or an onerous, unpaid recruiting filter.

### Comment pulse

- Benchmarking became collaborative → Readers shared agent scores and optimization clues, especially vectorization limits and random tree reads bottlenecking memory bandwidth.
- Recruiting value remains disputed → Fans prefer a concrete systems problem to LeetCode; critics see days of unpaid work without hiring certainty.
- Transfer matters more than trivia → Several argued low-level specialization is less important than demonstrated learning and problem-solving ability.

### LLM perspective

- View: The task measures performance reasoning well, but unlimited retries blur comparison with the original timed hiring exercise.
- Impact: Public benchmarks let candidates, engineers, and model vendors compare optimization strategies on a shared workload.
- Watch next: Whether newer models consistently beat expert humans under equal time, tooling, and review constraints.
