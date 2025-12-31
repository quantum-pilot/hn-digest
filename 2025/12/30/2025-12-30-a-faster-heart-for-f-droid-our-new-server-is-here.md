# A faster heart for F-Droid. Our new server is here

- Score: 201 | [HN](https://news.ycombinator.com/item?id=46436409) | Link: https://f-droid.org/2025/12/30/a-faster-heart-for-f-droid.html

### TL;DR
F-Droid has replaced its aging core build/publish server—funded by community donations—with newer hardware, dramatically increasing build frequency from every few days to up to twice daily. The project deliberately avoided generic datacenters; instead, the machine is physically hosted and controlled by a long‑time contributor, emphasizing known location and access. Hacker News discussion centers less on performance and more on governance and trust: is a single member’s “basement server” compatible with security, bus‑factor resilience, and a recent $400k grant?

---

### Comment pulse
- Single‑person hosting is risky → physical control by one contributor raises bus‑factor, governance, and optics concerns, especially given a recent $400k grant—counterpoint: key‑holder risk exists even in cloud.
- Setup feels janky/unprofessional → slow procurement and home‑style hosting unsettle security‑focused communities like GrapheneOS—counterpoint: most FOSS infra is volunteer‑run on shoestring hardware and still underfunded.
- Data center alternative exists → colos can provide strict access control and known location without “some guy’s bedroom”; F-Droid’s framing suggests unfamiliarity with professional hosting options.

---

### LLM perspective
- View: The real issue is redundancy and documented access controls, not whether the box sits in a colo or a closet.
- Impact: Trust of security‑sensitive users and institutional donors depends on transparent infra governance more than on raw hardware specs.
- Watch next: Look for published infra diagrams, multi‑admin access policies, and possibly geographically redundant build/signing setups with verifiable, reproducible outputs.
