# Speeding up Unreal Editor launch by not spawning unused tooltips

- Score: 205 | [HN](https://news.ycombinator.com/item?id=45111273) | Link: https://larstofus.com/2025/09/02/speeding-up-the-unreal-editor-launch-by-not-spawning-38000-tooltips/

- TL;DR
    - An Unreal dev found the editor eagerly instantiates ~38k tooltip widgets during startup—spending up to 2–5s (debug) and ~40 MB RAM for UI you won’t see. Fix: defer creation—store FText on SetToolTip, build the widget on GetToolTip when hovered. Runtime impact is negligible (≤0.05 ms; one tooltip per frame). A PR implements this, and closing Settings/Preferences lowers counts further. HN echoes the pattern: lazy-init UI beats prebuilding components, and routine audits catch excessive call counts.

- Comment pulse
    - UE slows small-team iteration → heavy editor, Blueprint pain; AngelScript helps — counterpoint: with experience, UE productive; Unity easier but pricing worries.
    - Audit hot libraries regularly → invocation counts often dominate; flame charts misattribute; big wins from reducing unnecessary calls.
    - Lazy UI pays off → render tooltips/modals on demand or via single global instance/portal to cut idle cost; first-use may be slower.

- LLM perspective
    - View: Classic lazy-init win: store FText, instantiate tooltip on hover; avoids 38k widgets and RAM at startup.
    - Impact: Faster editor launch, lower baseline memory; best for users with Settings/Preferences closed and lighter default layouts.
    - Watch next: UE merge PR, measure cold-start delta across SKUs; audit other eager widget patterns; add engine-wide lazy tool/tooltip factories.
