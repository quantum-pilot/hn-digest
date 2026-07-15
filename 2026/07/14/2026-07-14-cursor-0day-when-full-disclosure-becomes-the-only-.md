# Cursor 0day: When Full Disclosure Becomes the Only Protection Left

- Score: 187 | [HN](https://news.ycombinator.com/item?id=48910676) | Link: https://mindgard.ai/blog/cursor-0day-when-full-disclosure-becomes-the-only-protection-left

## TL;DR
Mindgard found a simple but serious Windows bug in the Cursor IDE: when a project is opened, Cursor automatically runs any git.exe in the repo root, giving arbitrary code execution to anyone controlling that repository. Mindgard disclosed in December 2025 via email and HackerOne; despite confirmation and reproduction, Cursor allegedly shipped ~200 releases without fixing or warning users, prompting full public disclosure. HN commenters debate severity, Windows’ role, and whether overloaded, AI-flooded bug-bounty pipelines are killing coordinated disclosure.

## Comment pulse
- Vendor silence suggests disclosure pipelines overwhelmed by AI-found bugs → some researchers now favor public disclosure—counterpoint: this case might just reflect Cursor’s internal priorities.  
- Risk model dispute → some say attacker already controlling repo means compromise; others argue opening random GitHub code shouldn’t imply arbitrary execution in your IDE.  
- Windows search-path semantics blamed → current-directory execution is old gotcha, yet commenters stress Cursor should hard-code Git locations or add trust prompts.  

## LLM perspective
- View: IDEs that auto-execute binaries from repositories grant maintainers RCE; treat opening a project like running untrusted code needing containment.  
- Impact: Enterprises adopting AI IDEs need policies to sandbox untrusted repos, restrict executable paths, and audit how tools discover binaries.  
- Watch next: Whether Cursor and peers add trust prompts, repo sandboxes, signed toolchains, and improve triage for AI-generated vulnerability reports.
