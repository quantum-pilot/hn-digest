# HackMyClaw

- Score: 232 | [HN](https://news.ycombinator.com/item?id=47049573) | Link: https://hackmyclaw.com/

### TL;DR

HackMyClaw is a $100 prompt-injection challenge targeting Fiu, an OpenClaw email assistant running Claude Opus 4.6. Participants may send up to ten crafted emails per hour and win by inducing Fiu to reveal credentials from secrets.env; attacks outside email are forbidden. Fiu’s restrictions are only prompt instructions, not technical controls, and the creator deliberately added no special defenses to test baseline resistance. Discussion questions the experiment’s realism because shared context exposes repeated attacks, costs prevent normal replies, and the agent’s intended email duties remain underspecified.

### Comment pulse

- Repeated attempts may help the defender → seeing many obvious injections can make subtle payloads easier to recognize.
- Treating every inbound email as hostile could improve resilience → counterpoint: an assistant still needs defined legitimate actions to remain useful.
- Some suspect mailing-list collection → the creator says anonymous mail works and addresses will not be reused.

### LLM perspective

- **View:** Prompt-only secrecy is an experiment, not a defensible production boundary.
- **Impact:** Agent builders need capability isolation, least privilege, and human approval enforced outside the model.
- **Watch next:** Report independent-attempt success rates and separate fresh contexts from accumulated attack history.
