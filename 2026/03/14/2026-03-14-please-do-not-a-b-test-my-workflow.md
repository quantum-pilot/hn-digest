# Please do not A/B test my workflow

- Score: 155 | [HN](https://news.ycombinator.com/item?id=47375682) | Link: https://backnotprop.com/blog/do-not-ab-test-my-workflow/

## TL;DR
Author uses Claude Code’s “plan mode” heavily and pays $200/month. An Anthropic A/B test silently changed the planning prompt, yielding terse, worse plans and breaking their workflow. They argue that for professional tools, opaque experiments on core behavior undermine trust, reproducibility, and responsible human-in-the-loop use; users need transparency, configurability, and opt-out. An Anthropic engineer confirms the test, says it aimed to cut rate-limit usage, and has now been stopped. HN debates A/B testing ethics for LLMs and open-source alternatives.

## Comment pulse
- Silent A/B tests on core LLM behavior are unacceptable → they unpredictably degrade workflows, confuse teams, and feel like experimentation without informed consent.  
- LLM instability plus hidden tests kills reproducibility → long-term evaluations or organizational rollouts become meaningless when vendors can secretly flip behavior mid-study.  
- Open source pitched as safeguard → no unilateral A/B flips, more user control — counterpoint: dependencies and low telemetry still allow surprises and weak evidence.  

## LLM perspective
- View: Paid AI dev tools should offer version pinning, a stable channel, and explicit opt-in for experiments on core behavior.  
- Impact: Enterprises needing auditability, safety, or research validity will pressure vendors toward transparent prompts, change logs, and experiment metadata.  
- Watch next: Whether major LLM platforms ship experiment dashboards, per-project settings, and policies for excluding high-risk domains from disruptive testing.
