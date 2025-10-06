# Parrot – type-safe SQL in Gleam, supports SQlite, PostgreSQL and MySQL

- Score: 110 | [HN](https://news.ycombinator.com/item?id=45478033) | Link: https://github.com/daniellionel01/parrot

TL;DR
Parrot brings sqlc-style, type-safe SQL to Gleam: write real SQL in src/sql/*.sql and get a generated Gleam module with typed functions and named parameters. It supports SQLite, PostgreSQL, and MySQL, auto-downloads sqlc, and infers schemas via pg_dump/mysqldump/sqlite3. Client-agnostic wrappers exist for pog/sqlight. Caveats: some sqlc annotations unsupported, some complex types are dynamic, multidimensional arrays misidentified, and codegen runs only on the Erlang target. HN welcomes SQL-first ergonomics but debates dynamic queries and SQL composability vs DSLs or query-fragment approaches.

Comment pulse
- SQL-first, sqlc-style is preferred for type-safe access → write real SQL; generator maps inputs/outputs — counterpoint: dynamic filters/order remain clumsy and can degrade plans.
- SQL composability is lacking → two routes: DSLs (PRQL/ORMs) add power but add languages; query-fragment literals (e.g., Slonik) compose well with normal functions.
- Interest beyond Gleam → requests for TypeScript integrations; some argue SQL’s limited parameterization harms DX, preferring query builders; pgtyped cited as middle ground.

LLM perspective
- View: Good thin wrapper over sqlc, bringing typed SQL and SQL-file workflows to Gleam without inventing a new DSL.
- Impact: Eases Gleam backend adoption; fewer ORMs; better tooling interop; DB schema changes caught at compile time.
- Watch next: Dynamic query composition, JS-first generation, array/type fixes, and unsupported annotations; watch Hex adoption, integration guides, and performance regressions.
