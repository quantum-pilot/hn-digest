# The React2Shell Story

- Score: 209 | [HN](https://news.ycombinator.com/item?id=48065511) | Link: https://lachlan.nz/blog/the-react2shell-story/

## TL;DR
Lachlan Davidson dissected React’s undocumented Flight protocol (used by React Server Components / Server Actions) and uncovered React2Shell, a critical remote code execution bug (CVE-2025-55182). Flight lets clients send rich, non-JSON data and reference arbitrary prototype properties; combined with JavaScript “thenables” and React’s internal `Chunk` promise implementation, an attacker could coerce React into executing arbitrary server-side JS in a stock Next.js app. Meta and the React/Vercel teams responded rapidly with patches and coordination, sparking debate over RSC complexity and safety.

---

## Comment pulse

- Meta/React engineers praise Davidson → exemplary coordinated disclosure, deep collaboration on validation and remediation under tight time pressure.  

- RSCs are a DX disaster → mixing client/server concerns scales poorly in large teams — counterpoint: complexity mirrors the web’s reality and grants powerful control over UX.  

- Accessibility gripe → site’s animated background ignores `prefers-reduced-motion`, forcing some readers into browser reader mode to avoid motion sickness.  

---

## LLM perspective

- View: Protocol-level features plus dynamic language quirks create subtle RCE paths; undocumented internals multiply risk and debugging difficulty.  

- Impact: Framework vendors must harden serialization protocols; app teams should not assume TS types protect server actions from hostile inputs.  

- Watch next: Security reviews of similar “rich transport” layers (RPC, server components), better runtime validation, and tooling to fuzz these custom protocols.
