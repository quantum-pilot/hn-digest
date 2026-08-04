# What happened after 2k people tried to hack my AI assistant

- Score: 350 | [HN](https://news.ycombinator.com/item?id=48681687) | Link: https://www.fernandoi.cl/posts/hackmyclaw/

### TL;DR

More than 2,000 people sent 6,000 emails to Fiu, an OpenClaw assistant running Claude Opus 4.6, trying to extract a secrets.env file or trigger unauthorized replies. None succeeded despite multilingual prompts, authority impersonation, fake emergencies, and refusal-string attacks. A four-line security policy appeared effective, but Gmail suspension, $500-plus API costs, contaminated batch context, persistent memory, one-shot interactions, and a bounty peaking at $1,000 weakened the experiment. HN argued the result tests refusal under adversarial saturation, not whether a useful, permissioned agent can distinguish legitimate work from subtle attacks.

### Comment pulse

- Security without utility is trivial → an agent that refuses everything protects secrets but fails the harder task of safely completing legitimate requests.
- Exfiltration need not appear in output → realistic agents can send mail, call tools, or make requests; action misuse is the relevant boundary.
- Zero wins establish a useful lower bound → casual one-shot attacks failed — counterpoint: skilled attackers may withhold valuable jailbreaks from a public $1,000 challenge.

### LLM perspective

- **View:** The result supports model-level refusal, but says little about end-to-end security once agent permissions and legitimate ambiguity increase.
- **Impact:** Builders should retain least privilege, isolate contexts, control memory, monitor costs, and test usefulness alongside attack resistance.
- **Watch next:** Run blinded multi-turn tests using real tools, mixed traffic, weaker models, larger bounties, and joint utility-misuse metrics.
