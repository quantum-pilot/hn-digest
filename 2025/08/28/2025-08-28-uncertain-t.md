# Uncertain<T>

- Score: 448 | [HN](https://news.ycombinator.com/item?id=45054703) | Link: https://nshipster.com/uncertainty/

- TL;DR
    - NSHipster ports Microsoft Research’s Uncertain<T> to Swift, making uncertainty a first-class type. Values carry distributions; operators build computation graphs; decisions query probabilities via Monte Carlo sampling and SPRT. Examples span GPS accuracy, physics, and UI thresholds, with tunable sample budgets. Discussion stresses that real GPS error isn’t always circular and often needs sensor fusion/particle filters; asks about covariance (shared sampling can capture it); and connects the idea to probabilistic programming, probability monads, and even hardware like Signaloid for nonparametric propagation.

- Comment pulse
    - GPS error isn’t circular; multipath/occlusion dominate, so AVs use sensor fusion and particle filters — counterpoint: Rayleigh is fine for many consumer, open-sky cases.
    - Correlation matters; shared sampling across reused leaf variables captures covariance automatically; some want systems to learn correlations; gvar suggested for explicit tracking.
    - This aligns with probabilistic programming and probability monads; languages/libraries (Haskell, monad-bayes) and even hardware (Signaloid) show practical, optimized uncertainty propagation.

- LLM perspective
    - View: Treating uncertainty as a type improves decision thresholds and reduces brittle if-statements in sensor- and user-data-heavy apps.
    - Impact: Mobile, robotics, and finance teams gain calibrated outputs; developers must budget sampling costs and surface confidence to UX and logging.
    - Watch next: Benchmarks vs deterministic baselines; covariance-aware APIs; CoreLocation integration; optional particle filters; compare CPU/GPU to hardware like Signaloid.
