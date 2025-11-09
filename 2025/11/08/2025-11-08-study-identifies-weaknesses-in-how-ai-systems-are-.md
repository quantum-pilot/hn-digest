# Study identifies weaknesses in how AI systems are evaluated

- Score: 319 | [HN](https://news.ycombinator.com/item?id=45856804) | Link: https://www.oii.ox.ac.uk/news-events/study-identifies-weaknesses-in-how-ai-systems-are-evaluated/

- TL;DR
    - Oxford Internet Institute reviewed 445 LLM benchmarks and found weak construct validity: only 16% use statistical comparisons; many target vague constructs (e.g., “reasoning,” “harmlessness”) without clear definitions. Examples show confounded formats, brittle performance, and overclaimed capabilities. They propose psychometrics-style standards and a Construct Validity Checklist. HN practitioners say evals are chaotic and misaligned with real use; A/B and human feedback have pitfalls; teams rely on private, task-specific tests to avoid contamination; some call for causal and real-world (“meatspace”) evaluations.

- Comment pulse
    - Benchmarks are noisy and non-predictive → weak stats, rushed research, “benchmarketing,” and poor transparency; even infra benchmarks fail to map to real workloads.
    - Product A/B and human ratings help but can backfire → optimize for rater exploits and noisy prod signals — counterpoint: at scale, A/B best measures target outcomes directly.
    - Domain/private evals beat public suites → bespoke bug repos and hidden tests avoid contamination; crowdsourcing tough questions aims to stress real reasoning.

- LLM perspective
    - View: Treat benchmarks as measurements of latent constructs; define targets, report uncertainty, and pre-register analyses.
    - Impact: Model rankings, safety claims, and regulatory reliance (e.g., EU AI Act) hinge on sturdier evals; vendors must curb overclaiming.
    - Watch next: Adoption of the checklist; causal/interventional eval methods; contamination-resistant testbeds and third-party audits.
