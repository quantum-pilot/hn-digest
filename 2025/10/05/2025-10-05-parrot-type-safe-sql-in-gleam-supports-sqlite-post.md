# Parrot – type-safe SQL in Gleam, supports SQlite, PostgreSQL and MySQL

- Score: 110 | [HN](https://news.ycombinator.com/item?id=45478033) | Link: https://github.com/daniellionel01/parrot

### TL;DR

Parrot generates type-safe Gleam wrappers from SQL queries by orchestrating sqlc, with support for SQLite, PostgreSQL, and MySQL. It discovers SQL files under `src`, can obtain schemas automatically, supports named parameters, and emits a single project module that remains database-client agnostic, with wrappers for sqlight and pog. Generation must run on Erlang, though copied output can target JavaScript. The author documents important limits: unsupported sqlc annotations panic, complex types may become dynamic, and multidimensional PostgreSQL arrays can be misidentified.

### LLM perspective

- View: Parrot makes handwritten SQL more usable in Gleam without hiding the query layer behind an ORM.
- Impact: Compile-time wrappers can catch integration mistakes, but unsupported annotations and dynamic fallbacks narrow the guarantee.
- Watch next: Broader sqlc annotation coverage and more reliable PostgreSQL type discovery would strengthen production confidence.
