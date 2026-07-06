# If you're a button, you have one job

- Score: 528 | [HN](https://news.ycombinator.com/item?id=48790689) | Link: https://unsung.aresluna.org/if-youre-a-button-you-have-one-job/

### TL;DR
Author argues that UI buttons should maintain a strict contract: every acknowledged press equals one action. They criticize the Nothing Phone’s photo-rotation button, which emits haptic/sound feedback for each tap but silently drops extra presses during its rotation animation, breaking that contract and making rapid multi-rotations unpredictable, especially for accessibility users. Commenters debate debouncing vs buffering, note that real buttons juggle multiple jobs (state, feedback, action), and explain how typical UI frameworks let visual feedback drift out of sync with actual behavior.

*Content unavailable; summarizing from title/comments.*

### Comment pulse
- One-press-one-action contract → If a tap produces haptic/sound, it must trigger the action or none at all—counterpoint: some accessibility users want extra presses discarded.  
- Buttons juggle multiple roles → Label intended action, reflect mode, execute commands, show progress; “you had one job” framing hides this complexity.  
- Desynced feedback is common → UI components animate instantly, while handlers may cancel or fail actions, so color changes or beeps no longer guarantee success.  

### LLM perspective
- View: Treat input events and side effects transactionally: either both feedback and action occur, or neither, per press.  
- Impact: Clearer button contracts reduce cognitive load, help motor-impaired users, and cut subtle bugs in high-frequency actions like photo browsing.  
- Watch next: System-wide accessibility toggles for tap debouncing and repeat-ignoring seem preferable to every app inventing conflicting button behaviors.
