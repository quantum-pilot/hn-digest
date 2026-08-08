# Humanoid Robot Actuators

- Score: 165 | [HN](https://news.ycombinator.com/item?id=48004380) | Link: https://www.firgelli.com/pages/humanoid-robot-actuators

### TL;DR

The guide argues that humanoid actuators must survive about 5,000 impact-heavy steps per hour while remaining light, backdrivable, torque-controlled, and thermally sustainable. It favors rotary drives for major rotational joints and roller-screw linear drives where shock and force density dominate, while explaining the trade-off between low gearing for compliance and high gearing for strength. Its deeper point is that continuous torque and fatigue matter more than demo-ready peak ratings. Commenters broadly accepted the systems framing but challenged the author’s AI avatar and identified mechanically impossible details in several generated diagrams.

### Comment pulse

- Robotics veterans credited modern motors, controllers, ML, and sustained capital — counterpoint: Boston Dynamics demonstrated locomotion earlier, though not commercial economics.
- Incorrect gear teeth, roller alignment, and contact geometry in illustrations made the article unsafe as a precise engineering reference.
- Humanoid legs trade efficiency and complexity for stairs, rough terrain, and compatibility with spaces and tools built around human bodies.

### LLM perspective

- Treat the prose as a conceptual map; independently verify every equation, threshold, and diagram.
- Compare architectures on continuous duty cycles, shock survival, serviceability, energy use, and payload—not acrobatics.
- Watch open actuator projects for reproducible bills of materials, test rigs, fatigue curves, and thermal results.
