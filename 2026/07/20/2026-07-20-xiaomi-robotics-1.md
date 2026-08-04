# Xiaomi-Robotics-1

- Score: 445 | [HN](https://news.ycombinator.com/item?id=48974454) | Link: https://robotics.xiaomi.com/xiaomi-robotics-1.html

### TL;DR

Xiaomi-Robotics-1 is a vision-language-action foundation model pretrained on 100,000 hours of embodiment-free manipulation across more than 1,700 settings, then aligned with cross-embodiment data including 7,200 hours from real robots. Xiaomi reports predictable gains from larger models and datasets, generalization to unseen homes and objects, state-of-the-art results on four simulation benchmarks, and rapid specialization: under 10 demonstration hours per task yielded 75% aggregate success versus 40% for π0.5. HN focused on the practical leap—two-handed mobile manipulation of deformable objects—and welcomed imperfect but useful laundry and household automation.

### Comment pulse

- Demo difficulty was easy to underestimate → bimanual coordination, mobility, deformable materials, thin zippers, and multi-object grasps combine formerly separate research problems.
- Convenience outranked perfection → commenters would accept wrinkled folding if it removes chores, expecting quality to improve as earlier appliances did.
- Extra limbs could simplify holding and turning → counterpoint: unfamiliar embodiments increase control complexity and lack abundant human-demonstration data for training.

### LLM perspective

- **View:** Separating broad manipulation pretraining from embodiment and instruction alignment reduces dependence on scarce robot-specific data.
- **Impact:** If reported transfer holds across hardware, household robotics may progress through reusable base policies plus small task-specific demonstration sets.
- **Watch next:** Independently test safety, long-horizon reliability, failure recovery, hardware breadth, and performance outside curated demonstrations.
