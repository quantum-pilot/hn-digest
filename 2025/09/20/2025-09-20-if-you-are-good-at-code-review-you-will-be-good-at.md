# If you are good at code review, you will be good at using AI agents

- Score: 129 | [HN](https://news.ycombinator.com/item?id=45310529) | Link: https://www.seangoedecke.com/ai-agents-and-code-review/

### TL;DR

The author argues that effective coding-agent use resembles structural code review: humans must question architecture, find simpler existing paths, and redirect agents before they invest heavily in bad designs. Line-level nitpicking and rubber-stamping both miss this role; current agents behave more like enthusiastic juniors than autonomous engineers. HN commenters challenge whether inspection can rescue a failure-prone process, worry juniors lack the judgment to supervise it, and suggest automated tests, fuzzing, benchmarks, and narrow task boundaries as cheaper guardrails.

### Comment pulse

- Review skill may not scale → repeated correction is cognitively expensive and can erase promised productivity gains.
- Junior adoption creates a training gap → inexperienced engineers cannot reliably recognize architecture they have never learned to design.
- Process controls can reduce review load → tests, fuzzing, coverage, and performance thresholds catch objective failures before human inspection.

### LLM perspective

- View: Agent leverage depends less on code volume than on early rejection of wrong problem formulations.
- Impact: Senior judgment becomes a throughput constraint while junior learning risks being displaced by generated implementation.
- Watch next: Comparative defect rates, review time, skill development, and guardrail effectiveness across agent-assisted teams.
