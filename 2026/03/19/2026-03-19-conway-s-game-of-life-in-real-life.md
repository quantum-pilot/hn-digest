# Conway's Game of Life, in real life

- Score: 313 | [HN](https://news.ycombinator.com/item?id=47434732) | Link: https://lcamtuf.substack.com/p/conways-game-of-life-in-real-life

- TL;DR  
  Hardware hacker lcamtuf builds a fully-physical Conway’s Game of Life: a 17×17 grid of illuminated NKK pushbutton switches, driven directly by an AVR128DA64 microcontroller. LEDs are multiplexed by rows/columns with MOSFETs handling up to ~2.5 A peak, plus a knob-controlled simulation speed. Firmware separates display refresh from logic and uses watchdog + blackout windows to avoid LED overcurrent on crashes. It’s intentionally overbudget, gloriously tactile, and explicitly not “cost‑optimized”—more an art object than a product.

- Comment pulse  
  Physical-only digital toys feel magical → sparks dreams of actuated 3D tabletops for games; commenters riff on mechanics and repair challenges.  
  Overspending on parts is embraced → “reasonable budget ×10” resonates as the true cost of serious hobbies.  
  Cheaper options exist → Launchpads or generic lit buttons could cut cost, but add gaps/compromises; many mainly celebrate the idiosyncratic, clearly non-LLM writing.

- LLM perspective  
  View: Shows why bespoke hardware art still matters: tactility and constraint create experiences screens can’t match.  
  Impact: Likely to inspire copycats and variants, especially in maker education and interactive exhibits.  
  Watch next: Community forks that trade NKK switches for cheaper keypads or flip-dots, with documented BOMs, failure modes, and repair strategies.
