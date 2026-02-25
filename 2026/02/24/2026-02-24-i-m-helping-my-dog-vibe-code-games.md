# I'm helping my dog vibe code games

- Score: 541 | [HN](https://news.ycombinator.com/item?id=47139675) | Link: https://www.calebleak.com/posts/dog-game/

### TL;DR
- An ex-Meta research engineer built a system where his dog Momo “codes” Godot games by mashing a Bluetooth keyboard while Claude Code interprets the gibberish as cryptic game-design instructions. A Raspberry Pi proxy, Rust DogKeyboard app, and Zigbee treat dispenser create a closed loop: dog types, LLM builds, tools screenshot and play-test, and treats dispense. The main insight: good prompts plus strong automated feedback and linting can turn random input into surprisingly playable games, highlighting feedback loops over ideas.

### Comment pulse
- Fun demo, not paradigm shift → outputs are simple, buggy, depend on heavy human-engineered scaffolding — counterpoint: author argues about feedback-loop design, not dog creativity.  
- Sharp social commentary → dog generating code via LLM mirrors feeling that many modern apps are indistinguishable from vibe-coded slop by mediocre humans.  
- Humorous extrapolations → commenters joke about dog/LLM teams replacing engineers, reference infinite-monkey theorem and earlier experiments like a yucca plant “trading” stocks.  

### LLM perspective
- View: Shows robust tooling and automated QA can extract value from meaningless prompts, underscoring how framing and constraints steer LLMs.  
- Impact: Gamedev and tooling folks can reuse the screenshot/input harness, linters, and MCP-style bridges to harden their own AI-assisted workflows.  
- Watch next: Studies comparing dog-random, human-prompted, and manual pipelines could clarify where LLMs save time versus add debugging overhead.
