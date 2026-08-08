# CARA 2.0 – “I Built a Better Robot Dog”

- Score: 445 | [HN](https://news.ycombinator.com/item?id=48005432) | Link: https://www.aaedmusa.com/projects/cara2

### TL;DR

CARA 2.0 is an 18.2-pound, mostly 3D-printed quadruped built for $1,450—half its predecessor’s cost, though above the team’s $1,000 target. Its twelve quasi-direct-drive joints pair $18 drone motors, hand-rewound from 335 to 90 KV, with inexpensive controllers and 9.6:1 rope capstan reductions producing 12 Nm peak torque. The robot walks at 0.55 m/s, carries 6.8 kg, and runs about an hour. Redesigning asymmetric legs, turning trajectories, and center-of-mass compensation fixed major gait problems; reinforcement-learned locomotion remains unfinished.

### Comment pulse

- Readers credited drone parts for democratizing legged robotics — counterpoint: firmware repairs and manual rewinding preserve substantial hidden labor.
- Thermal risk drew attention because holding poses can heat motors; backstops, current integration, or sensors could protect longer runs.
- Several wanted simulation-trained galloping and compared CARA with documented Stanford Pupper kits costing substantially more.

### LLM perspective

- Cost reductions make this a strong teaching platform by exposing firmware, winding, mechanics, and control tradeoffs.
- Capstan precision blocks repeatable scaling; factory-custom windings and standard actuators could redirect effort toward locomotion research.
- Watch thermal endurance, fall recovery, repeatable assembly, actuator sourcing, and simulation-to-real reinforcement learning.
