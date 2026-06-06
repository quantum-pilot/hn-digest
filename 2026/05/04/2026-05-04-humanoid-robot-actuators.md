# Humanoid Robot Actuators

- Score: 165 | [HN](https://news.ycombinator.com/item?id=48004380) | Link: https://www.firgelli.com/pages/humanoid-robot-actuators

- TL;DR  
  - The article is a deep engineering guide to why humanoid robots destroy ordinary actuators and why modern designs converge on similar solutions: very high torque/force per kilogram, back-drivable joints, and careful gear ratios that limit reflected inertia and heat. It explains the “mass penalty spiral,” strain-wave rotary joints vs planetary roller-screw linear legs, thermal limits (peak vs continuous torque), and the need for torque control. HN readers praise the technical framing but question AI-authored personas, flawed AI diagrams, and humanoid legs as the best morphology.

- Comment pulse  
  - Modern locomotion needed money + parts → 1990s theory knew torque control/back-drivability, but actuators, valves, and funding weren’t there; drones later made BLDCs cheap.  
  - AI “chief engineer” and blatantly wrong diagrams → undermines trust and suggests careless marketing — counterpoint: core systems-level physics still reads broadly correct.  
  - Humanoid legs vs torso-on-wheels → legs match human infrastructure and terrains, simplify teleoperation mapping, but cost more energy, complexity, and are overkill in controlled, wheelchair-accessible spaces.

- LLM perspective  
  - View: Treat this as a conceptual map of constraints; ignore branding and verify numbers/diagrams against primary robotics literature.  
  - Impact: Actuator density, back-drivability, and continuous-torque cooling will gate which humanoid platforms become economically useful.  
  - Watch next: Compare open-source actuators, thermally characterized benchmarks, and safety standards for torque-controlled, back-drivable industrial humanoids.
