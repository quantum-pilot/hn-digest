# The compiler is your best friend

- Score: 127 | [HN](https://news.ycombinator.com/item?id=46445131) | Link: https://blog.daniel-beskin.com/2025-12-22-the-compiler-is-your-best-friend-stop-lying-to-it

## TL;DR

The essay argues that compilers are underused collaborators: they can prove many program properties if we stop “lying” to them. Lies include nullable references, unchecked exceptions, unsafe casts, and opaque side-effectful functions, all of which hide important facts from the type system. Instead, use explicit option/result types, union/enum types, tiny domain-specific wrappers, and constructs like `NonEmptyList` to encode invariants so “illegal states are unrepresentable.” This shifts work from production outages to compile-time dialogue with the compiler.

---

## Comment pulse

- What to do when “this cannot happen”? → Many argue for encoding impossible states in types; others insist some cases should still crash hard—counterpoint: crashes can be business- and user-hostile.  

- Functional core / imperative shell in practice → Advice: separate data gathering, pure decision logic, and effect execution; represent intended side effects as data; books like “Grokking Simplicity” help.  

- Power and limits of types → Strong typing helps only if your domain model is right; modeling complex business domains can exceed human capacity despite languages like Swift, Rust, TypeScript.

---

## LLM perspective

- View: The piece highlights that better type modeling reduces runtime uncertainty—exactly where LLM-generated code tends to be weakest.  

- Impact: Stronger, explicit types make LLM output easier to validate automatically and safer to integrate into large existing codebases.  

- Watch next: IDEs and codegen tools that propose union types, tiny types, and `Option/Result` refactors from existing untyped or loosely typed code.
