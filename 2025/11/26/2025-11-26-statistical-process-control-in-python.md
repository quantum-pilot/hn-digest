# Statistical Process Control in Python

- Score: 191 | [HN](https://news.ycombinator.com/item?id=46055421) | Link: https://timothyfraser.com/sigma/statistical-process-control-in-python.html

### TL;DR
Open-access textbook “System Reliability and Six Sigma in R and Python” walks through reliability engineering, probability, life distributions, and regression, then lands on practical Statistical Process Control (SPC) in both R and Python. The SPC-in-Python chapters show how to compute descriptive statistics, subgroup and between-group metrics, build X‑bar/S and moving-range charts, and estimate capability indices (Cp, Cpk, Pp, Ppk) with confidence intervals and bootstrapping. HN discussion emphasizes that such classical SPC methods often beat deep neural nets for real-world time-series monitoring.

---

### Comment pulse
- Classical SPC > deep nets for many anomaly-detection tasks → far fewer parameters, easier debugging, less babysitting, practical for small teams—counterpoint: organizational politics often favor “AI” regardless.
- Tooling nostalgia and evolution → Minitab once dominated SPC; open source lagged on advanced charts, but modern Python stacks now cover much of that ground.
- Classical statistics remains essential → small, messy, clinical and operational datasets still favor interpretable SPC and standard inference over heavier ML workflows.

---

### LLM perspective
- View: For operational monitoring, start with SPC/control charts; add ML only when there’s clear incremental value and enough high-quality data.
- Impact: Site reliability, manufacturing, and clinical teams can standardize on a transparent Python SPC toolkit instead of bespoke ML detectors.
- Watch next: Comparative benchmarks of SPC vs deep nets on public time-series corpora, plus more integrated SPC libraries in mainstream Python stacks.
