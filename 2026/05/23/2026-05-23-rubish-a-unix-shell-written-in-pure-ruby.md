# Rubish: A Unix shell written in pure Ruby

- Score: 168 | [HN](https://news.ycombinator.com/item?id=48245262) | Link: https://github.com/amatsuda/rubish

## TL;DR
Rubish is a Unix shell implemented entirely in Ruby that parses standard shell syntax into Ruby and runs it on the Ruby VM. It aims for full Bash compatibility while deeply integrating Ruby: you can use Ruby expressions in conditionals, Ruby-style method calls and chains as pipelines, iterator blocks on command output, Ruby-style function definitions, programmable prompts, lazy background init, and an embeddable REPL API. A restricted mode disables Ruby features for untrusted scripts. HN loves the idea and name, but worries about portability and maintainability of the “vibe-coded” Ruby internals.

## Comment pulse
- Excitement + dread → powerful hybrid shell, but lack of ubiquity on remote machines means users would juggle two shells—counterpoint: that’s true of most non-bash shells.  
- Codebase concerns → long methods and fuzzy boundaries feel LLM-shaped, intimidating for contributors—counterpoint: solo OSS has often been messy; tools just change who can navigate it.  
- Broader wish → more language-native shells and richer scripting ergonomics (Ruby, Python, Scheme); performance vs Go is irrelevant compared to ergonomics and being faster than bash.  

## LLM perspective
- View: Great fit for Ruby-heavy workflows and experimentation, unlikely to displace standard login shells broadly.  
- Impact: Most useful for Rubyists, terminal/IDE authors, and people wanting a programmable interactive environment over pure POSIX sh.  
- Watch next: Adoption stories, remote-install tooling, plugin ecosystem, and whether the codebase evolves toward clearer structure for non-agent contributors.
