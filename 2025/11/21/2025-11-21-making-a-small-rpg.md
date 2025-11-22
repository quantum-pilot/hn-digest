# Making a Small RPG

- Score: 160 | [HN](https://news.ycombinator.com/item?id=46004293) | Link: https://jslegenddev.substack.com/p/making-a-small-rpg

### TL;DR
The author documents designing a “small but complete” RPG that can be built in 1–2 months by aggressively scoping based on classic games. From Dragon Quest comes a tiny overworld that still feels expansive and opt‑in encounters; from Undertale and Just One Boss, a real‑time bullet‑hell combat system; from Breath of the Wild and Elden Ring, an open world with a single always-available final boss and XP-as-currency upgrades lost on death. They implement it in JavaScript with Kaplay, trimming systems (items, stamina, extra stats) and investing in strong pixel art, enemy patterns, and variable rewards for no‑hit victories. HN commenters trade tips on art assets, tools like Phaser/Tiled/Love2D, and praise Kaplay and the author’s tutorials.

---

### Comment pulse
- Use shared art assets → Liberated Pixel Cup and Kenney packs let non‑artists prototype whole games quickly—counterpoint: still need customization to avoid a generic look.  
- 2D web RPGs are approachable → Phaser plus Tiled (or Love2D + Tiled) makes world-building easy, especially with Lua export and flexible map formats.  
- Kaplay is appreciated → commenters find it fun and different, note prior JS game-dev posts, plus some joking confusion over “RPG” meaning and past HN discussions.

---

### LLM perspective
- View: This is a solid template for scoping an RPG: copy constraints from retro titles, then ruthlessly cut mechanics.  
- Impact: Solo devs gain a realistic path from “RPG dream” to shippable prototype without engines like Unity or Godot.  
- Watch next: Public demo, difficulty feedback on bullet patterns, balancing the XP/heal economy, and whether the open structure feels meaningful or thin.
