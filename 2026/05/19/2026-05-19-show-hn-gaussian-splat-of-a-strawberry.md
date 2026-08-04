# Show HN: Gaussian Splat of a Strawberry

- Score: 477 | [HN](https://news.ycombinator.com/item?id=48191602) | Link: https://superspl.at/scene/84df8849

### TL;DR

A highly detailed, interactive strawberry was reconstructed as a Gaussian splat from 90 viewpoints, each using 88 focus-stacked macro photographs, then trained with slang-splat and published as a 22.94 MB SuperSplat scene. Unlike a mesh, the result composites translucent oriented blobs to reproduce observed light, so moving too close reveals no true surface or interior. HN readers praised its smooth mobile rendering and unusual dreamlike degradation, while discussing capture effort, reconstruction artifacts, open-source PlayCanvas, and faster but constrained single-image alternatives.

### Comment pulse

- Users clarified splats model radiance, not geometry: blob positions need not coincide with the apparent surface, explaining penetration and invented interiors.
- Viewers loved graceful, fog-like degradation and mobile speed — counterpoint: some scenes showed foreground-order errors, weak exteriors, and missing boundary clipping.
- Single-image generation reportedly takes 30 seconds on M1 Pro and enables modest viewpoint shifts, but 2.6 GB weights impede browser deployment.

### LLM perspective

- View: Gaussian splats occupy a useful middle ground between photography and explicit 3D, favoring view fidelity over structural truth.
- Impact: Artists and spatial-capture users gain expressive, interactive scenes; measurement and collision workflows still need geometry or derived bounds.
- Watch next: Compare multi-view and single-image quality, load times, memory, mobile stability, artifact rates, and usable camera-motion range.
