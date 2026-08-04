# Formal methods and the future of programming

- Score: 296 | [HN](https://news.ycombinator.com/item?id=48526633) | Link: https://blog.janestreet.com/formal-methods-at-jane-street-index/?from_theconsensus=1

### TL;DR

After 25 years of skepticism, Jane Street is forming a formal-methods team because coding agents alter both cost and benefit. Models can automate proof-system drudgery, while their code output creates a verification bottleneck that tests alone cannot close; specifications, types, and proofs can provide universal feedback during generation. Jane Street plans to exploit its control over OxCaml and a receptive user base while integrating existing provers. HN agreed agents reduce proof labor, but debated specification errors, inscrutable formalisms, applicability outside high-stakes systems, and agents changing requirements to make proofs pass.

### Comment pulse

- Automation should favor grinding over cleverness → experienced practitioners want language-integrated assertions and provers that minimize human lemma discovery and notation switching.
- Universal claims differ from tests → properties quantify over every input or execution, exposing races and edge cases no finite suite anticipates.
- Proof theater remains possible → agents may formalize misunderstood English or weaken requirements — counterpoint: machine-checked proofs still guarantee the stated model.

### LLM perspective

- **View:** Agents make proof construction cheaper, but the enduring human task is choosing comprehensible specifications that match intent.
- **Impact:** Language teams gain leverage by integrating constraints early; reviewers shift from line-by-line inspection toward model design and exception auditing.
- **Watch next:** Measure proof maintenance, escaped specification defects, agent iteration counts, developer onboarding, and production gains beyond security-critical code.
