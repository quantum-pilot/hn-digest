# I write games in C (yes, C) (2016)

- Score: 157 | [HN](https://news.ycombinator.com/item?id=46925808) | Link: https://jonathanwhiting.com/writing/blog/games_in_c/

### TL;DR
An indie developer (writing in 2016) explains why all his solo games are in plain C: he wants reliability, extreme portability, fast compilation, strict typing, good tooling, and a tiny feature set, and dislikes OOP and GC pauses. He finds C++/C#/Java too complex, Go and the web stack ill-suited for games, Haxe and DIY languages too risky. C remains a dangerous but predictable “sharp knife.” HN replies debate C vs “C++ subsets,” compile times, and highlight Zig, Odin, and Rust as modern alternatives.

---

### Comment pulse
- C as enforced C++ subset → guarantees simplicity and avoids surprise features; C++ subsets drift as teams change and libraries pull in unwanted complexity.  
- Zig/Odin/Rust positioning → Zig tightens C’s model and replaces the preprocessor; Odin targets Go-like simplicity sans GC; Rust covers correctness-heavy, concurrent systems.  
- Real-world C games → titles and idTech3 mods still ship in C, but timing quirks and toolchains hurt — counterpoint: some deem C-only dev “crazy.”  

---

### LLM perspective
- View → For solo gamedev, simplicity and fast builds can outweigh safety features and abstractions, especially when targeting long-term portability.  
- Impact → New C-like languages absorb C’s lessons, but its stable ABI and tooling keep it a primary interoperability target.  
- Watch next → Benchmark small games in C, Zig, Odin, Rust to compare compile times, tooling friction, memory behavior, and console/web deployment effort.
