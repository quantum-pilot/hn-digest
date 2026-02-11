# What functional programmers get wrong about systems

- Score: 187 | [HN](https://news.ycombinator.com/item?id=46953491) | Link: https://www.iankduncan.com/engineering/2026-02-09-what-functional-programmers-get-wrong-about-systems/

## TL;DR

The essay argues that functional programming’s powerful type systems encourage overconfidence: they verify single binaries, while real correctness in web/distributed systems is about whole ensembles of coexisting versions, schemas and stored data. It walks through schema migrations, queues, Kafka retention, event sourcing, temporal databases, semantic drift and deployment patterns to show why “making illegal states unrepresentable” stops at process boundaries. HN discussion debates how novel this is, FP’s actual scope, and alternative tools like model checking.

## Comment pulse

- Meta debate: some suspect AI-generated, low-density clickbait due to length and style — counterpoint: others see human drafts, solid research, just overlong.  
- FP scope: critics say thesis confuses language features with systems design; defenders argue FP still removes many intra-process bugs, reducing overall failure surface.  
- Alternatives: commenters promote model checking and session/spec languages for global properties; note similar blind spots in non-FP communities facing distributed-systems complexity.  

## LLM perspective

- View: Treat “version-compatibility graphs” as first-class objects; FP skills suit designing composable migrations and checkers for them.  
- Impact: Stronger pre-deploy compatibility checks reduce incidents more than ever-deeper local type trickery, especially in event-sourced and Kafka-heavy systems.  
- Watch next: tools unifying schema registries, migrations and runtime telemetry to automatically decide if a proposed deploy is ensemble-compatible.
